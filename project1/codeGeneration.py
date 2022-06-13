from AST import *
from Mips import Mips
from LLVM import LLVM


class CodeGeneration:

    def __init__(self, tree, llvm):
        self.tree = tree
        self.llvm = LLVM()
        self.enterdForwardDecl = False
        self.mips = Mips()
        self.isLLVM = llvm

    def generateCode(self, inputfile):
        # print(self.isLLVM)
        if self.tree.root is None:
            return

        self.convert(self.tree.root)
        if self.isLLVM == 'True':

            self.llvm.writeToFile(inputfile)

        else:

            self.mips.writeToFile(inputfile)

    def convert(self, node):

        self.EnterExitstatements(node, enter=True)
        for i, child in enumerate(node.children):
            self.convert(child)

        self.EnterExitstatements(node, enter=False)

    def EnterExitstatements(self, node, enter):
        if node.parent is not None:
            if node.parent.token == "ROOT" and node.token == "=":
                return

        # print(node.token)

        if node.token == "FORDECL":
            if enter:
                self.enterdForwardDecl = True
            else:
                self.enterdForwardDecl = False

        #We kunnen alles skippen want dit is niet nodig op te genereren
        if self.enterdForwardDecl:
            return

        if node.token == "FUNC_DEF":
            if enter:
                self.llvm.enterFunction(node) if self.isLLVM else self.mips.enterFunction(node)

            else:
                self.llvm.exitFunction(node) if self.isLLVM else self.mips.exitFunction(node)


        elif node.token == "RETURN":
            if enter:
                self.llvm.enterReturn(node) if self.isLLVM else self.mips.enterReturn(node)

            else:
                self.llvm.exitReturn(node) if self.isLLVM else self.mips.exitReturn(node)

        elif node.token == "PRINTF":
            if enter:
                self.llvm.enterPrintf(node) if self.isLLVM else self.mips.enterPrintf(node)

            else:
                self.llvm.exitPrintf(node) if self.isLLVM else self.mips.exitPrintf(node)

        elif node.token == "SCANF":
            if enter:
                self.llvm.enterScanf(node) if self.isLLVM else self.mips.enterScanf(node)

            else:
                self.llvm.exitScanf(node) if self.isLLVM else self.mips.exitScanf(node)

        elif node.token == "IF":
            if enter:
                self.llvm.enterIf_stmt(node) if self.isLLVM else self.mips.enterIf_stmt(node)

            else:
                self.llvm.exitIf_stmt(node) if self.isLLVM else self.mips.exitIf_stmt(node)

        elif node.token == "ELSE":
            if enter:
                self.llvm.enterElse_stmt(node) if self.isLLVM else self.mips.enterElse_stmt(node)

            else:
                self.llvm.exitElse_stmt(node) if self.isLLVM else self.mips.exitElse_stmt(node)

        elif node.token == "WHILE":
            if enter:
                self.llvm.enterWhile_stmt(node) if self.isLLVM else self.mips.enterWhile_stmt(node)

            else:
                self.llvm.exitWhile_stmt(node) if self.isLLVM else self.mips.exitWhile_stmt(node)

        elif node.token == "=":
            if enter:
                self.llvm.enterAssignment(node) if self.isLLVM else self.mips.enterAssignment(node)

            else:
                self.llvm.exitAssignment(node) if self.isLLVM else self.mips.exitAssignment(node)

        elif node.token == "UN_OP":
            if enter:
                self.llvm.enterUnaryOperation(node) if self.isLLVM else self.mips.enterUnaryOperation(node)

            else:
                self.llvm.exitUnaryOperation(node) if self.isLLVM else self.mips.exitUnaryOperation(node)

        elif node.token == "BREAK":
            if enter:
                self.llvm.enterBreak(node) if self.isLLVM else self.mips.enterBreak(node)

            else:
                self.llvm.exitBreak(node) if self.isLLVM else self.mips.exitBreak(node)

        elif node.token == "CONTINUE":
            if enter:
                self.llvm.enterContinue(node) if self.isLLVM else self.mips.enterContinue(node)

            else:
                self.llvm.exitContinue(node) if self.isLLVM else self.mips.exitContinue(node)


        elif node.token == "FUNC_CALL":
            if enter:
                self.llvm.enterFuncCall(node) if self.isLLVM else self.mips.enterFuncCall(node)

            else:
                self.llvm.exitFuncCall(node) if self.isLLVM else self.mips.exitFuncCall(node)


        elif node.token == "BIN_OP1" or node.token == "BIN_OP2":
            if enter:
                self.llvm.enterBinOperation(node) if self.isLLVM else self.mips.enterBinOperation(node)

            else:
                self.llvm.exitBinOperation(node) if self.isLLVM else self.mips.exitBinOperation(node)

        elif node.token == "IDENTIFIER":
            if enter:
                self.llvm.enterIdentifier(node) if self.isLLVM else self.mips.enterIdentifier(node)

            else:
                self.llvm.exitIdentifier(node) if self.isLLVM else self.mips.exitIdentifier(node)


        elif node.token == "INT" or node.token == "FLOAT" or node.token == "CHAR":
            if enter:
                self.llvm.enterType(node) if self.isLLVM else self.mips.enterType(node)

            else:
                self.llvm.exitType(node) if self.isLLVM else self.mips.exitType(node)


        elif node.token == "STRING" or node.token == "PRINTTEXT":
            if enter:
                self.llvm.enterString(node) if self.isLLVM else self.mips.enterString(node)

            else:
                self.llvm.exitString(node) if self.isLLVM else self.mips.exitString(node)


        elif node.token == "COMP_OP" or node.token == "EQ_OP":
            if enter:
                self.llvm.enterComparison(node) if self.isLLVM else self.mips.enterComparison(node)

            else:
                self.llvm.exitComparison(node) if self.isLLVM else self.mips.exitComparison(node)


        elif node.token == "LOG_OR" or node.token == "LOG_AND" or node.token == "LOG_NOT":
            if enter:
                self.llvm.enterLogical(node) if self.isLLVM else self.mips.enterLogical(node)

            else:
                self.llvm.exitLogical(node) if self.isLLVM else self.mips.exitLogical(node)


        elif node.token == "CONDITION":
            if enter:
                self.llvm.enterCondition(node) if self.isLLVM else self.mips.enterCondition(node)

            else:
                self.llvm.exitCondition(node) if self.isLLVM else self.mips.exitCondition(node)


        elif node.token == "ARRAY":
            if enter:
                self.llvm.enterArray(node) if self.isLLVM else self.mips.enterArray(node)

            else:
                self.llvm.exitArray(node) if self.isLLVM else self.mips.exitArray(node)


        elif node.token == "INDICES":
            if enter:
                self.llvm.enterIndices(node) if self.isLLVM else self.mips.enterIndices(node)

            else:
                self.llvm.exitIndices(node) if self.isLLVM else self.mips.exitIndices(node)





# def getSymbolFromTable( if self.isLLVM else self.mips.exitIndices(node)node):
#     searchNode = node
#
#     symbolValue = None
#     name = None
#     if node.token == "IDENTIFIER":
#         while symbolValue is None:
#
#             while searchNode.symbolTablePointer is None:
#                 searchNode = searchNode.parent
#
#             table = searchNode.symbolTablePointer.dict
#
#             for key in table:
#                 if str(key) == str(node.value):
#                     symbolValue = table[key]
#                     name = str(key)
#                     break
#
#             if symbolValue is None:
#                 searchNode = searchNode.parent
#
#     return symbolValue, name
