from AST import *

# types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1"), None: ("void", "")}
calculations_ = {"+": "add", "-": "sub", "*": "mul", "/": "div", "%": "mfhi"}
logicals = {"||": "OR", "&&": "AND", "!": "NOT"}

global_types = {"INT": "word", "FLOAT": "float", "CHAR": "asciiz", None: ("void", "")}
syscalls = {"print_int": [1, "$a0", None],
            "print_float": [2, "$f12", None],
            "print_string": [4, "$a0", None],
            "read_int": [5, None, "$v0"],
            "read_float": [6, None, "$f0"],
            "read_string": [8, ("$a0", "$a1"), None],
            "exit": [10, None, None], }  # list(Code, Args, Result)
data_comp_instr = {"==": "seq", "!=": "sne", ">=": "sge", ">": "sgt", "<=": "sle", "<": "slt"}
data_comp_instr_f = {"==": "c.eq.s", "!=": "c.ne.s", ">=": "c.ge.s", ">": "c.gt.s", "<=": "c.le.s", "<": "c.lt.s"}
branch_intr_bin = {"uncond": "b", "==": "beq", "<=": "ble", "<": "blt", ">=": "bge", ">": "bgt",
                   "!=": "bne"}  # branch instructions for binary check (2 registers)
branch_intr_un = {"==": "beqz", "<=": "blez", "<": "bltz", ">=": "bgez", ">": "bgtz",
                  "!=": "bnez"}  # branch instructions for unary check (1 register), comparison with 0


