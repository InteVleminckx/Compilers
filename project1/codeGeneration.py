from AST import *



types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1")}

class funcNode:

    def __init__(self, line, number, state, register):
        self.line = line
        self.functionNumber = number
        self.isOpen = state
        self.registerCounter = register

class LLVM:

    def __init__(self, tree):
        self.tree = tree
        self.strings = list()
        self.file = None
        self.functions = list()
        self.isPrintf = False
        self.isScanf = False
        self.registerCount = 1
        self.line = ""

    def toLLVM(self, inputfile):

        afterSlash = re.search("[^/]+$", inputfile)
        pos = afterSlash.start()
        inputfile = inputfile[pos:]
        filename = str(inputfile[:len(inputfile) - 2]) + ".ll"
        self.file = open("llvm_files/" + filename, "w")

        if self.tree.root is None:
            return

        self.generateLLVM(self.tree.root)

        for strings in self.strings:
            self.file.write(self.printStrings(*strings))

        self.file.write(self.line)

        if self.isPrintf:
            self.file.write(self.printfFunction())

        if self.isScanf:
            self.file.write(self.scanfFunction())

        self.file.close()


    def generateLLVM(self, node):

        for i, child in enumerate(node.children):

            if child.value == "FUNC_DEF":
                self.function(child)
            if child.value == "RETURN":
                self.returnFunction(node)
            if child.token == "PRINTF":
                self.printf(child)
            if child.token == "SCANF":
                self.scanf(child)
            if child.token == "IF":
                self.if_stmt(child)
            if child.token == "WHILE":
                self.while_stmt(child)
            if child.token == "=":
                self.storeNew(child)
            #Zie dat deze op het laatste staat
            if i == len(node.children)-1 and node.value == "FUNC_DEF":
                self.returnFunction(node)

            self.generateLLVM(child)


    # def addition(self, value, var, register, float=False):
    #     """
    #     :param value: De waarde/andere variable die bij de var wordt opgeteld (node)
    #     :param var: De variable waar de value wordt opgeteld. (node)
    #     :param register: Het register nummer waar we de uitkomst in wegschrijven
    #     :param float: Geeft aan of een een add of fadd is.
    #     :return: De register nummber en de line die wegschreven moeten worden in het bestand
    #     """
    #
    #     #0 = value, 1 = var
    #     registers = [None, None]
    #     type = "FLOAT"
    #     line = ""
    #
    #     # Moest 1 van de 2 maar een float zijn moeten we eerst nog de int omzetten naar een float
    #     if float:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #         if value.type == "INT":
    #             registers[0], lineValue = intToFloat(registers[0])
    #             line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #         if var.type == "INT":
    #             registers[1], lineVar = intToFloat(registers[1])
    #             line += lineVar
    #
    #         line += "%" + str(registerCount) + " = fadd float %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #
    #     else:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #
    #         line += "%" + str(registerCount) + " = add i32 %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #         type = "INT"
    #
    #     line += store(registerCount, register, type)
    #
    #     return line
    #
    # def subtract(self, value, var, register, float=False):
    #     """
    #     :param value: De waarde/andere variable die bij de var wordt opgeteld (node)
    #     :param var: De variable waar de value wordt opgeteld. (node)
    #     :param register: Het register nummer waar we de uitkomst in wegschrijven
    #     :param float: Geeft aan of een een sub of fsub is.
    #     :return: De register nummber en de line die wegschreven moeten worden in het bestand
    #     """
    #
    #     # 0 = value, 1 = var
    #     registers = [None, None]
    #     type = "FLOAT"
    #     line = ""
    #
    #     # Moest 1 van de 2 maar een float zijn moeten we eerst nog de int omzetten naar een float
    #     if float:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #         if value.type == "INT":
    #             registers[0], lineValue = intToFloat(registers[0])
    #             line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #         if var.type == "INT":
    #             registers[1], lineVar = intToFloat(registers[1])
    #             line += lineVar
    #
    #         line += "%" + str(registerCount) + " = fsub float %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #
    #     else:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #
    #         line += "%" + str(registerCount) + " = sub i32 %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #         type = "INT"
    #
    #     line += store(registerCount, register, type)
    #
    #     return line

    def allocateVariables(self, symbolTable):
        toAllocate = symbolTable.dict
        for key in toAllocate:

            if toAllocate[key].value.parent.children[0].token == "IDENTIFIER":
                type = toAllocate[key].type
                toAllocate[key].register = self.registerCount
                self.line += self.allocate(self.registerCount, type)
                self.registerCount += 1


    def function(self, node):
        table, name = getSymbolFromTable(node.parent.children[1].children[0])
        symbolTable = tableLookup(node)
        symbol_lookup = symbolLookup(node.value, symbolTable)

        return_type = table.type
        parameters = table.functionParameters

        self.line += "\ndefine dso_local " + types[return_type][0] + " @" + name + "() {\n"

        #Alloceer een register voor deze return
        if return_type != "void":
            self.line += self.allocate(self.registerCount, return_type)
            #store deze waarde ook
            #TODO: controleer dit nog later
            self.store(0, self.registerCount, return_type, False, True)
            self.registerCount += 1

        #TODO: parameters moeten nog worden toegevoegd maar momenteel doen we dit nog niet

        self.allocateVariables(symbolTable)

        #Nu gaan we zien dat er assignments zijn
        for child in node.children:
            if child.token == "=":
                #TODO: hier verder werken voor de assignments
                pass

    def returnFunction(self, node):

        # We nemen de laatst toegevoegde functie waar nog een return aan toegevoegd moet worden

        if node.token == "FUNC_DEF":
            # TODO: Check bij void ook
            returnType = node.parent.children[0].children[0].value
            #Geval return opgegeven
            if node.children[len(node.children) - 1].token == "RETURN":
                # symbolTable = tableLookup(node)

                returnNode = node.children[len(node.children) - 1].children[0]
                returnValue = str(returnNode.value)
                returnToken = returnNode.token
                #TODO: lookup in symbol table
                if returnToken == "IDENTIFIER":
                    pass
                else:
                    self.line += "  ret " + types[returnType][0] + " " + str(returnValue) + "\n}\n\n"

            #Geval return niet opgegeven
            else:
                if returnType == "INT":
                    self.line += "  ret " + "i32" + " 0\n}\n\n"
                elif returnType == "FLOAT":
                    self.line += "  ret " + "i32" + " 0\n}\n\n"
                elif returnType == "CHAR":
                    pass

    def printf(self, node):
        self.isPrintf = True
        # line = ""
        # func = self.functions[len(self.functions) - 1]
        #check eerst of er geen functie meer openstaat
        # if func.isOpen:
        #     line = func.line
        text = node.children[0].value
        # register = func.registerCounter
        params = parseFuncCallParameters(text)

        #Als de lengte nul is betekent dat we gewoon een string hebben

        textsize = len(text)
        addsize = 0
        strname = text
        #We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
        if len(text) > 1:
            if text[len(text) - 2:len(text)] != "\\n":
                addsize += 1
            else:
                text  = text[0:len(text) - 2]
                text += "\\0A"
        textsize += addsize
        text += "\\00"

        inbound = "[" + str(textsize) + " x i8]"

        self.line += "  %" + str(self.registerCount) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds (" + inbound + ", " \
                "" + inbound + "* "

        stringnumber = "@.str"
        exists = False
        # check if string is in self.strings anders maak nieuwe aan
        for number, textt, inbound1 in self.strings:
            if textt == text:
                stringnumber = number
                exists = True
                break

        if not exists and len(self.strings) > 0:
            stringnumber = "@.str" + str(len(self.strings))
            self.strings.append((stringnumber, text, inbound))

        elif len(self.strings) == 0:
            self.strings.append((stringnumber, text, inbound))

        self.line += stringnumber + ", i64 0, i64 0)"
        if len(params) == 0:
            self.line += ")\n"
        else:
            
            for i, child in enumerate(node.children):
                if (i == 0):
                    continue
                else:
                    if i <= len(node.children) - 1:
                        self.line += ", "
                    if node.children[i].token == "INT":
                        self.line += "i32 " + str(node.children[i].value)
                    elif node.children[i].token == "FLOAT":
                        self.line += "double " + str(node.children[i].value)
                    elif node.children[i].token == "CHAR":
                        number = ord(str(node.children[i].value)[1])
                        self.line += "i32 " + str(number)
                    elif node.children[i].token == "STRING":
                        text = node.children[i].value
                        textsize = len(text)
                        addsize = 0
                        strname = text
                        # We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
                        if len(text) > 1:
                            if text[len(text) - 2:len(text)] != "\\n":
                                addsize += 1
                            else:
                                text = text[0:len(text) - 2]
                                text += "\\0A"
                        textsize += addsize
                        text += "\\00"

                        inbound = "[" + str(textsize) + " x i8]"

                        self.line += "i8* getelementptr inbounds (" + inbound + ", " + inbound + "* "


                        stringnumber = "@.str"
                        exists = False
                        # check if string is in self.strings anders maak nieuwe aan
                        for number, textt, inbound1 in self.strings:
                            if textt == text:
                                stringnumber = number
                                exists = True
                                break

                        if not exists and len(self.strings) > 0:
                            stringnumber = "@.str" + str(len(self.strings))
                            self.strings.append((stringnumber, text, inbound))

                        elif len(self.strings) == 0:
                            self.strings.append((stringnumber, text, inbound))

                        self.line += stringnumber + ", i64 0, i64 0)"

            self.line += ")\n"

        self.registerCount += 1
        # func.line = line

    def scanf(self, node):

        self.isScanf = True

        text = node.children[0].value
        params = parseFuncCallParameters(text)

        # Als de lengte nul is betekent dat we gewoon een string hebben

        textsize = len(text)
        addsize = 0
        # We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
        if len(text) > 1:
            if text[len(text) - 2:len(text)] != "\\n":
                addsize += 1
            else:
                text = text[0:len(text) - 2]
                text += "\\0A"
        textsize += addsize
        text += "\\00"

        inbound = "[" + str(textsize) + " x i8]"

        self.line += "  %" + str(
            self.registerCount) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds (" + inbound + ", " \
                                                                                                            "" + inbound + "* "

        stringnumber = "@.str"
        exists = False
        # check if string is in self.strings anders maak nieuwe aan
        for number, textt, inbound1 in self.strings:
            if textt == text:
                stringnumber = number
                exists = True
                break

        if not exists and len(self.strings) > 0:
            stringnumber = "@.str" + str(len(self.strings))
            self.strings.append((stringnumber, text, inbound))

        elif len(self.strings) == 0:
            self.strings.append((stringnumber, text, inbound))

        self.line += stringnumber + ", i64 0, i64 0)"
        if len(params) == 0:
            self.line += ")\n"
        else:

            for i, child in enumerate(node.children):
                if (i == 0):
                    continue
                else:
                    if i <= len(node.children) - 1:
                        self.line += ", "
                    if node.children[i].token == "INT":
                        self.line += "i32 " + str(node.children[i].value)
                    elif node.children[i].token == "FLOAT":
                        self.line += "double " + str(node.children[i].value)
                    elif node.children[i].token == "CHAR":
                        number = ord(str(node.children[i].value)[1])
                        self.line += "i32 " + str(number)
                    elif node.children[i].token == "STRING":
                        text = node.children[i].value
                        textsize = len(text)
                        addsize = 0
                        strname = text
                        # We controleren of er een \n bij de tekst staat, moest dit niet zo zijn dan doen we nog +1
                        if len(text) > 1:
                            if text[len(text) - 2:len(text)] != "\\n":
                                addsize += 1
                            else:
                                text = text[0:len(text) - 2]
                                text += "\\0A"
                        textsize += addsize
                        text += "\\00"

                        inbound = "[" + str(textsize) + " x i8]"

                        self.line += "i8* getelementptr inbounds (" + inbound + ", " + inbound + "* "

                        stringnumber = "@.str"
                        exists = False
                        # check if string is in self.strings anders maak nieuwe aan
                        for number, textt, inbound1 in self.strings:
                            if textt == text:
                                stringnumber = number
                                exists = True
                                break

                        if not exists and len(self.strings) > 0:
                            stringnumber = "@.str" + str(len(self.strings))
                            self.strings.append((stringnumber, text, inbound))

                        elif len(self.strings) == 0:
                            self.strings.append((stringnumber, text, inbound))

                        self.line += stringnumber + ", i64 0, i64 0)"

            self.line += ")\n"

        self.registerCount += 1

    def if_stmt(self, node):

        compOp = node.parent.children[0].children[0].value
        left = node.parent.children[0].children[0].value
        compOp = node.parent.children[0].children[0].value


    def while_stmt(self, node):
        pass

    def printfFunction(self):
        return "declare dso_local i32 @printf(i8*, ...) "

    def scanfFunction(self):
        return "declare dso_local i32 @__isoc99_scanf(i8*, ...) "

    def printStrings(self, number, text, inboud):
        return number + " = private unnamed_addr constant " + inboud + " c\"" + text + "\", align 1\n"

    def scanStrings(self, number, text, inboud):
        return number + " = private unnamed_addr constant " + inboud + " c\"" + text + "\", align 1\n"

    def load(self, type, register):

        return self.registerCount, "%" + str(self.registerCount) + " = load " + types[type][0] + ", " + types[type][0] + "* " \
                                                                                                               "%" + str(register) + ", " + types[type][1] + "\n"
    def store(self, fromRegister, toRegister, type, isReg1, isReg2):

        reg1 = "%" + str(fromRegister) if isReg1 else str(fromRegister)
        reg2 = "%" + str(toRegister) if isReg2 else str(toRegister)

        self.line += "  store " + types[type][0] + " " + reg1 + ", " + types[type][0] + "* " + reg2 + "" \
            ", " + types[type][1] + "\n"

    def storeNew(self, node):

        symbolTable = tableLookup(node).dict
        #TODO: Lookup in table naar zijn register
        if node.children[1].token == "IDENTIFIER":
            pass
        else:
            for key in symbolTable:
                if str(key) == str(node.children[0].value):
                    register = symbolTable[key].register
                    type = symbolTable[key].type
                    value = node.children[1].value
                    self.store(value, register, type, False, True)

    def allocate(self, register, type):
        return "  %" + str(register) + " = alloca " + types[type][0] + ", " + types[type][1] + "\n"

def multiply():
    pass
def divide():


    pass


# def intToFloat(register):
#     """
#     Krijgt een integer binnen en zet deze om naar een float
#     :param register: De ingeladen register
#     :return: node als een float
#     """
#
#     return registerCount, "%" + str(registerCount) + " = sitofp i32 %" + str(register) + " to float\n"

def getSymbolFromTable(node):

    searchNode = node

    symbolValue = None
    name = None
    if node.token == "IDENTIFIER":
        while symbolValue is None:

            while searchNode.symbolTablePointer is None:
                searchNode = searchNode.parent

            table = searchNode.symbolTablePointer.dict

            for key in table:
                if str(key) == str(node.value):
                    symbolValue = table[key]
                    name = str(key)
                    break

            if symbolValue is None:
                searchNode = searchNode.parent

    return symbolValue, name
