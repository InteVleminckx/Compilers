from AST import *
from Mips import Mips
from LLVM import LLVM


class CodeGeneration:

    def __init__(self, tree):
        self.tree = tree
        self.llvm = LLVM()
        self.mips = Mips()

    def generateCode(self, inputfile):

        if self.tree.root is None:
            return

        self.convert(self.tree.root)

        self.llvm.writeToFile(inputfile)

    def convert(self, node):

        self.EnterExitstatements(node, enter=True)
        for i, child in enumerate(node.children):
            self.convert(child)

        self.EnterExitstatements(node, enter=False)

    def EnterExitstatements(self, node, enter):
        if node.parent is not None:
            if node.parent.token == "ROOT" and node.token == "=":
                return

        print(node.token)

        if node.token == "FUNC_DEF":
            if enter:
                self.llvm.enterFunction(node)
                self.mips.enterFunction(node)
            else:
                self.llvm.exitFunction(node)
                self.mips.exitFunction(node)

        elif node.token == "RETURN":
            if enter:
                self.llvm.enterReturn(node)
                self.mips.enterReturn(node)
            else:
                self.llvm.exitReturn(node)
                self.mips.exitReturn(node)
        elif node.token == "PRINTF":
            if enter:
                self.llvm.enterPrintf(node)
                self.mips.enterPrintf(node)
            else:
                self.llvm.exitPrintf(node)
                self.mips.exitPrintf(node)
        elif node.token == "SCANF":
            if enter:
                self.llvm.enterScanf(node)
                self.mips.enterScanf(node)
            else:
                self.llvm.exitScanf(node)
                self.mips.exitScanf(node)
        elif node.token == "IF":
            if enter:
                self.llvm.enterIf_stmt(node)
                self.mips.enterIf_stmt(node)
            else:
                self.llvm.exitIf_stmt(node)
                self.mips.exitIf_stmt(node)
        elif node.token == "ELSE":
            if enter:
                self.llvm.enterElse_stmt(node)
                self.mips.enterElse_stmt(node)
            else:
                self.llvm.exitElse_stmt(node)
                self.mips.exitElse_stmt(node)
        elif node.token == "WHILE":
            if enter:
                self.llvm.enterWhile_stmt(node)
                self.mips.enterWhile_stmt(node)
            else:
                self.llvm.exitWhile_stmt(node)
                self.mips.exitWhile_stmt(node)
        elif node.token == "=":
            if enter:
                self.llvm.enterAssignment(node)
                self.mips.enterAssignment(node)
            else:
                self.llvm.exitAssignment(node)
                self.mips.exitAssignment(node)
        elif node.token == "UN_OP":
            if enter:
                self.llvm.enterUnaryOperation(node)
                self.mips.enterUnaryOperation(node)
            else:
                self.llvm.exitUnaryOperation(node)
                self.mips.exitUnaryOperation(node)
        elif node.token == "BREAK":
            if enter:
                self.llvm.enterBreak(node)
                self.mips.enterBreak(node)
            else:
                self.llvm.exitBreak(node)
                self.mips.exitBreak(node)
        elif node.token == "CONTINUE":
            if enter:
                self.llvm.enterContinue(node)
                self.mips.enterContinue(node)
            else:
                self.llvm.exitContinue(node)
                self.mips.exitContinue(node)

        elif node.token == "FUNC_CALL":
            if enter:
                self.llvm.enterFuncCall(node)
                self.mips.enterFuncCall(node)
            else:
                self.llvm.exitFuncCall(node)
                self.mips.exitFuncCall(node)

        elif node.token == "BIN_OP1" or node.token == "BIN_OP2":
            if enter:
                self.llvm.enterBinOperation(node)
                self.mips.enterBinOperation(node)
            else:
                self.llvm.exitBinOperation(node)
                self.mips.exitBinOperation(node)
        elif node.token == "IDENTIFIER":
            if enter:
                self.llvm.enterIdentifier(node)
                self.mips.enterIdentifier(node)
            else:
                self.llvm.exitIdentifier(node)
                self.mips.exitIdentifier(node)

        elif node.token == "INT" or node.token == "FLOAT" or node.token == "CHAR":
            if enter:
                self.llvm.enterType(node)
                self.mips.enterType(node)
            else:
                self.llvm.exitType(node)
                self.mips.exitType(node)

        elif node.token == "STRING" or node.token == "PRINTTEXT":
            if enter:
                self.llvm.enterString(node)
                self.mips.enterString(node)
            else:
                self.llvm.exitString(node)
                self.mips.exitString(node)

        elif node.token == "COMP_OP" or node.token == "EQ_OP":
            if enter:
                self.llvm.enterComparison(node)
                self.mips.enterComparison(node)
            else:
                self.llvm.exitComparison(node)
                self.mips.exitComparison(node)

        elif node.token == "LOG_OR" or node.token == "LOG_AND" or node.token == "LOG_NOT":
            if enter:
                self.llvm.enterLogical(node)
                self.mips.enterLogical(node)
            else:
                self.llvm.exitLogical(node)
                self.mips.exitLogical(node)

        elif node.token == "CONDITION":
            if enter:
                self.llvm.enterCondition(node)
                self.mips.enterCondition(node)
            else:
                self.llvm.exitCondition(node)
                self.mips.exitCondition(node)

        elif node.token == "ARRAY":
            if enter:
                self.llvm.enterArray(node)
                self.mips.enterArray(node)
            else:
                self.llvm.exitArray(node)
                self.mips.exitArray(node)


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
