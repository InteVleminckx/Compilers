from AST import *

types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1"), None: ("void", "")}
calculations_ = {"+": "add", "-": "sub", "*": "mul", "/": "div", "%": "srem"}


class LLVM:

    def __init__(self):
        self.line = ""
        self.register = 0
        self.stringCount = 0

        self.assignmentStack = []
        self.functionCallStack = []
        self.returnStack = []
        self.printfStack = []

        self.enteredAssignment = False
        self.enteredFunctionCall = 0
        self.enteredReturn = False
        self.enteredPrintf = False

        self.returnType = ""
        self.hasReturnNode = (False, 0)
        self.curPrintf = 0

        self.printf = False
        self.scanf = False

        self.strings = []

    def enterFunction(self, node):
        print("enterFunction")

        # We enteren een nieuwe functie dus kunnen de registercount terug op 0 zetten
        self.register = 0

        # We beginnen eerst met de functie naam, return type ne parameters op te vragen
        self.returnType = node.parent.children[0].children[0].token
        functionName = str(node.parent.children[1].children[0].value)
        parameters = [(str(child.value), child.type) for child in node.parent.children[2].children]

        # We voegen het begin al toe aan de lijn van de functie
        self.line += "define dso_local "

        if self.returnType == "CHAR":
            self.line += "signext "
        self.line += types[self.returnType][0] + " @" + functionName + "("

        symboltable = tableLookup(node)

        # We gaan nu over de parameters om deze toe te voegen
        for i, param in enumerate(parameters):
            # Als we een none hebben betekent dat we geen parameters hebben
            if param[0] == "NONE":
                break

            # We voegen de types toe en de registers hiervoor
            self.line += types[param[1]][0] + " %" + str(i)

            # We vragen het symbool ook op uit de symbol table zodat we het juiste
            # register eraan kunnen toekennen
            symbol_lookup = symbolLookup(param[0], symboltable)[1]
            symbol_lookup.register = i

            # Als het een parameter is zetten we dit ook op true
            symbol_lookup.isParam = True

            # We verhogen ook de registercount al
            self.register += 1

            if i < len(parameters) - 1:
                self.line += ", "

        # sluiten de functie definitie
        self.line += ") {\n"

        # We verhogen de registercount nog maals 1 keer
        self.register += 1

        # We gaan eerst nog controleren of we een return node hebben
        # Zoniet en het is geen void dan maken we hier ook nog een register voor vrij

        if len(node.children) == 0:
            self.noReturn()
        elif node.children[-1].token != "RETURN" and self.returnType is not None:
            self.noReturn()
        else:
            self.hasReturnNode = True, 0

        # We gaan nu alle variable alloceren binnen de scope
        self.allocateVariables(symboltable)

    def exitFunction(self, node):
        print("exitFunction")
        if not self.hasReturnNode[0]:
            if self.returnType is not None:
                reg = self.load(str(self.hasReturnNode[1]), self.returnType)
                self.line += "  ret " + types[self.returnType][0] + " %" + str(reg)
            else:
                self.line += "  ret void"

            self.line += "\n}\n\n"

    def enterReturn(self, node):
        print("enterReturn")
        self.enteredReturn = True
        if self.returnType is None:
            self.line += "  ret void"
            self.enteredReturn = False

        # Als we een return hebben met 1 child (enkel identifier of value) kunnen we dit al direct doen
        # Wanneer dit niet het geval is zullen er eerst andere dingen moeten gebeuren en daarom zal de return in de exit functie gebeuren
        elif len(node.children[0].children) == 0:
            self.enteredReturn = False
            # Controleren of de node als kind een value of indentifier heeft
            if node.children[0].token == "IDENTIFIER":
                # We moeten dan de register hiervan opvragen en returnen
                symboltable = tableLookup(node.children[0])
                symbol_lookup = symbolLookup(str(node.children[0].value), symboltable)[1]
                reg = symbol_lookup.register
                reg = self.load(reg, self.returnType)
                self.line += "  ret " + types[self.returnType][0] + " %" + str(reg)

            else:
                # Als het een char is moeten we deze eerst nog omzetten naar een integer
                val = str(node.children[0].value)
                if self.returnType == "CHAR":
                    val = str(ord(str(node.children[0].value)[1]))

                self.line += "  ret " + types[self.returnType][0] + " " + val

        if not self.enteredReturn:
            self.line += "\n}\n\n"

    def exitReturn(self, node):
        print("exitReturn")
        # We controleren nog of we nog de return moeten toepassen, dit is het geval wanneer de bool nog op true staat
        if self.enteredReturn:
            # Op dit moment zou er ook nog maar 1 element in de stack mogen zitten die die uitkomst bevat
            elem = self.returnStack[-1]
            self.returnStack.pop()
            # We returen dit register nog
            self.line += "  ret " + types[elem[1]][0] + " %" + str(elem[0])
            self.enteredReturn = False
            self.line += "\n}\n\n"

    def enterPrintf(self, node):
        print("enterPrintf")
        self.enteredPrintf = True
        # We predefinen hier al de count voor de string links in de printf functie omdat er nadien nog kunnen toegevoegd worden
        self.curPrintf = self.stringCount
        self.stringCount += 1

    def exitPrintf(self, node):
        print("exitPrintf")
        if self.enteredPrintf:
            self.enteredPrintf = False
            textLeft = str(node.children[0].value)
            textsize = len(textLeft)
            addsize = 0

            # We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
            if textsize > 1:
                if textLeft[len(textLeft) - 2:len(textLeft)] != "\\n":
                    addsize += 1
                else:
                    text = textLeft[0:len(textLeft) - 2]
                    text += "\\0A"
            textsize += addsize
            textLeft += "\\00"
            self.strings.append((textsize, str(self.curPrintf), textLeft))
            inbound = "[" + str(textsize) + " x i8], [" + str(textsize) + " x i8]*"
            str_ = "@.str"
            str_ += str(self.curPrintf) if self.curPrintf > 0 else ""
            self.line += "  %" + str(
                self.register) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds (" + inbound + " " + str_ + ", i64 0, i64 0)"
            self.register += 1
            for i in range(len(self.printfStack)):
                elem = self.printfStack[i]
                self.line += ", "
                if elem[1] == "TEXT":
                    self.line += "i8* getelementptr inbounds ("
                    inbound = "[" + str(elem[3]) + " x i8], [" + str(elem[3]) + " x i8]*"
                    self.line += inbound
                    str_ = "@.str"
                    str_ += str(elem[0]) if int(elem[0]) > 0 else ""
                    self.line += " " + str_ + ", i64 0, i64 0)"
                else:
                    self.line += types[elem[1]][0] + " "
                    self.line += "%" + str(elem[0]) if elem[2] else str(elem[0])

            self.printfStack.clear()
            self.enteredPrintf = False
            self.line += ")\n"

    def enterScanf(self, node):
        print("enterScanf")

    def exitScanf(self, node):
        print("exitScanf")

    def enterIf_stmt(self, node):
        print("enterIf_stmt")

    def exitIf_stmt(self, node):
        print("exitIf_stmt")

    def enterElse_stmt(self, node):
        print("enterElse_stmt")

    def exitElse_stmt(self, node):
        print("exitElse_stmt")

    def enterWhile_stmt(self, node):
        print("enterWhile_stmt")

    def exitWhile_stmt(self, node):
        print("exitWhile_stmt")

    def enterAssignment(self, node):
        print("enterAssignment")
        self.enteredAssignment = True

        # Als we gewoon een assignment hebben van een value aan een variable kunnen we dit direct hier doen

        if len(node.children[1].children) == 0:
            # We vragen de symbol lookup op van het linker deel
            symboltable = tableLookup(node)
            symbol_lookup = symbolLookup(str(node.children[0].value), symboltable)[1]
            reg1 = symbol_lookup.register
            type1 = node.children[0].type
            # Dan controleren we nog of de rechterkant een identifier is of niet
            if node.children[1].token == "IDENTIFIER":
                # Moeten hiervoor zijn register ook terug opvragen
                symboltable2 = tableLookup(node.children[1])
                symbol_lookup2 = symbolLookup(str(node.children[1].value), symboltable2)[1]
                reg2 = symbol_lookup2.register
                self.store(reg2, reg1, type1, True, True)
            else:
                # We nemen hier gewoon de waarde zelf van het attribuut
                val = str(node.children[1].value)
                self.store(val, reg1, type1, False, True)

            # Na we dit hebben gedaan kunnen we enterAss terug afzetten
            self.enteredAssignment = False

    def exitAssignment(self, node):
        print("exitAssignment")

        # We controleren nog of we nog de assignment moeten toepassen, dit is het geval wanneer de bool nog op true staat
        if self.enteredAssignment:
            # Op dit moment zou er ook nog maar 1 element in de stack mogen zitten die die uitkomst bevat
            elem = self.assignmentStack[-1]
            self.assignmentStack.pop()
            # We vragen het register en type op van de variable
            symboltable = tableLookup(node.children[0])
            symbol_lookup = symbolLookup(str(node.children[0].value), symboltable)[1]
            reg = symbol_lookup.register
            type = symbol_lookup.type

            # En we doen store
            self.store(elem[0], reg, type, True, True)
            self.enteredAssignment = False

    def enterUnaryOperation(self, node):
        print("enterUnaryOperation")

    def exitUnaryOperation(self, node):
        print("exitUnaryOperation")

    def enterBreak(self, node):
        print("enterBreak")

    def exitBreak(self, node):
        print("exitBreak")

    def enterContinue(self, node):
        print("enterContinue")

    def exitContinue(self, node):
        print("exitContinue")

    def enterFuncCall(self, node):
        print("enterFuncCall")
        self.enteredFunctionCall += 1

    def exitFuncCall(self, node):
        print("exitFuncCall")

        # We moeten eerst het type van de functie opvragen
        funcName = str(node.children[0].children[0].value)
        symboltable = tableLookup(node.children[0].children[0])
        # Betekent dat we de naam van de functie hebben, hier moeten we niets mee doen
        symbol_lookup = symbolLookup(funcName, symboltable)[1]
        outputtype = symbol_lookup.outputTypes[0]

        self.line += "  %" + str(self.register) + " = call " + types[outputtype][0] + " @" + funcName + "("
        # Er zouden nu op zijn minst even elementen in de stack moeten zitten dan er parameters zijn voor de functie
        numberOfParams = len(node.children[1].children)
        for i in range(numberOfParams):
            # Zit er omgekeerd in dus moeten het er ook omgekeerd terug uithalen
            elem = self.functionCallStack[-(numberOfParams - i)]
            self.line += types[elem[1]][0]
            self.line += " %" + str(elem[0]) if elem[2] else " " + str(elem[0])
            if i < numberOfParams - 1:
                self.line += ", "

        for i in range(numberOfParams):
            self.functionCallStack.pop()

        self.line += ")\n"

        self.enteredFunctionCall -= 1
        self.register += 1

        if self.enteredFunctionCall > 0:
            self.functionCallStack.append((str(self.register - 1), outputtype, True))

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredReturn:
            self.returnStack.append((str(self.register - 1), outputtype, True))

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredPrintf:
            self.printfStack.append((str(self.register - 1), outputtype, True))

        # Ook hier kan het zijn dat we een recursieve call hebben van aanroepen in elkaar dus moeten we deze ook eerst voorrang geven
        elif self.enteredAssignment:
            # Als dit het geval is moet de register van deze function call worden toegevoegd aan de stack
            self.assignmentStack.append((str(self.register - 1), outputtype, True))

    def enterBinOperation(self, node):
        print("enterBinOperation")

    def exitBinOperation(self, node):
        print("exitBinOperation")
        # We controleren of we in een assignment zijn gegaan

        func = lambda node1, stack: (
            self.operate(calculations_[str(node1.value)], stack[-2][0], stack[-1][0], stack[-2][1], stack[-1][1],
                         stack[-2][2], stack[-1][2]))

        if self.enteredFunctionCall > 0:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toReg, toType = func(node, self.functionCallStack)
            self.functionCallStack.pop()
            self.functionCallStack.pop()
            self.functionCallStack.append((toReg, toType, True))
        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredReturn:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toReg, toType = func(node, self.returnStack)
            self.returnStack.pop()
            self.returnStack.pop()
            self.returnStack.append((toReg, toType, True))

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredPrintf:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toReg, toType = func(node, self.printfStack)
            self.printfStack.pop()
            self.printfStack.pop()
            self.printfStack.append((toReg, toType, True))

        elif self.enteredAssignment:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toReg, toType = func(node, self.assignmentStack)
            self.assignmentStack.pop()
            self.assignmentStack.pop()
            self.assignmentStack.append((toReg, toType, True))

    def enterIdentifier(self, node):
        print("enterIdentifier")

    def exitIdentifier(self, node):

        print("exitIdentifier")
        if node.parent.token == "NAME":
            return

        symboltable = tableLookup(node)
        # Betekent dat we de naam van de functie hebben, hier moeten we niets mee doen
        symbol_lookup = symbolLookup(str(node.value), symboltable)[1]

        func = lambda symbol_lookup: (self.load(symbol_lookup.register, symbol_lookup.type), symbol_lookup.type)

        # als we een functioncall hebben dan heeft dit voorrang op een assignment omdat een functioncall in een assignment kan voorkomen
        if self.enteredFunctionCall > 0:
            reg, type = func(symbol_lookup)
            self.functionCallStack.append((reg, type, True))
        # Ook hier heeft de functioncall voorang
        elif self.enteredReturn:
            reg, type = func(symbol_lookup)
            self.returnStack.append((reg, type, True))

        # Ook hier heeft de functioncall voorang
        elif self.enteredPrintf:
            reg, type = func(symbol_lookup)
            self.printfStack.append((reg, type, True))

        # We controleren of we in een assignment zijn gegaan en dat het niet het linkerdeel is van de assign
        elif self.enteredAssignment and node.parent.token != "=":
            # We voegen het toe aan de stack
            # We laden eerst de variable in een nieuw register
            # Moet wel eerst het huidige register opvragen
            reg, type = func(symbol_lookup)
            # We geven het register mee en het type en zeggen dat een register is
            self.assignmentStack.append((reg, type, True))

    def enterType(self, node):
        print("enterType")

    def exitType(self, node):
        print("exitType")

        # Functioncall krijgt voorrang
        if self.enteredFunctionCall > 0:
            self.functionCallStack.append((str(node.value), node.token, False))

        # Ook hier heeft de functioncall voorang
        elif self.enteredReturn:
            self.returnStack.append((str(node.value), node.token, False))

        # Ook hier heeft de functioncall voorang
        elif self.enteredPrintf:
            self.printfStack.append((str(node.value), node.token, False))

        # We controleren of we in een assignment zijn gegaan
        elif self.enteredAssignment:
            # We voegen het toe aan de stack
            # We geven de value mee en het type en zeggen dat het geen register is
            self.assignmentStack.append((str(node.value), node.token, False))

    def enterString(self, node):
        pass

    def exitString(self, node):

        if self.enteredPrintf:
            # Ookal kan dit enkel hier voorkomen, een check kan geen kwaad
            text = str(node.value)
            textsize = len(text)
            addsize = 0

            # We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
            if textsize > 1:
                if text[len(text) - 2:len(text)] != "\\n":
                    addsize += 1
                else:
                    text = text[0:len(text) - 2]
                    text += "\\0A"
            textsize += addsize
            text += "\\00"
            self.strings.append((textsize, str(self.stringCount), text))
            self.printfStack.append((str(self.stringCount), "TEXT", False, textsize))
            self.stringCount += 1

    def allocateVariables(self, symbolTable):
        # We vragen de dict op met alle variable
        toAllocate = symbolTable.dict
        params = []
        for key in toAllocate:

            type = toAllocate[key].type
            # We checken dan voor de zekerheid of het wel een identifier is
            if toAllocate[key].value.token == "IDENTIFIER" or toAllocate[key].value.parent.children[
                0].token == "IDENTIFIER":
                tempReg = toAllocate[key].register
                toAllocate[key].register = self.register
                self.allocate(self.register, type)
                self.register += 1
                if toAllocate[key].isParam:
                    params.append((tempReg, toAllocate[key].register, toAllocate[key].type))

        # Nu gaan we de parameters hun waarde storen in de nieuwe registers
        for param in params:
            self.store(param[0], param[1], param[2], True, True)

    def allocate(self, register, type):
        self.line += "  %" + str(register) + " = alloca " + types[type][0] + ", " + types[type][1] + "\n"

    def store(self, fromRegister, toRegister, type, isReg1, isReg2):

        reg1 = "%" + str(fromRegister) if isReg1 else str(fromRegister)
        reg2 = "%" + str(toRegister) if isReg2 else str(toRegister)

        if type == "CHAR" and not isReg1:
            reg1 = str(ord(str(reg1[1])))

        if type == "FLOAT":
            if not isReg1:
                reg1 = str(reg1) + "e+00"
            if not isReg2:
                reg2 = str(reg2) + "e+00"

        self.line += "  store " + types[type][0] + " " + reg1 + ", " + types[type][0] + "* " + reg2 + "" \
                                                                                                      ", " + \
                     types[type][1] + "\n"

    def load(self, fromReg, type):
        self.line += "  %" + str(self.register) + " = load " + types[type][0] + ", " + types[type][0] + "* %" + str(
            fromReg) + ", " + types[type][1] + "\n"
        self.register += 1
        return self.register - 1

    def operate(self, operation, num1, num2, type1, type2, isReg1, isReg2):

        type = "INT"
        if type1 == "FLOAT" or type2 == "FLOAT":
            type = "FLOAT"

        if type == "FLOAT":
            # Moest 1 van de 2 types een int zijn moeten we deze eerst nog omzetten naar een float
            if type1 == "INT":
                # Check of het een register is of niet.
                if not isReg1:
                    num1 = str(num1) + ".0e+00"
                else:
                    self.line += "  %" + str(self.register) + " = sitofp i32 %" + str(num1) + " to float\n"
                    left = str(self.register)
                    self.register += 1

                self.line += "  %" + str(self.register) + " = f" + operation + " float "
                self.line += "%" if isReg1 else ""
                self.line += str(num1) + ", "
                self.line += "%" if isReg2 else ""
                self.line += str(num2) + "\n"

            elif type2 == "INT":
                # Check of het een register is of niet.
                if not isReg2:
                    num2 = str(num2) + ".0e+00"
                else:
                    self.line += "  %" + str(self.register) + " = sitofp i32 %" + str(num2) + " to float\n"
                    num2 = str(self.register)
                    self.register += 1

                self.line += "  %" + str(self.register) + " = f" + operation + " float "
                self.line += "%" if isReg1 else ""
                self.line += str(num1) + ", "
                self.line += "%" if isReg2 else ""
                self.line += str(num2) + "\n"

            else:
                # Allebei float
                self.line += "  %" + str(self.register) + " = f" + operation + " float "
                self.line += "%" if isReg1 else ""
                self.line += str(num1) + ", "
                self.line += "%" if isReg2 else ""
                self.line += str(num2) + "\n"

        elif type == "INT":
            if operation == "div":
                operation = "sdiv"

            self.line += "  %" + str(self.register) + " = " + operation + " i32 "
            self.line += "%" if isReg1 else ""
            self.line += str(num1) + ", "
            self.line += "%" if isReg2 else ""
            self.line += str(num2) + "\n"

        self.register += 1
        return self.register - 1, type

    def noReturn(self):
        self.line += "  %" + str(self.register) + " = alloca " + types[self.returnType][0] + ", " + \
                     types[self.returnType][1] + "\n"
        self.register += 1
        self.line += "  %" + str(self.register) + " = load " + types[self.returnType][0] + ", " + \
                     types[self.returnType][0] + "* %" + str(self.register - 1) + ", " + types[self.returnType][
                         1] + "\n"
        self.hasReturnNode = (False, self.register)
        self.register += 1