class Mips:

    def __init__(self):
        self.line = ""
        self.stackOffset = 0
        self.stringCount = 0
        self.floatCount = 0

        self.assignmentStack = []
        self.functionCallStack = []
        self.returnStack = []
        self.printfStack = []
        self.conditionStack = []
        self.logicalStack = []
        self.ifStack = []
        self.whileStack = []
        self.scanfStack = []

        self.enteredAssignment = False
        self.enteredFunctionCall = 0
        self.enteredReturn = False
        self.enteredPrintf = False
        self.enteredCondition = False
        self.enteredScanf = False

        self.returnType = ""
        self.hasReturnNode = (False, 0)
        self.curPrintf = 0
        self.isComparison = False
        self.wasLogical = False
        self.isBreaked = False

        self.printf = False
        self.scanf = False

        self.floats = []
        self.strings = []
        self.globals = []

        self.logLabelCount = 0
        self.finalRegLog = None
        self.ifLabelCount = 0
        self.whileLabelCount = 0

        self.register = 0
        self.offset = -4

        self.isMain = False

        self.compBranchNr = 0
        self.labelCount = 0
        self.reverseCount = 0
        self.ifElseCount = 0
        self.whileCount = 0

    def enterFunction(self, node):
        print("enterFunction")

        # We enteren een nieuwe functie dus kunnen de registercount terug op 0 zetten
        self.stackOffset = 0

        # We beginnen eerst met de functie naam, return type en parameters op te vragen
        self.returnType = node.parent.children[0].children[0].token
        functionName = str(node.parent.children[1].children[0].value)
        parameters = [(str(child.value), child.type) for child in node.parent.children[2].children]

        if functionName == "main":
            self.isMain = True

        self.line += functionName + ":"

        symboltable = tableLookup(node)

        # We gaan nu over de parameters om deze toe te voegen
        for i, param in enumerate(parameters):
            # Als we een none hebben betekent dat we geen parameters hebben
            if param[0] == "NONE":
                break

            # We voegen de types toe en de registers hiervoor
            # self.line += types[param[1]][0] + " %" + str(i)

            # We vragen het symbool ook op uit de symbol table zodat we het juiste
            # register eraan kunnen toekennen
            # TODO: check lines and columns with function
            symbol_lookup = symbolLookup(param[0], symboltable, afterTotalSetup=True)[1]
            symbol_lookup.register = i
            # Als het een parameter is zetten we dit ook op true
            symbol_lookup.isParam = True
            # We verhogen ook de registercount al
            # self.register += 1
            # if i < len(parameters) - 1:
            #     self.line += ", "

        # sluiten de functie definitie
        self.line += "\n"

        # We verhogen de registercount nog maals 1 keer
        # self.register += 1

        # We gaan eerst nog controleren of we een return node hebben
        # Zoniet en het is geen void dan maken we hier ook nog een register voor vrij

        if len(node.children) == 0 or node.children[-1].token != "RETURN":
            self.hasReturnNode = False

        # We gaan nu alle variable alloceren binnen de scope
        self.stackOffset += 4
        self.allTables(symboltable)
        self.stackOffset += 4

        line = "\tsw\t$fp, -4($sp)\n" + \
               "\taddi\t$fp,$sp,0\n" + \
               "\taddi\t$sp,$sp," + str(-self.stackOffset) + "\n" + \
               "\tsw $ra, " + str(self.stackOffset - 8) + "($sp)\n"

        self.line += line
        self.line += "\n"

    def exitFunction(self, node):
        print("exitFunction")

        if not self.hasReturnNode:
            line = "\n\tlw $ra, " + str(self.stackOffset - 8) + "($sp)\n" + \
                   "\taddi\t$sp,$fp,0\n" + \
                   "\tlw\t$fp, -4($sp)\n"

            if not self.isMain:
                line += "\tjr\t$ra\n\n"
                self.isMain = False

            self.line += line

    def enterReturn(self, node):
        print("enterReturn")

        self.enteredReturn = True
        #
        # # We kunnen een return hebben in een if of else of while of for
        # # Als deze stacks nog niet leeg zijn betekent dat we hier een return aanroepen dus we
        # # voeren geen return uit maar gaan branchen naar de laatste return, dit wordt automatisch gedaan
        # if len(self.ifStack) > 0 or len(self.whileStack) > 0:
        #     return
        #
        # if self.returnType is None:
        #     self.line += "  ret void"
        #     self.enteredReturn = False
        #
        # # Als we een return hebben met 1 child (enkel identifier of value) kunnen we dit al direct doen
        # # Wanneer dit niet het geval is zullen er eerst andere dingen moeten gebeuren en daarom zal de return in de exit functie gebeuren
        # elif len(node.children[0].children) == 0:
        #     self.enteredReturn = False
        #     # Controleren of de node als kind een value of indentifier heeft
        #     if node.children[0].token == "IDENTIFIER":
        #         # We moeten dan de register hiervan opvragen en returnen
        #         symboltable = tableLookup(node.children[0])
        #         symbol_lookup = symbolLookup(str(node.children[0].value), symboltable, afterTotalSetup=True,
        #                                      varLine=node.children[0].line, varColumn=node.children[0].column)[1]
        #         reg = symbol_lookup.register
        #         reg, line = self.load(reg, self.returnType, symbol_lookup.pointer)
        #         self.line += line
        #         self.line += "  ret " + types[self.returnType][0] + " %" + str(reg)
        #
        #     else:
        #         # Als het een char is moeten we deze eerst nog omzetten naar een integer
        #         val = str(node.children[0].value)
        #         if self.returnType == "CHAR":
        #             val = str(ord(str(node.children[0].value)[1]))
        #
        #         self.line += "  ret " + types[self.returnType][0] + " " + val
        #
        # if not self.enteredReturn:
        #     self.line += "\n}\n\n"

    def exitReturn(self, node):
        print("exitReturn")
        # We controleren nog of we nog de return moeten toepassen, dit is het geval wanneer de bool nog op true staat
        if self.enteredReturn:

            # We kunnen een return hebben in een if of else of while of for
            # Als deze stacks nog niet leeg zijn betekent dat we hier een return aanroepen dus we
            # voeren geen return uit maar gaan branchen naar de laatste return, dit wordt automatisch gedaan
            # if len(self.returnStack) > 0:
            #     if self.returnStack[-1][2] is False:
            #         self.store(self.returnStack[-1][0], self.hasReturnNode[1], self.returnStack[-1][1], False, True)
            #         self.returnStack.pop()
            #         self.enteredReturn = False
            #     else:
            #         self.store(self.returnStack[-1][0], self.hasReturnNode[1], self.returnStack[-1][1], True, True)
            #         self.returnStack.pop()
            #         self.enteredReturn = False
            # else:
            #     # Op dit moment zou er ook nog maar 1 element in de stack mogen zitten die die uitkomst bevat
            #     elem = self.returnStack[-1]
            #     self.returnStack.pop()
            #     # We returen dit register nog
            #     # self.line += "  ret " + types[elem[1]][0] + " %" + str(elem[0])
            #     self.enteredReturn = False
            #     self.line += "\n"

            returnReg = self.returnStack[-1]
            self.returnStack.pop()

            toReg, line = self.load(returnReg[0], returnReg[1])
            self.line += line

            line = "\n\tsw\t" + str(toReg) + ", 0($fp)\n" + \
                   "\tlw $ra, " + str(self.stackOffset - 8) + "($sp)\n" + \
                   "\taddi\t$sp,$fp,0\n" + \
                   "\tlw\t$fp, -4($sp)\n"

            if not self.isMain:
                line += "\tjr\t$ra\n\n"
                self.isMain = False

            self.line += line
            self.line += "\n"
            self.enteredReturn = False

    def enterPrintf(self, node):
        print("enterPrintf")
        self.enteredPrintf = True
        # We predefinen hier al de count voor de string links in de printf functie omdat er nadien nog kunnen toegevoegd worden
        self.curPrintf = self.stringCount
        self.printf = True

    def exitPrintf(self, node):
        print("exitPrintf")
        if self.enteredPrintf:
            text = self.printfStack[0]
            textsize = text[3]
            textcount = text[0]
            stringElem = None
            deleteIndex = 0
            # self.line += "printf" + textcount + ":" + "\n"
            for i in range(len(self.strings)):  # om uiteindelijk de string zelf te verkrijgen
                if textcount == self.strings[i][1]:
                    stringElem = self.strings[i]
                    deleteIndex = i
                    break

            splitString = []
            actualString = stringElem[2][1:-1]
            if len(self.printfStack) > 1:  # we hebben extra argumenten bij de printf
                char = 0
                curString = ""
                while char != len(actualString):
                    if actualString[char] == "%":
                        if curString != "":
                            splitString.append(curString)
                        curString = actualString[char] + actualString[char + 1]
                        splitString.append(curString)
                        curString = ""
                        char += 2
                    else:
                        curString += actualString[char]
                        char += 1
                        if char == len(actualString):
                            splitString.append(curString)
            else:
                splitString.append(actualString)

            del self.strings[deleteIndex]
            printfStackIndex = 1
            for i in range(len(splitString)):
                if splitString[i][0] == "%":

                    elem = self.printfStack[printfStackIndex]
                    name = ""
                    if elem[1] == "TEXT":
                        str_ = "str"
                        str_ += str(elem[0])
                        name = str_
                    else:
                        # if elem[1] == "CHAR": #TODO: dit ook nog bekijken
                        #     name = str(elem[0]) if elem[2] else str(ord(str(elem[0])[1]))
                        #     # self.line += "%" + str(elem[0]) if elem[2] else str(ord(str(elem[0])[1]))
                        # else:
                        # self.line += types[elem[1]][0] + " "
                        # self.line += "%" + str(elem[0]) if elem[2] else str(elem[0])
                        name = str(elem[0])
                        name, line = self.load(name, elem[1])
                        self.line += line

                    if splitString[i][1] == "d":
                        self.line += "\tla $a0, (" + name + ")\n"
                        self.line += "\tli $v0, 1\n"
                        self.line += "\tsyscall\n\n"

                    elif splitString[i][1] == "f":

                        self.line += "\tmov.s $f12, " + name + "\n"
                        self.line += "\tli $v0, 2\n"
                        self.line += "\tsyscall\n\n"

                    elif splitString[i][1] == "c":

                        self.line += "\tla $a0, (" + name + ")\n"
                        self.line += "\tli $v0, 11\n"
                        self.line += "\tsyscall\n\n"

                    elif splitString[i][1] == "s":

                        self.line += "\tla $a0, " + name + "\n"
                        self.line += "\tli $v0, 4\n"
                        self.line += "\tsyscall\n\n"

                    printfStackIndex += 1
                else:
                    name = str(self.stringCount)
                    isAanwezig = False
                    for j in range(len(self.strings)):
                        if self.strings[j][2] == splitString[i]:
                            name = self.strings[j][1]
                            isAanwezig = True
                            break
                    name = "str" + name

                    if not isAanwezig:
                        self.strings.append((0, str(self.stringCount), splitString[i]))
                        self.stringCount += 1
                        line = name + ":\t" + ".asciiz\t" + "\"" + splitString[i] + "\"\n"
                        self.globals.append(line)

                    self.line += "\tla $a0, " + name + "\n"
                    self.line += "\tli $v0, 4\n"
                    self.line += "\tsyscall\n\n"

            self.printfStack.clear()
            self.enteredPrintf = False

    def enterScanf(self, node):
        print("enterScanf")
        self.enteredScanf = True
        # We predefinen hier al de count voor de string links in de printf functie omdat er nadien nog kunnen toegevoegd worden
        self.curPrintf = self.stringCount
        self.scanf = True

    def exitScanf(self, node):
        print("exitScanf")
        if self.enteredScanf:
            self.enteredScanf = False

            text = self.scanfStack[0]
            textsize = text[3]
            textcount = text[0]
            stringElem = ""
            for i in range(len(self.strings)):  # om uiteindelijk de string zelf te verkrijgen
                if textcount == self.strings[i][1]:
                    stringElem = self.strings[i]
                    break

            actualString = stringElem[2][1:-1]
            splitString = []
            if len(self.scanfStack) > 1:  # dit zal eigenlijk altijd normaal zo zijn
                char = 0
                curString = ""
                while char != len(actualString):
                    if actualString[char] == "%":
                        curString = actualString[char] + actualString[char + 1]
                        splitString.append(curString)
                        curString = ""
                        char += 2
                    # else:
                    #     curString += actualString[char]
                    #     char += 1
                    #     if char == len(actualString):
                    #         splitString.append(curString)
            else:
                splitString.append(actualString)

            printfStackIndex = 1
            for i in range(len(splitString)):
                if splitString[i][0] == "%":  # zou normaal altijd het geval moeten zijn

                    elem = self.scanfStack[printfStackIndex]
                    name = ""
                    # if elem[1] == "TEXT":
                    #     str_ = "str"
                    #     str_ += str(elem[0])
                    #     name = str_
                    # else:
                    #     # if elem[1] == "CHAR": #TODO: dit ook nog bekijken
                    #     #     name = str(elem[0]) if elem[2] else str(ord(str(elem[0])[1]))
                    #     #     # self.line += "%" + str(elem[0]) if elem[2] else str(ord(str(elem[0])[1]))
                    #     # else:
                    #     # self.line += types[elem[1]][0] + " "
                    #     # self.line += "%" + str(elem[0]) if elem[2] else str(elem[0])
                    #     name = str(elem[0])
                    #     name, line = self.load(name, elem[1])
                    #     self.line += line

                    if splitString[i][1] == "d":
                        self.line += "\tli $v0, 5\n"
                        self.line += "\tsyscall\n"  # result in v0
                        self.line += "\tmove $t0, $v0\n"

                        self.store("$t0", elem[0])

                    elif splitString[i][1] == "f":
                        self.line += "\tli $v0, 6\n"
                        self.line += "\tsyscall\n\n"  # result in f0

                        self.store("$f0", elem[0])

                    elif splitString[i][1] == "c":
                        self.line += "\tli $v0, 12\n"
                        self.line += "\tsyscall\n"  # result in v0
                        self.line += "\tmove $t0, $v0\n"

                        self.store("$t0", elem[0])

                    elif splitString[i][1] == "s":
                        buffer = "buffer" + str(self.stringCount)
                        length = 32
                        self.strings.append((0, str(self.stringCount), str(length)))
                        line = buffer + ":\t" + ".space\t" + str(length) + "\n"
                        self.globals.append(line)
                        self.line += "\tli $v0, 8\n"
                        self.line += "\tla $a0, " + buffer + "\n"
                        self.line += "\tli $a1, " + str(length) + "\n"
                        self.line += "\tsyscall\n\n"

                        self.stringCount += 1

                    printfStackIndex += 1

            # inbound = "[" + str(textsize) + " x i8], [" + str(textsize) + " x i8]*"
            # str_ = "@.str"
            # str_ += str(textcount) if int(textcount) > 0 else ""
            # self.line += "  %" + str(
            #     self.register) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds (" + inbound + " " + str_ + ", i64 0, i64 0)"
            # self.register += 1
            # for i in range(1, len(self.scanfStack)):
            #     elem = self.scanfStack[i]
            #     self.line += ", "
            #     self.line += types[elem[1]][0] + "* "
            #     self.line += "%" + str(elem[0]) if elem[2] else str(elem[0])

            self.scanfStack.clear()
            self.enteredScanf = False

    def enterIf_stmt(self, node):
        print("enterIf_stmt")
        # De conditie is net gedaan, we halen het resultaat hieruit en branchen

        condtion = self.conditionStack[-1]
        self.conditionStack.pop()
        self.ifStack.append(self.ifLabelCount)
        self.ifLabelCount += 1
        self.ifStack.append(self.ifLabelCount)
        self.ifLabelCount += 1
        toReg = condtion[0]
        toReg, line = self.load(toReg, condtion[1])
        self.line += line
        if self.wasLogical or not condtion[2]:
            # De logical gaat normaal gezien altijd een int returnen dat
            # Deze moeten we eerst nog omzetten naar een bool (i1)
            toReg, type, line = self.compare("ne", condtion[0], 0, condtion[1], "INT", condtion[2], False, True)
            self.line += line
            self.wasLogical = False

        self.branch(str(toReg), str(self.ifStack[-2]), str(self.ifStack[-1]), self.ifStack[-2], "if")

        self.line = self.line.replace("if" + str(self.ifStack[-2]), "__IF_" + str(self.ifElseCount) + "__")
        self.ifElseCount += 1

    def exitIf_stmt(self, node):
        print("exitIf_stmt")

        # Als we geen else hebben
        if node == node.parent.children[-1]:

            if not self.isBreaked:
                # We branchen nu gewoon naar de volgende branch met het laatste element in de stack
                self.line += "\tb if" + str(self.ifStack[-1]) + "\n\n"
                self.line += "if" + str(self.ifStack[-1]) + ":\n"
                self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_" + str(self.ifElseCount) + "__")
                self.ifElseCount += 1
                # Poppen de 2 labels uit de stack

            else:
                self.isBreaked = False

            self.ifStack.pop()
            self.ifStack.pop()
        # We hebben een else
        else:
            self.ifStack.append(self.ifLabelCount)
            self.ifLabelCount += 1
            if not self.isBreaked:
                self.line += "\tb if" + str(self.ifStack[-1]) + "\n\n"

    def enterElse_stmt(self, node):
        print("enterElse_stmt")

        # nu maken we het deel voor de else aan
        if not self.isBreaked:
            self.line += "if" + str(self.ifStack[-2]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-2]), "__ELSE_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1

        else:
            self.isBreaked = False

    def exitElse_stmt(self, node):
        print("exitElse_stmt")

        if not self.isBreaked:
            # Nu branchen we nog naar de laatst toegevoegde else
            self.line += "\tb if" + str(self.ifStack[-1]) + "\n\n"
            self.line += "if" + str(self.ifStack[-1]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_ELSE_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1

        else:
            self.isBreaked = False

        # Poppen de 3 labels uit de stack
        self.ifStack.pop()
        self.ifStack.pop()
        self.ifStack.pop()

    def enterWhile_stmt(self, node):
        print("enterWhile_stmt")
        # We gaan nu de branch maken

        toReg, line = self.load(self.conditionStack[-1][0], self.conditionStack[-1][1])
        self.line += line
        self.branch(toReg, self.whileStack[-1][0], self.whileLabelCount, self.whileStack[-1][0], "while")

        # self.line += "  br i1 %" + toReg + ", label %" + str(
        #     self.register) + ", label %while" + str(self.whileLabelCount) + "\n\n"
        # self.line += str(self.whileStack[-1][0]) + ":\n"
        self.line = self.line.replace("while" + str(self.whileStack[-1][0]), "__WHILE_" + str(self.whileCount) + "__")
        self.whileStack.append((self.whileLabelCount, False))
        self.whileLabelCount += 1
        self.whileCount += 1

    def exitWhile_stmt(self, node):
        print("exitWhile_stmt")

        # We maken een branch naar het begin van de while loop, dit zou de voorlaatste value moeten zijn in de stack
        self.line += "\tb __WHILE_CONDITION_" + str(self.whileStack[-2][0]) + "__\n\n"

        # We maken de andere branch aan
        self.line += "while" + str(self.whileStack[-1][0]) + ":\n"
        self.line = self.line.replace("while" + str(self.whileStack[-1][0]),
                                      "__END_WHILE_" + str(self.whileCount) + "__")
        self.whileCount += 1
        self.whileStack.pop()
        self.whileStack.pop()

    def enterAssignment(self, node):
        print("enterAssignment")
        self.enteredAssignment = True

        # Als we gewoon een assignment hebben van een value aan een variable kunnen we dit direct hier doen

        # check of child een array is of niet

        if str(node.children[0].token) != "ARRAY":

            if len(node.children[1].children) == 0:  # e.g. int a = 5; of int a = b;
                # We vragen de symbol lookup op van het linker deel
                symboltable = tableLookup(node)
                symbol_lookup = symbolLookup(str(node.children[0].value), symboltable, afterTotalSetup=True,
                                             varLine=node.children[0].line, varColumn=node.children[0].column)[1]
                offset1 = symbol_lookup.stackOffset
                type1 = node.children[0].type
                # Dan controleren we nog of de rechterkant een identifier is of niet
                if node.children[1].token == "IDENTIFIER":
                    # Moeten hiervoor zijn register ook terug opvragen
                    symboltable2 = tableLookup(node.children[1])
                    symbol_lookup2 = symbolLookup(str(node.children[1].value), symboltable2, afterTotalSetup=True,
                                                  varLine=node.children[1].line, varColumn=node.children[1].column)[1]

                    offset2 = symbol_lookup2.stackOffset

                    toReg, line = self.load(offset2, symbol_lookup2.type)

                    self.line += line
                    if symbol_lookup.type == "INT" and symbol_lookup2.type == "FLOAT":
                        toReg = self.floatToInt(toReg)

                    elif symbol_lookup.type == "FLOAT" and symbol_lookup2.type == "INT":
                        toReg = self.intToFloat(toReg)

                    self.store(toReg, offset1)

                else:  # non-identifier rechts
                    # We nemen hier gewoon de waarde zelf van het attribuut
                    val = str(node.children[1].value)
                    if symbol_lookup.type == "INT" and node.children[1].type == "FLOAT":
                        val = val.partition('.')[0]
                    # elif symbol_lookup.type == "FLOAT" and node.children[1].type == "INT":
                    #     toReg = self.intToFloat(toReg)

                    toReg, line = self.loadInReg(val, type1)
                    self.line += line
                    self.store(toReg, offset1)

                # Na we dit hebben gedaan kunnen we enterAss terug afzetten
                self.enteredAssignment = False

        else:
            if len(node.children[1].children) == 0:
                # We vragen de symbol lookup op van het linker deel
                symboltable = tableLookup(node)
                symbol_lookup = symbolLookup(str(node.children[0].children[0].value), symboltable, afterTotalSetup=True,
                                             varLine=node.children[0].children[0].line,
                                             varColumn=node.children[0].children[0].column)[1]
                type1 = symbol_lookup.type
                reg1 = self.loadArray(symbol_lookup.register, symbol_lookup.arrayData[0], type1,
                                      node.children[0].children[1].children[0].value)
                # Dan controleren we nog of de rechterkant een identifier is of niet
                if node.children[1].token == "IDENTIFIER":
                    # Moeten hiervoor zijn register ook terug opvragen
                    symboltable2 = tableLookup(node.children[1])
                    symbol_lookup2 = symbolLookup(str(node.children[1].value), symboltable2, afterTotalSetup=True,
                                                  varLine=node.children[1].line, varColumn=node.children[1].column)[1]
                    reg2 = symbol_lookup2.register

                    toReg, line = self.load(reg2, symbol_lookup2.type, symbol_lookup2.pointer)
                    self.line += line
                    if symbol_lookup.type == "INT" and symbol_lookup2.type == "FLOAT":
                        toReg = self.floatToInt(toReg)
                    elif symbol_lookup.type == "FLOAT" and symbol_lookup2.type == "INT":
                        toReg = self.intToFloat(toReg)
                    self.store(toReg, reg1, type1, True, True, symboltable.pointer)
                else:
                    # We nemen hier gewoon de waarde zelf van het attribuut
                    val = str(node.children[1].value)
                    if symbol_lookup.type == "INT" and node.children[1].type == "FLOAT":
                        val = val.partition('.')[0]
                    # elif symbol_lookup.type == "FLOAT" and node.children[1].type == "INT":
                    #     toReg = self.intToFloat(toReg)

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

            if str(node.children[0].token) != "ARRAY":

                # We vragen het register en type op van de variable
                symboltable = tableLookup(node.children[0])
                symbol_lookup = \
                    symbolLookup(str(node.children[0].value), symboltable, afterTotalSetup=True,
                                 varLine=node.children[0].line,
                                 varColumn=node.children[0].column)[1]
                offset = symbol_lookup.stackOffset

                # En we doen store
                toReg, line = self.load(elem[0], elem[1])
                self.line += line
                self.store(toReg, offset)
                self.enteredAssignment = False

            else:
                # We vragen het register en type op van de variable
                symboltable = tableLookup(node.children[0].children[0])
                symbol_lookup = \
                    symbolLookup(str(node.children[0].children[0].value), symboltable, afterTotalSetup=True,
                                 varLine=node.children[0].children[0].line,
                                 varColumn=node.children[0].children[0].column)[1]
                reg = symbol_lookup.register
                type = symbol_lookup.type

                reg = self.loadArray(reg, symbol_lookup.arrayData[0], type,
                                     node.children[0].children[1].children[0].value)

                # En we doen store
                self.store(elem[0], reg, type, True, True, symbol_lookup.pointer)
                self.enteredAssignment = False

    def enterUnaryOperation(self, node):
        print("enterUnaryOperation")

    def exitUnaryOperation(self, node):
        print("exitUnaryOperation")
        # We controleren of het een ++ of -- is
        child = node.children[0]
        tableLookup__ = tableLookup(child)
        symbolTable = \
            symbolLookup(str(child.value), tableLookup__, afterTotalSetup=True, varLine=node.line,
                         varColumn=node.column)[1]

        if str(node.value) == "++":
            toReg = None
            if not self.enteredCondition:
                toReg, line = self.load(symbolTable.stackOffset, symbolTable.type)
                self.line += line
            else:
                toReg = self.conditionStack[-1][0]
            toReg, toType, line = self.operate(calculations_["+"], toReg, 1, symbolTable.type, "INT", True, False)
            self.line += line
            self.store(toReg, symbolTable.stackOffset)


        elif str(node.value) == "--":
            toReg = None
            if not self.enteredCondition:
                toReg, line = self.load(symbolTable.stackOffset, symbolTable.type)
                self.line += line
            else:
                toReg = self.conditionStack[-1][0]
            toReg, toType, line = self.operate(calculations_["-"], toReg, 1, symbolTable.type, "INT", True, False)
            self.line += line
            self.store(toReg, symbolTable.stackOffset)

    def enterBreak(self, node):
        print("enterBreak")

    def exitBreak(self, node):
        print("exitBreak")
        # We controlleren of we in een if/else waren
        # Als de lengte van onze stack %2 == 0 is dan zitten we in de if
        # Als de lengte van onze stack %3 == 0 is dan zitten we in de else

        if len(self.ifStack) % 2 == 0:
            # We branchen naar de while zijn eind en maken de if zijn false aan
            self.line += "\tb while" + str(self.whileStack[-1][0]) + "\n\n"
            self.line += "if" + str(self.ifStack[-1]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1
            self.isBreaked = True

        elif len(self.ifStack) % 3 == 0:
            # We branchen naar de while zijn eind en maken de label voor de branchen buiten de else aan
            self.line += "\tb while" + str(self.whileStack[-1][0]) + "\n\n"
            self.line += "if" + str(self.ifStack[-1]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_ELSE_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1
            self.isBreaked = True

    def enterContinue(self, node):
        print("enterContinue")

    def exitContinue(self, node):
        print("exitContinue")
        # We controlleren of we in een if/else waren
        # Als de lengte van onze stack %2 == 0 is dan zitten we in de if
        # Als de lengte van onze stack %3 == 0 is dan zitten we in de else

        if len(self.ifStack) % 2 == 0:
            # We branchen naar de while zijn condition en maken de if zijn false aan
            self.line += "\tb __WHILE_CONDITION_" + str(self.whileStack[-2][0]) + "__\n\n"
            self.line += "if" + str(self.ifStack[-1]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_ELSE_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1
            self.isBreaked = True

        elif len(self.ifStack) % 3 == 0:
            # We branchen naar de while zijn condition en maken de label voor de branchen buiten de else aan
            self.line += "\tb __WHILE_CONDITION_" + str(self.whileStack[-2][0]) + "__\n\n"
            self.line += "if" + str(self.ifStack[-1]) + ":\n"
            self.line = self.line.replace("if" + str(self.ifStack[-1]), "__END_IF_ELSE_" + str(self.ifElseCount) + "__")
            self.ifElseCount += 1
            self.isBreaked = True

    def enterFuncCall(self, node):
        print("enterFuncCall")
        self.enteredFunctionCall += 1

    def exitFuncCall(self, node):
        print("exitFuncCall")

        # TODO: naar dit ook nog eens uittesten
        if len(self.logicalStack) > 0:
            if node == self.logicalStack[-1][0]:
                print("func call")

        # We moeten eerst het type van de functie opvragen
        funcName = str(node.children[0].children[0].value)
        symboltable = tableLookup(node.children[0].children[0])
        # Betekent dat we de naam van de functie hebben, hier moeten we niets mee doen
        # TODO: ook nog lijn en kolom doorgeven
        symbol_lookup = symbolLookup(funcName, symboltable, afterTotalSetup=True)[1]
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

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredCondition:
            self.conditionStack.append((str(self.register - 1), outputtype, True))

        # Ook hier kan het zijn dat we een recursieve call hebben van aanroepen in elkaar dus moeten we deze ook eerst voorrang geven
        elif self.enteredAssignment:
            # Als dit het geval is moet de register van deze function call worden toegevoegd aan de stack
            self.assignmentStack.append((str(self.register - 1), outputtype, True))

    def enterBinOperation(self, node):
        print("enterBinOperation")

    def exitBinOperation(self, node):
        print("exitBinOperation")
        # We controleren of we in een assignment zijn gegaan

        func = lambda node1, stack, reg1, reg2, type_: (
            self.operate(calculations_[str(node1.value)], reg1, reg2, stack[-2][1], stack[-1][1],
                         stack[-2][2], stack[-1][2], type_))

        toReg = None
        toType = None

        if node.parent.token == "=":
            toType, toReg = node.parent.children[0].type

        if self.enteredFunctionCall > 0:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitBinOperationStackHandler(self.functionCallStack, node, func, toType)

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredReturn:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitBinOperationStackHandler(self.returnStack, node, func, toType)


        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredPrintf:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitBinOperationStackHandler(self.printfStack, node, func, toType)

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredCondition:
            toType = self.exitBinOperationStackHandler(self.conditionStack, node, func, toType)

        elif self.enteredAssignment:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitBinOperationStackHandler(self.assignmentStack, node, func, toType)

        if len(self.logicalStack) > 0:
            if node == self.logicalStack[-1][0] or node == self.logicalStack[-1][1]:
                toReg__, type, line = self.compare(
                    "sne" if toType == "INT" else "c.ne.s", "$zero", toReg, "INT", toType, True, True, True)
                self.popRightStack()

                self.line += line
                self.determineBranch(node, node.parent, toReg__)

    def enterIdentifier(self, node):
        print("enterIdentifier")

    def exitIdentifier(self, node):

        print("exitIdentifier")
        if node.parent.token == "NAME":
            return

        if node.parent.parent.token == "ROOT":
            # betekent dat we een globale variabele hebben
            self.makeGlobal(node)
            return

        symboltable = tableLookup(node)
        # Betekent dat we de naam van de functie hebben, hier moeten we niets mee doen
        symbol_lookup = \
            symbolLookup(str(node.value), symboltable, afterTotalSetup=True, varLine=node.line, varColumn=node.column)[
                1]

        func = lambda symbol_lookup: (
            self.load(symbol_lookup.stackOffset, symbol_lookup.type, None, symbol_lookup.isGlobal), symbol_lookup.type)

        reg = None
        type = None

        # als we een functioncall hebben dan heeft dit voorrang op een assignment omdat een functioncall in een assignment kan voorkomen
        if self.enteredFunctionCall > 0:
            type, reg = self.exitIdentifierStackHandler(self.functionCallStack, symbol_lookup, func)

        elif self.enteredReturn:
            type, reg = self.exitIdentifierStackHandler(self.returnStack, symbol_lookup, func)

        # Ook hier heeft de functioncall voorang
        elif self.enteredPrintf:
            type, reg = self.exitIdentifierStackHandler(self.printfStack, symbol_lookup, func)

            # # Als het een char is moeten we deze ook nog is omzetten naar een int
            # if type == "CHAR":
            #     self.line += "  %" + str(self.register) + " = sext i8 %" + str(reg[0]) + " to i32\n"
            #     reg = self.register, reg[1]
            #     self.register += 1
            # self.printfStack.append((reg[0], type, True))

        elif self.enteredScanf:
            type, reg = self.exitIdentifierStackHandler(self.scanfStack, symbol_lookup, func)

        # Ook hier heeft de functioncall voorang
        elif self.enteredCondition:
            type, reg = self.exitIdentifierStackHandler(self.conditionStack, symbol_lookup, func)

        # We controleren of we in een assignment zijn gegaan en dat het niet het linkerdeel is van de assign
        elif self.enteredAssignment and node.parent.token != "=":
            # We voegen het toe aan de stack
            # We laden eerst de variable in een nieuw register
            # Moet wel eerst het huidige register opvragen
            # reg = [symbol_lookup.register]
            # if str(node.parent.value) != "&":
            #     # if symbol_lookup.pointer == 0:
            #     reg, type = func(symbol_lookup, tempReg)
            #     self.line += reg[1]
            # # We geven het register mee en het type en zeggen dat een register is
            # self.assignmentStack.append((reg[0], type, True))

            type, reg = self.exitIdentifierStackHandler(self.assignmentStack, symbol_lookup, func)

        if len(self.logicalStack) > 0:
            if node == self.logicalStack[-1][0] or node == self.logicalStack[-1][1]:
                # We gaan nu de compare opartion uitvoeren
                toReg__, type, line = self.compare(
                    "sne" if type == "INT" else "c.ne.s", "$zero", reg, "INT", type, True, True, True)

                # Omdat we da waarde uit de stack al hebben gebruikt moeten we deze nog wel terug verwijderen
                self.popRightStack()

                self.line += line
                self.determineBranch(node, node.parent, toReg__)

    def enterType(self, node):
        print("enterType")

    def exitType(self, node):
        print("exitType")
        toReg, toType = None, None
        # Functioncall krijgt voorrang
        if self.enteredFunctionCall > 0:
            toReg, toType = self.exitTypeStackHandler(self.functionCallStack, node)

        # Ook hier heeft de functioncall voorang
        elif self.enteredReturn:
            toReg, toType = self.exitTypeStackHandler(self.returnStack, node)

        # Ook hier heeft de functioncall voorang
        elif self.enteredPrintf:
            toReg, toType = self.exitTypeStackHandler(self.printfStack, node)

        # Ook hier heeft de functioncall voorang
        elif self.enteredCondition:
            toReg, toType = self.exitTypeStackHandler(self.conditionStack, node)

        # We controleren of we in een assignment zijn gegaan
        elif self.enteredAssignment:
            toReg, toType = self.exitTypeStackHandler(self.assignmentStack, node)

        if len(self.logicalStack) > 0:  # TODO: dit later nog afhandelen
            if node == self.logicalStack[-1][0] or node == self.logicalStack[-1][1]:
                self.popRightStack()
                toReg__, type, line = self.compare(
                    "sne" if toType == "INT" else "c.ne.s", "$zero", toReg, "INT", toType, True, True, True)

                self.line += line
                self.determineBranch(node, node.parent, toReg__)

    def enterString(self, node):
        pass

    def exitString(self, node):

        if self.enteredPrintf or self.enteredScanf:
            # Ookal kan dit enkel hier voorkomen, een check kan geen kwaad
            text = str(node.value)
            textsize = len(text)
            text = "\"" + text + "\""
            strCount = None
            for i in range(len(self.strings)):
                if text == self.strings[i][2]:
                    strCount = self.strings[i][1]
                    break

            if self.enteredPrintf:
                if strCount is not None:
                    self.printfStack.append((strCount, "TEXT", False, textsize))
                else:
                    self.strings.append((textsize, str(self.stringCount), text))
                    self.printfStack.append((str(self.stringCount), "TEXT", False, textsize))
                    self.stringCount += 1

            elif self.enteredScanf:
                if strCount is not None:
                    self.scanfStack.append((strCount, "TEXT", False, textsize))
                    self.stringCount += 1
                else:
                    self.strings.append((textsize, str(self.stringCount), text))
                    self.scanfStack.append((str(self.stringCount), "TEXT", False, textsize))
                    self.stringCount += 1

    def enterComparison(self, node):
        print("enterComparison")

    def exitComparison(self, node):
        print("exitComparison")

        func = lambda node1, stack, condition, reg1, reg2: (
            self.compare(data_comp_instr[str(node1.value)] if stack[-2][1] == "INT" and stack[-1][1] == "INT" else
                         data_comp_instr_f[str(node1.value)], reg1, reg2, stack[-2][1], stack[-1][1],
                         stack[-2][2], stack[-1][2], condition))

        toReg = None
        toType = None

        if self.enteredFunctionCall > 0:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            self.exitComparisonStackHandler(self.functionCallStack, node, func, False)

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredReturn:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitComparisonStackHandler(self.returnStack, node, func, False)


        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredPrintf:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitComparisonStackHandler(self.printfStack, node, func, False)

        # Ook hier heeft de functioncall eerst voorrang
        elif self.enteredCondition:
            toType, toReg = self.exitComparisonStackHandler(self.conditionStack, node, func, True)

        elif self.enteredAssignment:
            # Dit betekent dat we normaal gezien 2 items heb de stack hebben zitten
            # Waar we de operation moeten uitvoeren
            toType, toReg = self.exitComparisonStackHandler(self.assignmentStack, node, func, False)

        if len(self.logicalStack) > 0:  # TODO: dit nog bekijken
            if node == self.logicalStack[-1][0] or node == self.logicalStack[-1][1]:
                # Omdat we da waarde uit de stack al hebben gebruikt moeten we deze nog wel terug verwijderen
                self.popRightStack()
                self.determineBranch(node, node.parent, toReg)
                if self.isComparison:
                    node.parent.fromRegBrM = toReg

    def enterLogical(self, node):
        print("enterLogical")
        """
        Het idee is eigenlijk dat wanneer we een logical betreden dat we op deze moment bekijken in welke 
        situatie ons bevinden
        heeft de logical operator links wel of niet een logical operator, heeft het rechts wel of niet een logical operator
        """

        # Als het links een logical operation hebben doen we niets, anders wel

        leftChild = node.children[0]
        rightChild = None
        if node.value != "!":
            rightChild = node.children[1]

        stackContent = [None, None]

        if str(leftChild.value) not in logicals:
            # We slagen deze node op, wanneer we een node verlaten waar deze node gelijk is aan die node gaan we de br aanmaken
            # Dit kan een identifier, bin op, comp op, func call of gewoon een value zijn
            stackContent[0] = leftChild

        if rightChild is not None:
            if str(rightChild.value) not in logicals:
                # We slagen deze node op, wanneer we een node verlaten waar deze node gelijk is aan die node gaan we de br aanmaken
                # Dit kan een identifier, bin op, comp op, func call of gewoon een value zijn
                stackContent[1] = rightChild

        self.logicalStack.append(stackContent)

        # TODO: add
        if node.parent is not None:
            # We nemen de parent zijn labels over (moete deze niet kloppen worden deze later toch overschreven)
            node.trueLabelM = node.parent.trueLabelM
            node.falseLabelM = node.parent.falseLabelM

        # We gaan ook een final register alloceren waar de uitkomst in komt
        # if self.finalRegLog is None:
        #     self.finalRegLog = self.register
        #     self.register += 1
        #     self.allocate(self.finalRegLog, "INT")

    def exitLogical(self, node):
        print("exitLogical")

        if len(self.logicalStack) > 0:
            self.logicalStack.pop()
        # We controleren dat de node zijn parent een log is of niet
        parent = node.parent

        if str(parent.value) in logicals:

            # Als dit het geval is gaan we kijken of we het rechter of linkerkind zijn
            if node == parent.children[0]:
                # Als we het linkerkind zijn kijken we naar de parent zijn logical

                if logicals[str(parent.value)] == "AND":
                    # We branchen dan met de Truelabel van de node
                    # We voeren nog een comparison uit

                    self.branch(node.fromRegBrM, node.trueLabelM, node.falseLabelM, node.trueLabelM, "x")
                    self.line = self.line.replace("x" + str(node.trueLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1
                    parent.falseLabelM = node.falseLabelM

                elif logicals[str(parent.value)] == "OR":
                    # We branchen met het Falselabel van de node
                    self.branch(node.fromRegBrM, node.trueLabelM, node.falseLabelM, node.falseLabelM, "x")
                    self.line = self.line.replace("x" + str(node.falseLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1
                    parent.trueLabelM = node.trueLabelM

                elif logicals[str(parent.value)] == "NOT":
                    parent.trueLabelM = node.trueLabelM
                    parent.falseLabelM = node.falseLabelM
                    parent.fromRegBrM = node.fromRegBrM

            elif node == parent.children[1]:
                # Als we het rechterkind zijn kijken we naar de parent zijn logical

                if logicals[str(parent.value)] == "AND":
                    # We gaan niet branchen, we geven gewoon de truelabel door aan de parent
                    parent.trueLabelM = node.trueLabelM
                    parent.fromRegBrM = node.fromRegBrM

                elif logicals[str(parent.value)] == "OR":
                    # We gaan niet branchen, we geven gewoon het falseLabel door aan de parent
                    parent.falseLabelM = node.falseLabelM
                    parent.fromRegBrM = node.fromRegBrM

        else:
            # Nu moeten we nog 2 branches maken en de final branch
            # De 2 branches geven aan of de volledige expressie true of false is
            # De final branch zal de rest van de scope zijn

            if not self.isComparison:
                # We maken eerst de branch aan met een nieuw falseLabel
                self.branch(node.fromRegBrM, node.trueLabelM, node.falseLabelM, node.falseLabelM, "x")
                self.line = self.line.replace("x" + str(node.falseLabelM), "__label_" + str(self.labelCount) + "__")
                self.labelCount += 1
            else:
                self.isComparison = False
                self.wasLogical = True
                self.branch(node.fromRegBrM, node.trueLabelM, node.falseLabelM, node.falseLabelM, "x")
                self.line = self.line.replace("x" + str(node.falseLabelM), "__label_" + str(self.labelCount) + "__")
                self.labelCount += 1

            # Nu gaan we hier een false in het eind register plaatsen
            toReg, line = self.loadInReg(0, "INT")
            self.line += line

            # We doen hier een branch naar het final label
            self.line += "\tb x" + str(self.logLabelCount) + "\n\n"

            # Nu de true branch
            self.line += "x" + str(node.trueLabelM) + ":\n"

            self.line = self.line.replace("x" + str(node.trueLabelM), "__label_" + str(self.labelCount) + "__")
            self.labelCount += 1

            # We storen een true in het eind register
            toReg, line = self.loadInReg(1, "INT")
            self.line += line

            # We doen hier een branch naar het final label
            self.line += "\tb x" + str(self.logLabelCount) + "\n\n"

            # We maken de final branch aan

            self.line += "x" + str(self.logLabelCount) + ":\n"

            self.line = self.line.replace("x" + str(self.logLabelCount), "__label_" + str(self.labelCount) + "__")
            self.labelCount += 1

            toType = "INT"

            self.store(toReg, self.offset)

            if self.enteredFunctionCall > 0:
                self.functionCallStack.append((self.offset, toType, True))

                # Ook hier heeft de functioncall eerst voorrang
            elif self.enteredReturn:
                self.returnStack.append((self.offset, toType, True))

                # Ook hier heeft de functioncall eerst voorrang
            elif self.enteredPrintf:
                self.printfStack.append((self.offset, toType, True))

                # Ook hier heeft de functioncall eerst voorrang
            elif self.enteredCondition:
                self.conditionStack.append((self.offset, toType, True))

            elif self.enteredAssignment:
                self.assignmentStack.append((self.offset, toType, True))

            # We resetten de values
            self.finalRegLog = None
            self.logLabelCount = 0
            self.offset -= 4

    def enterCondition(self, node):
        print("enterCondition")
        self.enteredCondition = True

        # We kijken of het een condition is van een while of niet, als dit zo is dan moeten we eerst een branch doen
        if node.parent.children[-1].token == "WHILE":
            self.line += "\tb while" + str(self.whileLabelCount) + "\n\n"
            self.line += "while" + str(self.whileLabelCount) + ":\n"
            self.line = self.line.replace("while" + str(self.whileLabelCount),
                                          "__WHILE_CONDITION_" + str(self.whileCount) + "__")
            self.whileStack.append((self.whileLabelCount, True))
            self.whileLabelCount += 1
            self.whileCount += 1

    def exitCondition(self, node):
        print("exitCondition")
        if self.enteredCondition:
            # controleren nog voor de zekerheid
            self.enteredCondition = False

    def enterArray(self, node):
        print("enterArray")

        # We checken of het een declaration is of niet

        if not node.children[0].isDeclaration:
            pass

    def exitArray(self, node):
        print("exitArray")

    def allocateVariables(self, symbolTable):
        # We vragen de dict op met alle variable
        toAllocate = symbolTable.dict
        params = []
        for key in toAllocate:

            type = toAllocate[key].type
            # We checken dan voor de zekerheid of het wel een identifier is
            if toAllocate[key].value.token == "IDENTIFIER" or toAllocate[key].value.parent.children[
                0].token == "IDENTIFIER":
                # tempReg = toAllocate[key].stackOffset

                toAllocate[key].stackOffset = self.stackOffset - 4
                if toAllocate[key].arrayData is not False:
                    pass
                    # self.line += "  %" + str(self.register) + " = alloca ["
                    # length = str(toAllocate[key].arrayData[0])
                    # self.line += length + " x " + types[type][0] + "], " + types[type][1] + "\n"
                else:
                    self.allocate(self.register, type, toAllocate[key].pointer)
                self.stackOffset += 4
                # if toAllocate[key].isParam:
                #     params.append((tempReg, toAllocate[key].register, toAllocate[key].type, toAllocate[key].pointer))

        # Nu gaan we de parameters hun waarde storen in de nieuwe registers
        # for param in params:
        #     self.store(param[0], param[1], param[2], True, True, param[3])

    def allocate(self, register, type, numberOfPointer=0):
        pass
        # pointerAm = ""
        # for i in range(numberOfPointer):
        #     pointerAm += "*"
        #
        # self.line += "  %" + str(register) + " = alloca " + types[type][0] + pointerAm + ", " + types[type][1] + "\n"

    def allTables(self, symbolTable):
        self.allocateVariables(symbolTable)

        for table in symbolTable.childrenTables:
            self.allTables(table)

    def makeGlobal(self, node):
        tableLookup_ = tableLookup(node)
        symbolTable = \
            symbolLookup(node.value, tableLookup_, afterTotalSetup=True, varLine=node.line, varColumn=node.column)[1]
        type = symbolTable.type
        value = str(symbolTable.value.value)
        if type == 'CHAR':
            value = value.replace("'", '"')
        name = str(node.value)
        symbolTable.stackOffset = name
        symbolTable.isGlobal = True
        line = name + ":" + "\t" + "." + global_types[type] + " " + value + "\n"
        self.globals.append(line)

    def store(self, fromRegister, offset):

        # leftPoint = ""
        # rightPoint = "*"
        #
        # for i in range(numberOfPointer):
        #     leftPoint += "*"
        #     rightPoint += "*"
        #
        # reg1 = "%" + str(fromRegister) if isReg1 else str(fromRegister)
        # reg2 = "%" + str(toRegister) if isReg2 else str(toRegister)
        #
        # if type == "CHAR" and not isReg1:
        #     reg1 = str(ord(str(reg1[1])))
        #
        # if type == "FLOAT":
        #     if not isReg1:
        #         reg1 = str(reg1) + "e+00"
        #     if not isReg2:
        #         reg2 = str(reg2) + "e+00"
        #
        # self.line += "  store " + types[type][0] + leftPoint + " " + reg1 + ", " + types[type][
        #     0] + rightPoint + " " + reg2 + "" \
        #                                    ", " + \
        #              types[type][1] + "\n"

        storeCommand = "sw" if str(fromRegister)[1] != "f" else "swc1"
        self.line += "\t" + storeCommand + "\t" + str(fromRegister) + "," + str(offset) + "($sp)\n"

    def load(self, fromReg, type, toReg_=None, isGlobal=None):

        line = ""
        toReg = "$t0" if type != "FLOAT" else "$f0"

        if toReg_:
            toReg = toReg_

        if not isGlobal:
            if type != "FLOAT":
                line += "\tlw\t" + toReg + "," + str(fromReg) + "($sp)\n"

            else:
                line += "\tlwc1\t" + toReg + "," + str(fromReg) + "($sp)\n"

        else:
            if type != "FLOAT":
                line += "\tlw\t" + toReg + "," + str(fromReg) + "\n"

            else:
                line += "\tlwc1\t" + toReg + "," + str(fromReg) + "\n"

        return toReg, line

    def loadArray(self, fromReg, length, type, index):

        self.line += "  %" + str(self.register) + " = getelementptr inbounds [" + str(length) + " x " + types[type][
            0] + "], [" + str(length) + " x " + types[type][0] + "]* %" + str(fromReg) + ", i64 0, i64 " + str(
            index) + "\n"

        self.register += 1

        return self.register - 1

    def operate(self, operation, num1, num2, type1, type2, isReg1, isReg2,
                LHStype=None):  # num1 = t1, num 2 = t2, operation = see calculations global var

        line = ""
        type = "INT"
        resultReg = "$t0"
        if type1 == "FLOAT" or type2 == "FLOAT":
            type = "FLOAT"
            operation += ".s"

        if LHStype:
            type = LHStype

        if type == "FLOAT":
            resultReg = "$f0"
            # Moest 1 van de 2 types een int zijn moeten we deze eerst nog omzetten naar een float
            if type1 == "INT":
                # Check of het een register is of niet.
                if not isReg1:
                    pass
                else:
                    toReg = self.intToFloat(str(num1))
                    num1 = str(toReg)

                line += "\t" + operation + "\t" + resultReg + "\t," + str(num1) + "," + str(num2) + "\n"

            elif type2 == "INT":
                # Check of het een register is of niet.
                if not isReg2:
                    # num2 = str(num2) + ".0e+00"
                    pass
                else:
                    toReg = self.intToFloat(str(num2))
                    num2 = str(toReg)

                line += "\t" + operation + "\t" + resultReg + "\t," + str(num1) + "," + str(num2) + "\n"

            else:  # Allebei float

                line += "\t" + operation + "\t" + resultReg + "\t," + str(num1) + "," + str(num2) + "\n"

        elif type == "INT":

            if operation == "mfhi":
                line += "\tdiv\t" + str(num1) + "," + str(num2) + " \t#mod\n"
                line += "\tmfhi\t $t6  \t# temp for the mod\n"
                resultReg = "$t6"
            else:
                line += "\t" + operation + "\t" + resultReg + "\t," + str(num1) + "," + str(num2) + "\n"

        return resultReg, type, line

    def compare(self, comparison, num1, num2, type1, type2, isReg1, isReg2, isCondition=False):

        line = ""
        resultReg = "$t0"
        num1 = str(num1)
        num2 = str(num2)

        if type1 == "FLOAT" or type2 == "FLOAT":

            if type1 == "INT":
                num1 = self.intToFloat(num1)

            elif type2 == "INT":
                num2 = self.intToFloat(num2)

            if comparison == "c.gt.s":
                comparison = "c.lt.s"
                temp = num1
                num1 = num2
                num2 = temp
            elif comparison == "c.ge.s":
                comparison = "c.le.s"
                temp = num1
                num1 = num2
                num2 = temp

            label = "__false_" + str(self.compBranchNr) + "__\n"
            line += "\t" + comparison + "\t" + num1 + ", " + num2 + "\n"
            line += "\t" + "bc1f, " + label
            line += "\tli\t" + "$t0, " + "1\n"  # resultReg is t0
            line += "\tb\t" + "__resumeComparison_" + str(self.compBranchNr) + "__\n\n"

            line += "__false_" + str(self.compBranchNr) + "__:\n"
            line += "\tli $t0, 0\n\n"
            line += "__resumeComparison_" + str(self.compBranchNr) + "__:\n"

            self.compBranchNr += 1
        else:
            line += "\t" + comparison + "\t" + resultReg + ", " + num1 + ", " + num2 + "\n"

        if not isCondition and len(self.logicalStack) == 0:
            # Geeft een bool terug dus deze moeten we dan nog omzetten naar een integer, dit moet enkel wanneer we geen conditie hebben
            # Want conditions hebben wel bools nodig
            # line += "  %" + str(self.register) + " = zext i1 %" + str(self.register - 1) + " to i32\n"
            # self.register += 1
            pass

        return resultReg, "INT", line

    def determineBranch(self, node, parent, fromReg):

        # We kijken eerst of we het linkerkind of rechterkind zijn van de node

        if str(parent.parent.value) in logicals:
            if logicals[str(parent.parent.value)] == "NOT":
                self.reverseBool()
                parent.fromRegBrM = "$t0"
                fromReg = "$t0"

        if node == parent.children[0]:
            # Nu kijken we of de parent een OR of AND is
            if logicals[str(parent.value)] == "AND":
                # Als dit een AND is gaan we met een True naar het rechterkind en met een False niet
                # Omdat het rechterkind ook hierna komt gaan we dan ook direct de branch hiervoor maken

                # Voor het falseLabel moeten we nog kijken wat de parent zijn parent is
                # Als dit een and is en de parent is zijn rechterkind pakken we het falseLabel van die and
                if str(parent.parent.value) in logicals:

                    if parent == parent.parent.children[0]:
                        if logicals[str(parent.parent.value)] == "AND":
                            node.falseLabelM = parent.parent.falseLabelM

                        elif logicals[str(parent.parent.value)] == "NOT":
                            node.falseLabelM = self.logLabelCount
                            self.logLabelCount += 1

                        else:
                            node.falseLabelM = self.logLabelCount
                            self.logLabelCount += 1
                    else:
                        node.falseLabelM = parent.falseLabelM

                else:
                    node.falseLabelM = self.logLabelCount
                    self.logLabelCount += 1

                node.trueLabelM = self.logLabelCount
                self.logLabelCount += 1

                # TODO: aanpassing
                if str(node.value) in data_comp_instr and str(parent.value) in logicals:
                    # if str(parent.value) in comparisons and str(parent.value.value) not in logicals:
                    self.branch(fromReg, node.trueLabelM, node.falseLabelM, node.trueLabelM, "x")
                    self.line = self.line.replace("x" + str(node.trueLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1

                elif (str(node.token) == "IDENTIFIER" or str(node.token) in types):
                    self.branch(fromReg, node.trueLabelM, node.falseLabelM, node.trueLabelM, "x")
                    self.line = self.line.replace("x" + str(node.trueLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1

                else:
                    self.isComparison = True

                # We stellen de parent zijn falseLabel ook gelijk aan dit van deze node
                parent.falseLabelM = node.falseLabelM

            elif logicals[str(parent.value)] == "OR":
                # Als dit een OR is gaan we met een False naar het rechterkind en met een True niet
                # Omdat het rechterkind ook hierna komt gaan we dan ook direct de branch hiervoor maken

                # Bepalen van het true of false label
                if str(parent.parent.value) in logicals:

                    if parent == parent.parent.children[0]:
                        if logicals[str(parent.parent.value)] == "OR":
                            node.trueLabelM = parent.parent.trueLabelM

                        elif logicals[str(parent.parent.value)] == "NOT":
                            node.trueLabelM = self.logLabelCount
                            self.logLabelCount += 1

                        else:
                            node.trueLabelM = self.logLabelCount
                            self.logLabelCount += 1

                    else:
                        node.trueLabelM = parent.trueLabelM
                else:
                    node.trueLabelM = self.logLabelCount
                    self.logLabelCount += 1

                node.falseLabelM = self.logLabelCount
                self.logLabelCount += 1

                # TODO: aanpassing
                if str(node.value) in data_comp_instr and str(parent.value) in logicals:
                    # if str(parent.value) in comparisons and str(parent.value.value) not in logicals:
                    self.branch(fromReg, node.trueLabelM, node.falseLabelM, node.falseLabelM, "x")
                    self.line = self.line.replace("x" + str(node.falseLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1

                elif (str(node.token) == "IDENTIFIER" or str(node.token) in types):
                    self.branch(fromReg, node.trueLabelM, node.falseLabelM, node.falseLabelM, "x")
                    self.line = self.line.replace("x" + str(node.falseLabelM), "__label_" + str(self.labelCount) + "__")
                    self.labelCount += 1

                else:
                    self.isComparison = True

                # We stellen de parent zijn trueLabel gelijk aan dit van deze node
                parent.trueLabelM = node.trueLabelM

            elif logicals[str(parent.value)] == "NOT":
                self.reverseBool()
                parent.fromRegBrM = "$t0"

                if str(parent.parent.value) not in logicals:
                    node.trueLabelM = self.logLabelCount
                    self.logLabelCount += 1
                    node.falseLabelM = self.logLabelCount
                    self.logLabelCount += 1
                    parent.trueLabelM = node.trueLabelM
                    parent.falseLabelM = node.falseLabelM


        elif node == parent.children[1]:
            if logicals[str(parent.value)] == "AND":
                # Als dit een AND is gaan we de false van deze node gelijk stellen aan die van het linkerkind
                # en gaan we de True als nieuwLabel maken

                # Voor het trueLabel moeten we nog kijken wat de parent zijn parent is
                # Als dit een or is en de parent is zijn rechterkind pakken we het trueLabel van die or
                if str(parent.parent.value) in logicals:
                    if logicals[str(parent.parent.value)] == "OR" and parent == parent.parent.children[1]:
                        node.trueLabelM = parent.parent.trueLabelM
                    else:
                        node.trueLabelM = self.logLabelCount
                        self.logLabelCount += 1
                else:
                    node.trueLabelM = self.logLabelCount
                    self.logLabelCount += 1

                node.falseLabelM = parent.falseLabelM
                # We stellen nu ook de parent zijn trueLabel in
                parent.trueLabelM = node.trueLabelM

                parent.fromRegBrM = fromReg

                # We gaan hierna een exit doen, dus we behandelen dan dit geval verder in de log node zelf

            elif logicals[str(parent.value)] == "OR":
                # Als dit een OR is gaan we de true van deze node gelijk stellen aan die van het linkerkind
                # en gaan we de False als nieuwLabel maken

                node.trueLabelM = parent.trueLabelM
                # Voor het falseLabel moeten we nog kijken wat de parent zijn parent is
                # Als dit een and is en de parent is zijn rechterkind pakken we het falseLabel van die and
                if str(parent.parent.value) in logicals:
                    # Als de parent zijn parent een AND is en de parent is zijn rechterkind nemen we deze label over
                    if logicals[str(parent.parent.value)] == "AND" and parent == parent.parent.children[1]:
                        node.falseLabelM = parent.parent.falseLabelM
                    # Anders maken we een nieuw label aan omdat onze parent een or is
                    else:
                        node.falseLabelM = self.logLabelCount
                        self.logLabelCount += 1
                else:
                    node.falseLabelM = self.logLabelCount
                    self.logLabelCount += 1
                # We stellen nu ook de parent zijn falseLabel in
                parent.falseLabelM = node.falseLabelM

                parent.fromRegBrM = fromReg

                # We gaan hierna een exit doen, dus we behandelen dan dit geval verder in de log node zelf

    def branch(self, boolean, left, right, next, symbol):
        # self.line += "  br i1 %" + str(boolean) + ", label %" + symbol + str(left) + ", label %" + symbol + str(
        #     right) + "\n\n"
        # self.line += symbol + str(next) + ":\n"

        self.line += "\tbeq\t" + str(boolean) + ", 1, " + symbol + str(left) + "\n"
        self.line += "\tbeq\t" + str(boolean) + ", 0, " + symbol + str(right) + "\n\n"

        self.line += symbol + str(next) + ":\n"

    def floatToInt(self, reg):
        # self.line += "  %" + str(self.register) + " = fptosi float %" + str(reg) + " to i32\n"
        # self.register += 1
        self.line += "\tcvt.w.s\t" + reg + "," + reg + "\n" + \
                     "\tmfc1\t" + "$t0" + "," + reg + "\n"
        return "$t0"

    def intToFloat(self, reg):
        # self.line += "  %" + str(self.register) + " = sitofp i32 %" + str(reg) + " to float\n"
        # self.register += 1

        self.line += "\tmtc1\t" + reg + ", $f6\n" + \
                     "\tcvt.s.w\t $f6, $f6\n"
        return "$f6"

    def noReturn(self):
        self.line += "  %" + str(self.register) + " = alloca " + types[self.returnType][0] + ", " + \
                     types[self.returnType][1] + "\n"
        # TODO: dit is maar iets raars wat ik hier heb gedaan, nog eens bekijken op deze gevallen
        # self.register += 1
        # self.line += "  %" + str(self.register) + " = load " + types[self.returnType][0] + ", " + \
        #              types[self.returnType][0] + "* %" + str(self.register - 1) + ", " + types[self.returnType][
        #                  1] + "\n"
        self.hasReturnNode = (False, self.register)
        self.register += 1

    def loadInReg(self, value, type1):

        toReg = None
        line = ""

        if type1 != "FLOAT":  # int or char

            line += "\tli\t" + "$t0, " + str(value) + "\n"
            toReg = "$t0"

        else:

            floatName = "fl" + str(self.floatCount)
            isDuplicateFloatName = False
            for i in range(len(self.floats)):
                if self.floats[i][1] == str(value):
                    isDuplicateFloatName = True
                    floatName = self.floats[i][0]
                    break
            if not isDuplicateFloatName:
                self.floats.append((floatName, str(value)))
                self.floatCount += 1

                globalvar = str(floatName) + ":" + "\t" + "." + global_types[type1] + "\t" + str(value) + "\n"
                self.globals.append(globalvar)

            line = "\tl.s\t" + "$f0, " + floatName + "\n"

            toReg = "$f0"

        return toReg, line

    def exitTypeStackHandler(self, stack, node):
        toReg, line = self.loadInReg(node.value, node.token)
        self.line += line
        self.store(toReg, self.offset)
        stack.append((self.offset, node.token, True))
        self.offset -= 4
        return toReg, node.type

    def exitIdentifierStackHandler(self, stack, symbol_lookup, function):
        reg, type = function(symbol_lookup)
        self.line += reg[1]
        self.store(reg[0], self.offset)

        if not self.enteredScanf:
            stack.append((self.offset, type, True))  # Ook hier heeft de functioncall voorang

        else:
            stack.append((symbol_lookup.stackOffset, type, True))  # Ook hier heeft de functioncall voorang

        self.offset -= 4
        return type, reg[0]

    def exitBinOperationStackHandler(self, stack, node, function, LHStype):

        reg1 = '$t0' if stack[-2][1] != "FLOAT" else '$f0'
        reg2 = '$t1' if stack[-1][1] != "FLOAT" else '$f1'

        reg1, line = self.load(stack[-2][0], stack[-2][1], reg1)
        self.line += line

        reg2, line = self.load(stack[-1][0], stack[-1][1], reg2)
        self.line += line

        toReg, toType, line = function(node, stack, reg1, reg2, LHStype)
        self.line += line

        stack.pop()
        stack.pop()
        self.offset += 8

        self.store(toReg, self.offset)

        stack.append((self.offset, toType, True))
        self.offset -= 4
        return toType, toReg

    def exitComparisonStackHandler(self, stack, node, function, condition):
        reg1 = '$t0' if stack[-2][1] != "FLOAT" else '$f0'
        reg2 = '$t1' if stack[-1][1] != "FLOAT" else '$f1'

        reg1, line = self.load(stack[-2][0], stack[-2][1], reg1)
        self.line += line

        reg2, line = self.load(stack[-1][0], stack[-1][1], reg2)
        self.line += line

        toReg, toType, line = function(node, stack, condition, reg1, reg2)
        self.line += line

        stack.pop()
        stack.pop()
        self.offset += 8

        self.store(toReg, self.offset)

        stack.append((self.offset, toType, True))
        self.offset -= 4
        return toType, toReg

    def reverseBool(self):

        self.line += "\tbeq\t$t0, 0, __reverse_" + str(self.reverseCount) + "__\n"
        self.line += "\tli\t$t0, 0\n"
        self.line += "\tb __continue_" + str(self.reverseCount) + "__\n\n"
        self.line += "__reverse_" + str(self.reverseCount) + "__:\n"
        self.line += "\tli\t$t0, 1\n"
        self.line += "\tb __continue_" + str(self.reverseCount) + "__\n\n"
        self.line += "__continue_" + str(self.reverseCount) + "__:\n"
        self.reverseCount += 1

    def popRightStack(self):
        if self.enteredFunctionCall > 0:
            self.functionCallStack.pop()

        elif self.enteredReturn:
            self.returnStack.pop()

        elif self.enteredPrintf:
            self.printfStack.pop()

        elif self.enteredCondition:
            self.conditionStack.pop()

        elif self.enteredAssignment:
            self.assignmentStack.pop()

    def writeToFile(self, inputfile):
        afterSlash = re.search("[^/]+$", inputfile)
        pos = afterSlash.start()
        inputfile = inputfile[pos:]
        filename = str(inputfile[:len(inputfile) - 2]) + ".asm"
        # self.file = open("files/GeneratedMIPS/" + filename, "w")
        file = open("testfiles/generated/" + filename, "w")

        file.write(".data")
        file.write("\n")

        for global_ in self.globals:
            file.write(global_)

        if self.printf:
            self.strings.sort(key=lambda x: x[1])
            for string in self.strings:
                # str_ = "@.str" + str(string[1]) if int(string[1]) > 0 else "@.str"
                # line = str_ + " = private unnamed_addr constant " + inbound + " c\"" + str(string[2]) + "\", align 1\n"
                if string[0] != 0:
                    name = "str" + string[
                        1]  # TODO naam verkrijgen (moet normaal op het moment dat we de printf zelf tegenkomen gemaakt worden) + stringvorm
                    str_ = name + ":\t"
                    line = str_ + "." + "asciiz\t" + str(string[2]) + "\n"
                    file.write(line)

        file.write("\n")
        file.write(".text")
        file.write("\n")
        file.write(self.line)

        # if self.printf:
        #     file.write("declare dso_local i32 @printf(i8*, ...)\n")
        # if self.scanf:
        #     file.write("declare dso_local i32 @__isoc99_scanf(i8*, ...)\n")

        exit = "exit:\n\t" + "li $v0, 10\n\t" + "syscall"
        file.write(exit)

        file.close()
