import sys
from antlr4 import *
from mathGrammerLexer import mathGrammerLexer
from mathGrammerParser import mathGrammerParser
from AST import *

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
    # print("\n")
    # print(a.root.getToken())
    # print(a.root.getValue())
    # print("\n")
    # for child in a.children:
    #     print("child:")
    #     print(child.root.getToken())
    #     print(child.root.getValue())
    #     if len(child.children):
    #         for child1 in child.children:
    #             print("child2:")
    #             print(child1.root.getToken())
    #             print(child1.root.getValue())


if __name__ == '__main__':
    main(sys.argv)