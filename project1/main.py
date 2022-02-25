import sys
from antlr4 import *
from mathGrammerLexer import mathGrammerLexer
from mathGrammerParser import mathGrammerParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = mathGrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathGrammerParser(stream)
    tree = parser.startRule()


if __name__ == '__main__':
    main(sys.argv)