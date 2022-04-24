from AST import *

types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1")}

comparisons = {"==": "eq", "!=": "ne", ">": "sgt", "<": "slt", ">=": "sge", "<=": "sle"}
logicals = {"||": "OR", "&&": "AND", "!": "NOT"}
calculations_ = {"+": "add", "-": "sub", "*": "mul", "/": "div", "%": "srem"}

class Branch:

    def __init__(self):
        self.boolRegister = None
        self.label1 = None
        self.label2 = None
        self.instruction = "br"


class NodeCon:

    def __init__(self):
        self.isRoot = False
        self.parent = None
        self.children = []
        self.nodeNumber = 0

        #info node
        self.toRegister = None
        self.type = None
        self.instruction = None
        self.value = None

        #Nodig bij load
        self.fromRegister = None
        self.align = None

        #Nodig bij icmp
        self.comparison = None
        self.value1 = None
        self.value2 = None
        self.branch = None
        self.iden1 = True
        self.iden2 = True

        #Nodig bij operations
        self.calculation = None
        self.type = None
        self.val1 = None
        self.val2 = None
        self.isReg1 = None
        self.isReg2 = None
        self.type1 = None
        self.type2 = None

        #nodig bij logical
        self.operation = None


    def getLine(self):
        if self.instruction == "load":
            return self.load()
        elif self.instruction == "icmp":
            return self.icmp()
        elif self.instruction == "operation":
            return self.operate()
        elif self.instruction == "functioncall":
            return self.function()

    def load(self):
        return "  %" + str(self.toRegister) + " = load " + self.type + ", " + self.type + "* %" + str(self.fromRegister) + ", " + self.align + "\n"

    def icmp(self):
        val1 = str(self.value1)
        val2 = str(self.value2)
        if self.iden1:
            val1 = "%" + val1
        if self.iden2:
            val2 = "%" + val2

        if self.type in types:
            self.type = types[self.type][0]

        return "  %" + str(self.toRegister) + " = icmp " + self.comparison + " " + self.type + " " + val1 + ", " + val2 + "\n" + self.br()

    def operate(self):
        val1 = str(self.val1)
        val2 = str(self.val2)
        ope = str(self.calculation)
        if self.isReg1:
            val1 = "%" + str(self.children[0].toRegister)
        if self.isReg2:
            val2 = "%" + str(self.children[1].toRegister)
        if self.type == "FLOAT":
            ope = "f" + ope

        nsw = " nsw "
        if ope == "srem":
            nsw = " "

        return "  %" + str(self.toRegister) + " = " + ope + nsw + types[self.type][0] + " " + val1 + ", " + val2 + "\n"

    def function(self):
        registers = []
        self.getChildrenReg(registers, self.children)
        line = "  %" + str(self.toRegister) + " = " + "call " + types[self.type][0] + " @" + self.value + "("
        for i, param in enumerate(registers):
            if i < len(registers) -1:
                line += ", "

            type = param[1]
            if param[1] in types:
                type = types[param[1]][0]

            line += type + " %" + str(param[0])

        line += ")\n"
        return line

    def getChildrenReg(self, registers, children):
        for child in children:
            if child.toRegister is not None:
                registers.append((child.toRegister, child.type))

    def br(self):
        return "  br i1 %" + str(self.branch.boolRegister) + ", label %" + str(self.branch.label1) + ", label %" + str(self.branch.label2) + "\n\n" + str(self.branch.boolRegister + 1) + ":\n"

    def setEndRegister(self, number):
        if self.branch is not None:
            if self.branch.label1 is None:
                self.branch.label1 = number

            elif self.branch.label2 is None:
                self.branch.label2 = number

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
        self.nodeCount = 0
        #Vult op het einde van programma alle registers in van de if statements
        self.ifRegisters = {}
        self.ifCount = 0
        self.ifValues = []
        self.whileStack = []
        self.justBreaked = False
        self.ifElseBreaked = [False, False]
        self.returnRegister = None
        self.functionLabel = None

    def toLLVM(self, inputfile):

        afterSlash = re.search("[^/]+$", inputfile)
        pos = afterSlash.start()
        inputfile = inputfile[pos:]
        filename = str(inputfile[:len(inputfile) - 2]) + ".ll"
        self.file = open("llvm_files/" + filename, "w")

        if self.tree.root is None:
            return

        self.allocateVariables(self.tree.root.symbolTablePointer, True)
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

        value = self.registerCount
        # print("Enter: ", node.token, " Value: " , value)

        self.EnterExitstatements(node, True, value)
        if self.registerCount == 22:
            print(self.registerCount)
        for i, child in enumerate(node.children):
            #Zie dat deze op het laatste staat
            # if i == len(node.children)-1 and node.value == "FUNC_DEF":
            #     self.returnFunction(node)
            self.generateLLVM(child)

        # print("Exit: ", node.token, " Value: " , value)
        self.EnterExitstatements(node, False, value)

    def EnterExitstatements(self, node, enter, value):
        if node.parent is not None:
            if node.parent.token == "ROOT" and node.token == "=":
                return

        if self.ifElseBreaked == [True, True] and node.token != "WHILE":
            return

        if node.token == "FUNC_DEF":
            if enter:
                self.enterFunction(node)
            else:
                self.exitFunction(node)
                self.registerCount = 1
        elif node.token == "RETURN":
            if enter:
                self.exitFunction(node)
            else:    # def addition(self, value, var, register, float=False):
                pass
        elif node.token == "PRINTF":
            if enter:
                self.enterPrintf(node)
            else:
                pass
        elif node.token == "SCANF":
            if enter:
                self.enterScanf(node)
            else:
                pass
        elif node.token == "IF":
            if enter:
                self.enterIf_stmt(node, value)
            else:
                self.exitIf_stmt(node, value)
        elif node.token == "ELSE":
            if enter:
                self.enterElse_stmt()
            else:
                self.exitElse_stmt()
        elif node.token == "WHILE":
            if enter:
                self.enterWhile_stmt(node, value)
            else:
                self.exitWhile_stmt(node, value)
        elif node.token == "=":
            if enter:
                self.enterAssignment(node)
            else:
                self.exitAssignment(node)
        elif node.token == "UN_OP":
            if enter:
                self.enterUnaryOperation(node)
            else:
                self.exitUnaryOperation(node)
        elif node.token == "BREAK":
            if enter:
                self.enterBreak(node)
            else:
                self.exitBreak(node)
        elif node.token == "CONTINUE":
            if enter:
                self.enterContinue(node)
            else:
                self.exitContinue(node)

        elif node.token == "FUNC_CALL":
            if enter:
                self.enterFuncCall(node)
            else:
                self.exitFuncCall(node)

    def allocateVariables(self, symbolTable, isGlobal=False):
        toAllocate = symbolTable.dict
        params = []
        for key in toAllocate:

            type = toAllocate[key].type

            if type == '':
                type = toAllocate[key].value.type if toAllocate[key].value.type != '' else toAllocate[key].value.token

            if toAllocate[key].value.parent.children[0].token == "IDENTIFIER" or toAllocate[key].value.token == "IDENTIFIER":
                if isGlobal:
                    toAllocate[key].register = key
                    toAllocate[key].isAssigned = True
                    toAllocate[key].isGlobal = True
                    self.file.write(self.allocate(key, type, isGlobal, toAllocate[key].value.value))

                else:
                    tempReg = toAllocate[key].register
                    toAllocate[key].register = self.registerCount
                    self.line += self.allocate(self.registerCount, type, isGlobal)
                    self.registerCount += 1
                    if toAllocate[key].isParam:
                        params.append((tempReg, toAllocate[key].register, toAllocate[key].type))

        for param in params:
            self.store(param[0], param[1], param[2], True, True)

    def enterFunction(self, node):
        table, name = getSymbolFromTable(node.parent.children[1].children[0])
        symbolTable = tableLookup(node)
        symbol_lookup = symbolLookup(node.value, symbolTable)
        self.functionLabel = False
        return_type = table.type
        parameters = table.functionParameters


        # if len(parameters) == 0:
        #     self.line += "\ndefine dso_local " + types[return_type][0] + " @" + name + "() {\n"
        #
        # else:
        type = None
        if return_type is None:
            type = "void"
        else:
            type = types[return_type][0]

        self.line += "\ndefine dso_local " + type + " @" + name + "("
        if len(parameters) > 0:
            if len(parameters) == 1 and parameters[0] == "NONE":
                self.registerCount = 1
            else:
                self.registerCount = 0
        for i, param in enumerate(parameters):
            if param != 'NONE':
                symbol_lookup = symbolLookup(param, symbolTable)[1]
                symbol_lookup.register = self.registerCount
                symbol_lookup.isParam = True
                self.line += types[symbol_lookup.type][0] + " %" + str(self.registerCount)
                if i < len(parameters) - 1:
                    self.line += ", "

                self.registerCount += 1

        if len(parameters) > 0 and parameters[0] != 'NONE':
            self.registerCount += 1

        self.line += ") {\n"

        #Alloceer een register voor deze return
        if return_type != None:
            self.line += self.allocate(self.registerCount, return_type)
            #TODO: controleer dit nog later
            self.store(0, self.registerCount, return_type, False, True)
            self.returnRegister = self.registerCount, return_type
            self.registerCount += 1

        self.allocateVariables(symbolTable)

    def exitFunction(self, node):

        if len(node.children) > 0:
            if node.children[len(node.children) - 1].token == "RETURN":
                return

        # TODO: Check bij void ook
        returnType = None
        if node.parent is not None:
            parent = node
            while parent.token != "FUNC_DEF":
                parent = parent.parent
            returnType = parent.parent.children[0].children[0].value
        else:
            returnType = node.parent.parent.children[0].children[0].value

        # Geval return opgegeven
        if node.token == "RETURN":
            # symbolTable = tableLookup(node)
            returnNode = None
            returnValue =None
            returnToken =None
            if returnType is None:
                returnType = "void"
                returnValue = ""
            else:
                returnType = types[str(returnType)][0]
                returnNode = node.parent.children[len(node.parent.children) - 1].children[0]
                returnValue = str(returnNode.value)
                returnToken = returnNode.token

            # TODO: lookup in symbol table
            if returnToken == "IDENTIFIER":
                table = tableLookup(returnNode)
                symbolT = symbolLookup(returnValue, table)
                register = symbolT[1].register
                type = symbolT[1].type
                self.line += self.load(type, register)
                self.store(self.registerCount, self.returnRegister[0],type, True, True)
                self.registerCount += 1
                self.functionLabel = True
                # self.line += "  br label %function"

            elif returnToken is not None and returnValue.isdigit() is False:
                conditionNode = node.parent.children[0]
                startNode = NodeCon()
                startNode.isRoot = True
                self.nodeCount = 0
                self.generateConditionTree(conditionNode, startNode)
                self.clearEmpty(startNode)
                self.analyseCondition(startNode)
                self.fillIf(startNode, "function")
                self.writeIf(startNode)


            else:
                self.line += "  ret " + returnType + " " + str(returnValue) + "\n}\n\n"

        elif self.functionLabel:

            self.line += self.load(self.returnRegister[1], self.returnRegister[0])
            self.line += "  ret " + types[self.returnRegister[1]][0] + " " + str(self.registerCount) + "\n}\n"
            self.registerCount += 1
            self.functionLabel = False

        # Geval return niet opgegeven
        else:
            if returnType == "INT":
                self.line += "  ret " + "i32" + " 0\n}\n\n"
            elif returnType == "FLOAT":
                self.line += "  ret " + "i32" + " 0\n}\n\n"
            elif returnType == "CHAR":
                pass
            elif returnType is None:
                self.line += "  ret " + "void\n}\n\n"

    def enterAssignment(self, node):

        symbolTable = tableLookup(node.children[0])
        symbol_lookup = symbolLookup(node.children[0].value, symbolTable)[1]
        symbol_lookup.isAssigned = True
        if node.children[1].token == "IDENTIFIER":
            symbolTable1 = tableLookup(node.children[1])
            symbol_lookup1 = symbolLookup(node.children[1].value, symbolTable1)[1]
            register1 = symbol_lookup1.register
            register = symbol_lookup.register
            type = symbol_lookup1.value.token

            self.line += self.load(type, register1)
            self.store(self.registerCount, register, type, True, True)
            self.registerCount += 1

        elif node.children[1].token in types:
            #Speciaal geval voor die for loop
            if symbol_lookup.register == 0:
                self.allocateVariables(symbolTable)
            register = symbol_lookup.register
            type = node.children[1].token
            value = node.children[1].value
            self.store(value, register, type, False, True)

        # Kans op meerder berekingen die nog uitgevoerd moeten worden
        else:
            # We moeten eerst alle variable laden die we gebruiken
            registers = []
            self.getRegisters(node.children[1], registers)
            for i, register in enumerate(registers):
                self.line += self.load(register[0].type, register[0].register)
                registers[i] = self.registerCount, *register
                self.registerCount += 1

            returnReg = self.calculations(node.children[1], registers)
            type = symbol_lookup.type
            if type == '':
                type = symbol_lookup.value.type if symbol_lookup.value.type != '' else symbol_lookup.value.token
            self.store(returnReg[0], symbol_lookup.register, type, True, True)

    def exitAssignment(self, node):
        pass

    def enterPrintf(self, node):
        self.isPrintf = True

        reg = [] # registers waar we de variabelen in hebben geload
        for i, child in enumerate(node.children):
            if (i == 0):
                continue
            else:
                table = tableLookup(node.children[i])  # we look up the name of the function
                symbol_lookup = symbolLookup(node.children[i].value, table)

                if symbol_lookup[0]:
                    parent = node
                    val = node.children[i].value
                    while symbol_lookup[1].isAssigned is False:
                        while parent.symbolTablePointer is None:
                            parent = parent.parent

                        table = tableLookup(parent)  # we look up the name of the function
                        symbol_lookup = symbolLookup(val, table)
                        parent = parent.parent

                    type = symbol_lookup[1].type
                    if type == '':
                        type = symbol_lookup.value.type if symbol_lookup.value.type != '' else symbol_lookup.value.token
                    self.line += self.load(type, symbol_lookup[1].register, symbol_lookup[1].isGlobal)
                    reg.append(self.registerCount)
                    self.registerCount += 1
                else:
                    reg.append(None)

        text = node.children[0].value
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

        for i, child in enumerate(node.children):
            if (i == 0):
                continue
            else:
                table = tableLookup(node.children[i])  # we look up the name of the function
                symbol_lookup = symbolLookup(node.children[i].value, table)
                if symbol_lookup[0]:  # bij een identifier
                    if symbol_lookup[1].type == "FLOAT":
                        reg[i - 1] = self.floatToDouble(reg[i - 1])
                    elif symbol_lookup[1].type == "CHAR":
                        reg[i - 1] = self.charToInt(reg[i - 1])

        callRegister = []

        for j, child in enumerate(node.children):
            if child.token == "FUNC_CALL":

                # print("")

                startNode = NodeCon()
                startNode.isRoot = True
                self.nodeCount = 0
                self.generateConditionTree(node, startNode)
                self.clearEmpty(startNode)
                self.analyseCondition(startNode)
                self.fillIf(startNode, "function")
                self.writeIf(startNode)
                i = len(child.children[1].children)
                for chl in child.children[1].children:
                    name = str(chl.value)
                    tableF = tableLookup(chl)
                    sTable = symbolLookup(name, tableF)[1]
                    Rtype = sTable.type
                    callRegister.append([self.registerCount - i, Rtype])
                    i -= 1


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

                    table = tableLookup(node.children[i])  # we look up the name of the function
                    symbol_lookup = symbolLookup(node.children[i].value, table)
                    if symbol_lookup[0]: # bij een identifier
                        if symbol_lookup[1].type == "INT":
                            self.line += "i32 %" + str(reg[i-1])
                        elif symbol_lookup[1].type == "FLOAT":
                            self.line += "double %" + str(reg[i - 1])
                        elif symbol_lookup[1].type == "CHAR":
                            self.line += "i32 %" + str(reg[i - 1])

                        elif symbol_lookup[1].type == "STRING":  # TODO type kan wel ni kloppen, want hebben wij een string
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

                    elif child.token == "FUNC_CALL":
                        for j, reg in enumerate(callRegister):
                            if j < len(callRegister) -1 and j != 0:
                                self.line += ", "

                            self.line += types[reg[1]][0] + " %" + str(reg[0])


                    else: # bij een niet-identifier

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

    def exitPrintf(self, node):
        pass

    def enterScanf(self, node):

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

        extraLines = ""
        strings = []
        stringcount = 0
        for param in params:
            numbers = param[1:len(param)-1]
            if numbers.isdigit():
                number = int(numbers)
                strings.append(number)
            elif param[-1] == 's':
                strings.append(None)

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
                    if node.children[i].token == "UN_OP": # als we bij de argumenten (rechts) een ampersand hebben (reference), wat hoogstwaarschijnlijk gaat gebeuren
                        table = tableLookup(node.children[i].children[0])  # we look up the name of the function
                        symbol_lookup = symbolLookup(node.children[i].children[0].value, table)
                        # if node.children[i].children[0].token == "INT":
                        #     self.line += "i32 " + str(node.children[i].children[0].value)
                        symbol_lookup[1].isAssigned = True
                        if symbol_lookup[1].type == "INT":
                            self.line += "i32* %" + str(symbol_lookup[1].register)
                        elif symbol_lookup[1].type == "FLOAT":
                            self.line += "double* %" + str(symbol_lookup[1].register)
                        elif symbol_lookup[1].type == "CHAR":

                            number_ = strings[stringcount]
                            if number_ is None:
                                self.line += "i8* %" + str(symbol_lookup[1].register)

                            else:
                                bound = "["+ str(number_) + " x i8]"
                                self.line += bound + "* %" + str(symbol_lookup[1].register)
                                self.registerCount += 1
                                extraLines += "  %" + str(self.registerCount) + " = getelementptr inbounds " + bound + ", " + bound + "* %" + str(symbol_lookup[1].register) + ", i64 0, i64 0\n"
                            stringcount += 1

                        elif symbol_lookup[1].type == "STRING": # TODO type kan wel ni kloppen, want hebben wij een string
                            text = node.children[i].children[0].value
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
                    else: # geval waar er geen ampersand staat
                        pass


            self.line += ")\n"

        self.line += extraLines

        self.registerCount += 1

    def exitScanf(self, node):
        pass

    def enterIf_stmt(self, node, value):
        self.ifCount += 1
        self.ifRegisters["if"+str(self.ifCount)] = value, None
        conditionNode  = node.parent.children[0]
        # self.analyseCondition(conditionNode)
        startNode = NodeCon()
        startNode.isRoot = True
        self.nodeCount = 0
        self.generateConditionTree(conditionNode, startNode)
        self.clearEmpty(startNode)
        self.analyseCondition(startNode)
        self.fillIf(startNode, "if")
        self.writeIf(startNode)

    def exitIf_stmt(self, node, value):
        for key in self.ifRegisters:
            if self.ifRegisters[key][0] == value:
                self.line = self.line.replace(key, str(self.registerCount))
        #Geval geen else
        if node == node.parent.children[len(node.parent.children)-1] and not self.justBreaked:
            self.line += "  br label %" + str(self.registerCount) + "\n\n" + str(self.registerCount) + ":\n"

        elif not self.justBreaked:
            self.line += "  br label %" + "else" + str(value) + "\n\n" + str(self.registerCount) + ":\n"
            self.ifValues.append(value)
        elif self.justBreaked:
            self.ifElseBreaked[0] = True
            self.justBreaked = False
            self.ifValues.append(value)

        self.registerCount += 1

    def enterElse_stmt(self):
        pass

    def exitElse_stmt(self):
        self.line = self.line.replace("else"+str(self.ifValues[-1]), str(self.registerCount))
        self.ifValues.pop()
        if not self.justBreaked:
            self.line += "  br label %" + str(self.registerCount) + "\n\n" + str(self.registerCount) + ":\n"
            self.registerCount += 1
        elif self.justBreaked:
            self.ifElseBreaked[1] = True
            self.justBreaked = False

    def enterBIN_OP1(self, node):
        pass

    def exitBIN_OP1(self, node):
        pass

    def enterUnaryOperation(self, node):

        if str(node.value) == "++":
            symbolTable = tableLookup(node.children[0])
            lookup_symbol = symbolLookup(node.children[0].value, symbolTable)[1]

            if lookup_symbol is not None:
                parent = node
                val = node.children[0].value
                while lookup_symbol.isAssigned is False:
                    while parent.symbolTablePointer is None:
                        parent = parent.parent

                    table = tableLookup(parent)  # we look up the name of the function
                    lookup_symbol = symbolLookup(val, table)[1]
                    parent = parent.parent

            type = lookup_symbol.type
            if type == '':
                type = lookup_symbol.value.type if lookup_symbol.value.type != '' else lookup_symbol.value.token

            self.line += self.load(type, lookup_symbol.register, lookup_symbol.isGlobal)
            self.registerCount += 1
            retReg = self.operate(1, self.registerCount-1, [], lookup_symbol.type, "add")
            self.store(retReg[0],lookup_symbol.register, type, True, True)

        elif str(node.value) == "--":
            symbolTable = tableLookup(node.children[0])
            lookup_symbol = symbolLookup(node.children[0].value, symbolTable)[1]

            if lookup_symbol is not None:
                parent = node
                val = node.children[0].value
                while lookup_symbol.isAssigned is False:
                    while parent.symbolTablePointer is None:
                        parent = parent.parent

                    table = tableLookup(parent)  # we look up the name of the function
                    lookup_symbol = symbolLookup(val, table)
                    parent = parent.parent

            type = lookup_symbol.type
            if type == '':
                type = lookup_symbol.value.type if lookup_symbol.value.type != '' else lookup_symbol.value.token

            self.line += self.load(type, lookup_symbol.register, lookup_symbol.isGlobal)
            self.registerCount += 1
            retReg = self.operate(1, self.registerCount - 1, [], lookup_symbol.type, "sub")
            self.store(retReg[0], lookup_symbol.register, type, True, True)
            # self.operate()

    def exitUnaryOperation(self, node):
        pass

    def enterWhile_stmt(self, node, value):

        conditionNode = node.parent.children[0]

        if node.parent.children[0].token == "DECLARATION":
            conditionNode = node.parent.children[1]

        self.line += "  br label %" + str(self.registerCount) + "\n\n" + str(self.registerCount) + ":\n"
        self.registerCount += 1

        self.ifCount += 1
        self.ifRegisters["while" + str(self.ifCount)] = value, str(self.registerCount-1)
        self.whileStack.append(("while" + str(self.ifCount), str(self.registerCount-1)))

        # self.analyseCondition(conditionNode)
        startNode = NodeCon()
        startNode.isRoot = True
        self.nodeCount = 0
        self.generateConditionTree(conditionNode, startNode)
        self.clearEmpty(startNode)
        self.analyseCondition(startNode)
        self.fillIf(startNode, "while")
        self.writeIf(startNode)

    def exitWhile_stmt(self, node, value):
        register = None
        for key in self.ifRegisters:
            if self.ifRegisters[key][0] == value:
                self.line = self.line.replace(key, str(self.registerCount))
                register = self.ifRegisters[key][1]
        # Geval geen else
        # if node == node.parent.children[len(node.parent.children) - 1]:
        if self.ifElseBreaked != [True, True]:
            self.line += "  br label %" + register + "\n\n" + str(self.registerCount) + ":\n"
            self.registerCount += 1
        self.whileStack.pop()
        if self.justBreaked:
            self.justBreaked = False
        self.ifElseBreaked = [False, False]

    def enterBreak(self, node):
        if len(self.whileStack) > 0:
            self.line += "  br label %" + self.whileStack[-1][0] + "\n\n" + str(self.registerCount) + ":\n"
            self.justBreaked = True

    def exitBreak(self, node):
        pass

    def enterContinue(self, node):
        if len(self.whileStack) > 0:
            self.line += "  br label %" + self.whileStack[-1][1] + "\n\n" + str(self.registerCount) + ":\n"
            self.justBreaked = True

    def exitContinue(self, node):
        pass

    def enterFuncCall(self, node):

        # name = str(node.children[0].children[0].value)
        # table = tableLookup(node.children[0].children[0])
        # symbol = symbolLookup(name, table)
        # type = symbol[1].type
        # if len(node.children) == 1:
        #     if type is None:
        #         self.line += "  call void @" + name + "()\n"
        # else:
        #     parameters = node.children[1].children
        pass

    def exitFuncCall(self, node):
        pass


    def floatToDouble(self, register):
        self.line += "  %" + str(self.registerCount) + " = fpext float %" + str(register) + " to double\n"
        self.registerCount += 1
        return self.registerCount -1

    def charToInt(self, register):
        self.line += "  %" + str(self.registerCount) + " = sext i8 %" + str(register) + " to i32\n"
        self.registerCount += 1
        return self.registerCount - 1

    def writeIf(self, node):

        for child in node.children:
            self.writeIf(child)

        if node.instruction == "load" or node.instruction == "icmp" or node.instruction == "operation" or node.instruction == "functioncall":
            self.line += node.getLine()

    def fillIf(self, startNode, text):
        for child in startNode.children:
            self.fillIf(child, text)

        startNode.setEndRegister(text+str(self.ifCount))

    def generateConditionTree(self, node, newNode):
        for child in node.children:
            nNode = None

            if str(child.value) in comparisons:
                nNode = NodeCon()
                nNode.instruction = "icmp"
                nNode.comparison = comparisons[str(child.value)]
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            elif str(child.value) in logicals:
                nNode = NodeCon()
                nNode.instruction = "logical"
                nNode.operation = logicals[str(child.value)]
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            elif str(child.token) == "IDENTIFIER" and node.token != "NAME":
                nNode = NodeCon()
                nNode.instruction = "load"
                symbolTable = tableLookup(child)
                symbol_lookup = symbolLookup(child.value, symbolTable)
                symbol = symbol_lookup[1]
                type = symbol.type
                if type == '':
                    type = symbol.value.type if symbol.value.type != '' else symbol.value.token

                nNode.type, nNode.align = types[type]
                nNode.fromRegister = symbol.register
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            elif str(child.token) in types:
                nNode = NodeCon()
                nNode.instruction = "none"
                nNode.type, nNode.align = types[str(child.token)]
                nNode.value = str(child.value)
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            elif str(child.token) == "BIN_OP1" or str(child.token) == "BIN_OP2":
                nNode = NodeCon()
                nNode.instruction = "operation"
                nNode.calculation = calculations_[str(child.value)]
                if child.children[0].token == "IDENTIFIER":
                    table = tableLookup(child.children[0])
                    symTable = symbolLookup(child.children[0].value, table)[1]
                    nNode.val1 = symTable.register
                    nNode.typ1 = symTable.value.type
                    nNode.isReg1 = True
                else:
                    nNode.val1 = child.children[0].value
                    nNode.typ1 = child.children[0].token
                    nNode.isReg1 = False
                if child.children[1].token == "IDENTIFIER":
                    table = tableLookup(child.children[1])
                    symTable = symbolLookup(child.children[1].value, table)[1]
                    nNode.val2 = symTable.register
                    nNode.typ2 = symTable.value.type
                    nNode.isReg2 = True
                else:
                    nNode.val2 = child.children[1].value
                    nNode.typ2 = child.children[1].token
                    nNode.isReg2 = False

                nNode.type = nNode.typ1 if (nNode.typ1 == "INT" and nNode.typ2 == "INT") else "FLOAT"

                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            elif child.token == "FUNC_CALL":
                nNode = NodeCon()
                nNode.instruction = "functioncall"
                table = tableLookup(child.children[0].children[0])
                symTable = symbolLookup(child.children[0].children[0].value, table)[1]
                nNode.type = symTable.type
                nNode.value = str(child.children[0].children[0].value)
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            else:
                nNode = NodeCon()
                nNode.instruction = "empty"
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            self.generateConditionTree(child, nNode)

    def clearEmpty(self, node):
        for child in node.children:
            self.clearEmpty(child)

        if node.instruction == "empty":
            nmr = 0
            for chl in node.parent.children:
                if chl == node:
                    break
                nmr += 1
            if len(node.children) == 1:
                node.parent.children[nmr] = node.children[0]
                node.children[0].parent = node.parent
            # else:
            #     node.parent.children.pop(nmr)

    def analyseCondition(self, node):

        for child in node.children:
            self.analyseCondition(child)

        # print(node.instruction)
        # self.registerCount += 1

        if node.instruction == "load":
            node.toRegister = self.registerCount
            self.registerCount += 1

        elif node.instruction == "icmp":
            node.toRegister = self.registerCount

            if node.children[0].value is None:
                node.value1 = node.children[0].toRegister
            else:
                node.value1 = node.children[0].value
                node.iden1 = False

            if node.children[1].value is None:
                node.value2 = node.children[1].toRegister
            else:
                node.value2 = node.children[1].value
                node.iden2 = False

            node.type = node.children[0].type

            self.registerCount += 1
            # Elke icmp is gevolgd door een br instrutction
            # De labels worden bepaald door de logical er boven

            if node.parent.operation == "OR":
                node.branch = Branch()
                node.branch.boolRegister = node.toRegister

                # Als de node de linker van de operation is gaan we eerst naar de rechterkant gaan als het fout is
                # Als de node de rechter is van de operation gaan we naar de logical zijn parent zien
                # En deze bepaalt dan wat er moet gebeuren

                if node == node.parent.children[0]:
                    node.branch.label2 = self.registerCount
                    # self.registerCount += 1

                elif node == node.parent.children[1] and node.parent.parent is not None:
                    # We controleren nog voor de zekerheid dat we de linker van parent zijn
                    if node.parent == node.parent.parent.children[0] and len(node.parent.parent.children) == 2:
                        #We moeten ook nog kijken wat de parent hier van is want or of and heeft hier ook invloed
                        if node.parent.parent.operation == "AND":
                            node.branch.label1 = self.registerCount
                            # self.registerCount += 1
                        elif node.parent.parent.operation == "OR":
                            node.branch.label2 = self.registerCount
                            # self.registerCount += 1

            elif node.parent.operation == "AND":
                node.branch = Branch()
                node.branch.boolRegister = node.toRegister

                # Als de node de links van de operation is gaan we eerst naar de rechterkant gaan als het juist is
                # Als de node de rechts is van de operation gaan we naar de logical zijn parent zien
                # En deze bepaalt dan wat er moet gebeuren

                if node == node.parent.children[0]:
                    node.branch.label1 = self.registerCount
                    # self.registerCount += 1

                elif node == node.parent.children[1] and node.parent.parent is not None:
                    # We controleren nog voor de zekerheid dat we de linker van parent zijn
                    if node.parent == node.parent.parent.children[0] and len(node.parent.parent.children) == 2:
                        #We moeten ook nog kijken wat de parent hier van is want or of and heeft hier ook invloed
                        if node.parent.parent.operation == "AND":
                            node.branch.label1 = self.registerCount
                            # self.registerCount += 1
                        elif node.parent.parent.operation == "OR":
                            node.branch.label2 = self.registerCount
                            # self.registerCount += 1

            elif node.parent.isRoot:
                node.branch = Branch()
                node.branch.boolRegister = node.toRegister

                # Als de node de links van de operation is gaan we eerst naar de rechterkant gaan als het juist is
                # Als de node de rechts is van de operation gaan we naar de logical zijn parent zien
                # En deze bepaalt dan wat er moet gebeuren

                if node == node.parent.children[0]:
                    node.branch.label1 = self.registerCount
                    # self.registerCount += 1

            if len(node.children) == 2:
                if self.nodeCount-1 == node.children[1].nodeNumber:
                    #betekent dat we in de laatste node zitten dus de laatste branch ook voor de if statemtn
                    node.branch.label1 = self.registerCount
                    # self.registerCount += 1

            self.registerCount += 1

        elif node.instruction == "operation":
            if node.children[0].toRegister is not None and node.children[1].toRegister is not None:
                node.val1 = node.children[0].toRegister
                node.typ1 = node.children[0].type
                node.val2  = node.children[1].toRegister
                node.typ2 = node.children[1].type
                node.isReg1 = True
                node.isReg2 = True
                node.type = node.typ1 if node.typ1 == node.typ2 else "FLOAT"
            node.toRegister = self.registerCount

            self.registerCount += 1

        elif node.instruction == "functioncall":
            node.toRegister = self.registerCount
            node.fromRegister = self.registerCount - 1
            self.registerCount += 1

    def while_stmt(self, node):
        pass

    def printfFunction(self):
        return "declare dso_local i32 @printf(i8*, ...)\n"

    def scanfFunction(self):
        return "declare dso_local i32 @__isoc99_scanf(i8*, ...)\n"

    def printStrings(self, number, text, inboud):
        return number + " = private unnamed_addr constant " + inboud + " c\"" + text + "\", align 1\n"

    def scanStrings(self, number, text, inboud):
        return number + " = private unnamed_addr constant " + inboud + " c\"" + text + "\", align 1\n"

    def load(self, type, register, isGlobal=False):

        if isGlobal:
            return "  %" + str(self.registerCount) + " = load " + types[type][0] + ", " + types[type][0] + "* " \
                   "@" + str(register) + ", " + types[type][1] + "\n"
        else:
            return "  %" + str(self.registerCount) + " = load " + types[type][0] + ", " + types[type][0] + "* " \
                   "%" + str(register) + ", " + types[type][1] + "\n"

    def store(self, fromRegister, toRegister, type, isReg1, isReg2):

        reg1 = "%" + str(fromRegister) if isReg1 else str(fromRegister)
        reg2 = "%" + str(toRegister) if isReg2 else str(toRegister)

        if type == "CHAR" and not isReg1:
            reg1 = str(ord(str(reg1[1])))

        if type == "FLOAT":
            if not isReg1:
                reg1 = str(reg1)+"e+00"
            if not isReg2:
                reg2 = str(reg2)+"e+00"

        self.line += "  store " + types[type][0] + " " + reg1 + ", " + types[type][0] + "* " + reg2 + "" \
            ", " + types[type][1] + "\n"

    def allocate(self, register, type, isGlobal=False, value=None):
        if isGlobal:

            if type == 'CHAR':
                value = ord(str(value[1]))

            return "@" + str(register) + " = dso_local global  " + types[type][0] + " " + str(value) + " , " + types[type][1] + "\n"
        else:
            return "  %" + str(register) + " = alloca " + types[type][0] + ", " + types[type][1] + "\n"

    def getRegisters(self, node, registers):
        for child in node.children:
            self.getRegisters(child, registers)

        if node.token == "IDENTIFIER":
            symbolTable = tableLookup(node)
            lookup_symbol = symbolLookup(node.value, symbolTable)[1]
            registers.append((lookup_symbol, str(node.value)))

    def calculations(self, node, registers, returnReg=None):

        for child in node.children:
            returnReg = self.calculations(child, registers, returnReg)

        if str(node.value) == "+":
            returnReg = self.operate(node.children[0], node.children[1], registers, returnReg, "add")
        elif str(node.value) == "-":
            returnReg = self.operate(node.children[0], node.children[1], registers, returnReg, "sub")
        elif str(node.value) == "*":
            returnReg = self.operate(node.children[0], node.children[1], registers, returnReg, "mul")
        elif str(node.value) == "/":
            returnReg = self.operate(node.children[0], node.children[1], registers, returnReg, "div")
        elif str(node.value) == "%":
            returnReg = self.operate(node.children[0], node.children[1], registers, returnReg, "srem")

        return returnReg

    def getValuesForCalc(self, node):
        type = None
        isRegister = None
        value = None
        if node.token == "IDENTIFIER":
            symbolTable = tableLookup(node)
            lookup_symbol = symbolLookup(node.value, symbolTable)[1]
            type = lookup_symbol.value.token
            isRegister = True
            value = str(node.value)

        elif node.token in types:
            type = node.token
            isRegister = False
            value = node.value
        
        return value, type, isRegister
        
    def operate(self, leftChild, rightChild, registers, returnReg, operation):

        left, leftType, leftReg, right, rightType, rightReg = None, None, None, None, None, None,

        if isinstance(leftChild, int):
            left = leftChild
            leftType = "INT"
            right = rightChild
            rightType = returnReg
            rightReg = True

        else:
            left, leftType, leftReg = self.getValuesForCalc(leftChild)
            right, rightType, rightReg = self.getValuesForCalc(rightChild)
        type = "INT"
        if leftType == "FLOAT" or rightType == "FLOAT":
            type = "FLOAT"

        for register in registers:
            if register[2] == str(left):
                left = str(register[0])
            elif register[2] == str(right):
                right = str(register[0])

        if left is None:
            left = str(returnReg[0])
            leftType = str(returnReg[1])
            leftReg = True

        elif right is None:
            right = str(returnReg[0])
            rightType = str(returnReg[1])
            rightReg = True

        if type == "FLOAT":
            #Moest 1 van de 2 types een int zijn moeten we deze eerst nog omzetten naar een float
            if leftType == "INT":
                #Check of het een register is of niet.
                if not leftReg:
                    left = str(left) + ".0e+00"
                else:
                    self.line += "  %" + str(self.registerCount) + " = sitofp i32 %" + str(left) + " to float\n"
                    left = str(self.registerCount)
                    self.registerCount += 1

                self.line += "  %" + str(self.registerCount) + " = f" + operation + " float "
                self.line += "%" if leftReg else ""
                self.line += str(left) + ", "
                self.line += "%" if rightReg else ""
                self.line += str(right) + "\n"

            elif rightType == "INT":
                # Check of het een register is of niet.
                if not rightReg:
                    right = str(left) + ".0e+00"
                else:
                    self.line += "  %" + str(self.registerCount) + " = sitofp i32 %" + str(right) + " to float\n"
                    right = str(self.registerCount)
                    self.registerCount += 1

                self.line += "  %" + str(self.registerCount) + " = f" + operation + " float "
                self.line += "%" if leftReg else ""
                self.line += str(left) + ", "
                self.line += "%" if rightReg else ""
                self.line += str(right) + "\n"

            else:
                #Allebei float
                self.line += "  %" + str(self.registerCount) + " = f" + operation + " float "
                self.line += "%" if leftReg else ""
                self.line += str(left) + ", "
                self.line += "%" if rightReg else ""
                self.line += str(right) + "\n"

        elif type == "INT":
            if operation == "div":
                operation = "sdiv"

            self.line += "  %" + str(self.registerCount) + " = " + operation + " i32 "
            self.line += "%" if leftReg else ""
            self.line += str(left) + ", "
            self.line += "%" if rightReg else ""
            self.line += str(right) + "\n"

        self.registerCount += 1
        return self.registerCount-1, type


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
