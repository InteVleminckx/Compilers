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
    print(a)


if __name__ == '__main__':
    main(sys.argv)