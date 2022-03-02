import sys
from antlr4 import *
from mathGrammerLexer import mathGrammerLexer
from mathGrammerParser import mathGrammerParser
from AST import *


def printA(a, root):

    if root and root is not None:
        if len(a.root.children) != 0:
            for i in range(len(a.root.children)):
                if i == 1:
                    print(a.root.value)

                printA(a.root.children[i], False)
        else:
            print(a.root.value)

    elif a is not None:
        if len(a.children) != 0:
            for i in range(len(a.children)):

                if i == 1:
                    print(a.value)

                printA(a.children[i], False)

        else:
            print(a.value)


def main(argv):

    input_stream = FileStream(argv[1])
    lexer = mathGrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathGrammerParser(stream)
    tree = parser.math()
    printer = ASTprinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    a = ast
    # print("-------------------------------------------------")
    # printA(a,True)
    # a.inorderTraversal(print)
    # print("-------------------------------------------------")

    createGraph(a)



if __name__ == '__main__':
    main(sys.argv)