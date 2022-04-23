from AST import *

types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1")}

comparisons = {"==": "eq", "!=": "ne", ">": "sgt", "<": "slt", ">=": "sge", "<=": "sle"}
logicals = {"||": "OR", "&&": "AND", "!": "NOT"}


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


        #Nodig bij load
        self.fromRegister = None
        self.align = None

        #Nodig bij icmp
        self.comparison = None
        self.value1 = None
        self.value2 = None
        self.branch = None

        #nodig bij logical
        self.operation = None


    def getLine(self):
        if self.instruction == "load":
            return self.load()
        elif self.instruction == "icmp":
            return self.icmp()

    def load(self):
        return "  %" + str(self.toRegister) + " = load " + self.type + ", " + self.type + "* %" + str(self.fromRegister) + ", " + self.align + "\n"

    def icmp(self):
        return "  %" + str(self.toRegister) + " = icmp " + self.comparison + " " + self.type + " %" + str(self.value1) + ", %" + str(self.value2) + "\n" + self.br()

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

        value = self.registerCount
        # print("Enter: ", node.token, " Value: " , value)
        self.EnterExitstatements(node, True, value)
        for i, child in enumerate(node.children):
            #Zie dat deze op het laatste staat
            # if i == len(node.children)-1 and node.value == "FUNC_DEF":
            #     self.returnFunction(node)
            self.generateLLVM(child)

        # print("Exit: ", node.token, " Value: " , value)
        self.EnterExitstatements(node, False, value)


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

    def EnterExitstatements(self, node, enter, value):
        if node.token == "FUNC_DEF":
            if enter:
                self.enterFunction(node)
            else:
                self.exitFunction(node)
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
                self.while_stmt(node)
            else:
                pass
        elif node.token == "=":
            if enter:
                self.enterAssignment(node)
            else:
                self.exitAssignment(node)

    def allocateVariables(self, symbolTable):
        toAllocate = symbolTable.dict
        for key in toAllocate:

            if toAllocate[key].value.parent.children[0].token == "IDENTIFIER":
                type = toAllocate[key].type
                toAllocate[key].register = self.registerCount
                self.line += self.allocate(self.registerCount, type)
                self.registerCount += 1

    def enterFunction(self, node):
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

    def exitFunction(self, node):
        # TODO: Check bij void ook
        returnType = node.parent.children[0].children[0].value
        # Geval return opgegeven
        if node.children[len(node.children) - 1].token == "RETURN":
            # symbolTable = tableLookup(node)

            returnNode = node.children[len(node.children) - 1].children[0]
            returnValue = str(returnNode.value)
            returnToken = returnNode.token
            # TODO: lookup in symbol table
            if returnToken == "IDENTIFIER":
                pass
            else:
                self.line += "  ret " + types[returnType][0] + " " + str(returnValue) + "\n}\n\n"

        # Geval return niet opgegeven
        else:
            if returnType == "INT":
                self.line += "  ret " + "i32" + " 0\n}\n\n"
            elif returnType == "FLOAT":
                self.line += "  ret " + "i32" + " 0\n}\n\n"
            elif returnType == "CHAR":
                pass

    def enterAssignment(self, node):

        symbolTable = tableLookup(node.children[0])
        symbol_lookup = symbolLookup(node.children[0].value, symbolTable)[1]
        if node.children[1].token == "IDENTIFIER":
            symbolTable1 = tableLookup(node.children[1])
            symbol_lookup1 = symbolLookup(node.children[1].value, symbolTable1)[1]
            register1 = symbol_lookup1.register
            register = symbol_lookup.register
            type = symbol_lookup1.type

            self.line += self.load(type, register1)
            self.store(self.registerCount, register, type, True, True)
            self.registerCount += 1

        elif node.children[1].token in types:
            register = symbol_lookup.register
            type = symbol_lookup.type
            value = node.children[1].value
            self.store(value, register, type, False, True)

        # Kans op meerder berekingen die nog uitgevoerd moeten worden
        else:
            # We moeten eerst alle variable loaden die we gebruiken
            registers = []
            self.getRegisters(node.children[1], registers)
            for i, register in enumerate(registers):
                self.line += self.load(register[0].type, register[0].register)
                registers[i] = self.registerCount, *register
                self.registerCount += 1

            self.calculations(node.children[1], registers)


    def exitAssignment(self, node):
        pass

    def enterPrintf(self, node):
        self.isPrintf = True

        # TODO ? load voor de variabelen doen die in de printf gebruikt worden?
        reg = [] # registers waar we de variabelen in hebben geload
        for i, child in enumerate(node.children):
            if (i == 0):
                continue
            else:
                table = tableLookup(node.children[i])  # we look up the name of the function
                symbol_lookup = symbolLookup(node.children[i].value, table)
                if symbol_lookup[0]:
                    self.line += self.load(symbol_lookup[1].type, symbol_lookup[1].register)
                    reg.append(self.registerCount)
                    self.registerCount += 1

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
                            self.line += "i32* %" + str(reg[i-1])
                        elif symbol_lookup[1].type == "FLOAT":
                            self.line += "double* %" + str(reg[i-1])
                        elif symbol_lookup[1].type == "CHAR":
                            number = ord(str(node.children[i].children[0].value)[1])
                            self.line += "i32* %" + str(reg[i-1])
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

                    else: # bij een niet-identifier

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
                        if symbol_lookup[1].type == "INT":
                            self.line += "i32* %" + str(symbol_lookup[1].register)
                        elif symbol_lookup[1].type == "FLOAT":
                            self.line += "double* %" + str(symbol_lookup[1].register)
                        elif symbol_lookup[1].type == "CHAR":
                            number = ord(str(node.children[i].children[0].value)[1])
                            self.line += "i32* %" + str(symbol_lookup[1].register)
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

        self.registerCount += 1

    def exitScanf(self, node):
        pass

    def enterIf_stmt(self, node, value):
        self.ifCount += 1
        self.ifRegisters["if"+str(self.ifCount)] = value
        conditionNode  = node.parent.children[0]
        # self.analyseCondition(conditionNode)
        startNode = NodeCon()
        startNode.isRoot = True
        self.nodeCount = 0
        self.generateConditionTree(conditionNode, startNode)
        self.analyseCondition(startNode)
        self.fillIf(startNode)
        self.writeIf(startNode)

    def exitIf_stmt(self, node, value):
        for key in self.ifRegisters:
            if self.ifRegisters[key] == value:
                self.line = self.line.replace(key, str(self.registerCount))
        #Geval geen else
        if node == node.parent.children[len(node.parent.children)-1]:
            self.line += "  br label %" + str(self.registerCount) + "\n\n" + str(self.registerCount) + ":\n"

        else:
            self.line += "  br label %" + "else" + str(value) + "\n\n" + str(self.registerCount) + ":\n"
            self.ifValues.append(value)
        self.registerCount += 1

    def enterElse_stmt(self):
        pass

    def exitElse_stmt(self):
        self.line = self.line.replace("else"+str(self.ifValues[-1]), str(self.registerCount))
        self.ifValues.pop()
        self.line += "  br label %" + str(self.registerCount) + "\n\n" + str(self.registerCount) + ":\n"
        self.registerCount += 1

    def enterBIN_OP1(self, node):
        print("")

    def exitBIN_OP1(self, node):
        pass

    def writeIf(self, node):

        for child in node.children:
            self.writeIf(child)

        if node.instruction == "load" or node.instruction == "icmp":
            self.line += node.getLine()

    def fillIf(self, startNode):
        for child in startNode.children:
            self.fillIf(child)

        startNode.setEndRegister("if"+str(self.ifCount))

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

            elif str(child.token) == "IDENTIFIER":
                nNode = NodeCon()
                nNode.instruction = "load"
                symbolTable = tableLookup(child)
                symbol_lookup = symbolLookup(child.value, symbolTable)
                symbol = symbol_lookup[1]
                nNode.type, nNode.align = types[symbol.type]
                nNode.fromRegister = symbol.register
                nNode.parent = newNode
                nNode.nodeNumber = self.nodeCount
                self.nodeCount += 1
                newNode.children.append(nNode)

            self.generateConditionTree(child, nNode)

    def analyseCondition(self, node):

        for child in node.children:
            self.analyseCondition(child)

        # print(node.instruction)

        if node.instruction == "load":
            node.toRegister = self.registerCount
            self.registerCount += 1

        elif node.instruction == "icmp":
            node.toRegister = self.registerCount
            node.value1 = node.children[0].toRegister
            node.value2 = node.children[1].toRegister
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
                    self.registerCount += 1

                elif node == node.parent.children[1] and node.parent.parent is not None:
                    # We controleren nog voor de zekerheid dat we de linker van parent zijn
                    if node.parent == node.parent.parent.children[0] and len(node.parent.parent.children) == 2:
                        #We moeten ook nog kijken wat de parent hier van is want or of and heeft hier ook invloed
                        if node.parent.parent.operation == "AND":
                            node.branch.label1 = self.registerCount
                            self.registerCount += 1
                        elif node.parent.parent.operation == "OR":
                            node.branch.label2 = self.registerCount
                            self.registerCount += 1

            elif node.parent.operation == "AND":
                node.branch = Branch()
                node.branch.boolRegister = node.toRegister

                # Als de node de links van de operation is gaan we eerst naar de rechterkant gaan als het juist is
                # Als de node de rechts is van de operation gaan we naar de logical zijn parent zien
                # En deze bepaalt dan wat er moet gebeuren

                if node == node.parent.children[0]:
                    node.branch.label1 = self.registerCount
                    self.registerCount += 1

                elif node == node.parent.children[1] and node.parent.parent is not None:
                    # We controleren nog voor de zekerheid dat we de linker van parent zijn
                    if node.parent == node.parent.parent.children[0] and len(node.parent.parent.children) == 2:
                        #We moeten ook nog kijken wat de parent hier van is want or of and heeft hier ook invloed
                        if node.parent.parent.operation == "AND":
                            node.branch.label1 = self.registerCount
                            self.registerCount += 1
                        elif node.parent.parent.operation == "OR":
                            node.branch.label2 = self.registerCount
                            self.registerCount += 1

            if len(node.children) == 2:
                if self.nodeCount-1 == node.children[1].nodeNumber:
                    #betekent dat we in de laatste node zitten dus de laatste branch ook voor de if statemtn
                    node.branch.label1 = self.registerCount
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

    def load(self, type, register):

        return "  %" + str(self.registerCount) + " = load " + types[type][0] + ", " + types[type][0] + "* " \
                                                                                                               "%" + str(register) + ", " + types[type][1] + "\n"

    def store(self, fromRegister, toRegister, type, isReg1, isReg2):

        reg1 = "%" + str(fromRegister) if isReg1 else str(fromRegister)
        reg2 = "%" + str(toRegister) if isReg2 else str(toRegister)

        self.line += "  store " + types[type][0] + " " + reg1 + ", " + types[type][0] + "* " + reg2 + "" \
            ", " + types[type][1] + "\n"

    def allocate(self, register, type):
        return "  %" + str(register) + " = alloca " + types[type][0] + ", " + types[type][1] + "\n"

    def getRegisters(self, node, registers):
        for child in node.children:
            self.getRegisters(child, registers)

        if node.token == "IDENTIFIER":
            symbolTable = tableLookup(node)
            lookup_symbol = symbolLookup(node.value, symbolTable)[1]
            registers.append((lookup_symbol, str(node.value)))

    def calculations(self, node, registers):

        for child in node.children:
            self.calculations(child, registers)

        if str(node.value) == "+":
            self.addition(node.children[0], node.children[1], registers)
        elif str(node.value) == "-":
            self.addition(node.children[0], node.children[1], registers)
        elif str(node.value) == "*":
            self.addition(node.children[0], node.children[1], registers)
        elif str(node.value) == "/":
            self.addition(node.children[0], node.children[1], registers)
        elif str(node.value) == "%":
            self.addition(node.children[0], node.children[1], registers)

    def getValuesForCalc(self, node):
        type = None
        isRegister = None
        value = None
        if node.token == "IDENTIFIER":
            symbolTable = tableLookup(node)
            lookup_symbol = symbolLookup(node.value, symbolTable)[1]
            type = lookup_symbol.type
            isRegister = True
            value = str(node.value)

        elif node.token in types:
            type = node.token
            isRegister = False
            value = node.value
        
        return value, type, isRegister
        
    def addition(self, leftChild, rightChild, registers):

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

                self.line += "  %" + str(self.registerCount) + " = fadd float " + "%" if leftReg else "" + str(left) + ", " + "%" if rightReg else ""
                self.line += str(right) + "\n"

            elif rightType == "INT":
                # Check of het een register is of niet.
                if not rightReg:
                    right = str(left) + ".0e+00"
                else:
                    self.line += "  %" + str(self.registerCount) + " = sitofp i32 %" + str(right) + " to float\n"
                    right = str(self.registerCount)
                    self.registerCount += 1

                self.line += "  %" + str(self.registerCount) + " = fadd float " + "%" if leftReg else "" + str(left) + ", " + "%" if rightReg else ""
                self.line += str(right) + "\n"

            else:
                #Allebei float
                self.line += "  %" + str(self.registerCount) + " = fadd float " + "%" if leftReg else "" + str(left) + ", " + "%" if rightReg else ""
                self.line += str(right) + "\n"

        elif type == "INT":
            self.line += "  %" + str(self.registerCount) + " = add i32 " + "%" if leftReg else "" + str(left) + ", " + "%" if rightReg else ""
            self.line += str(right) + "\n"

        self.registerCount += 1
        return self.registerCount-1


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
