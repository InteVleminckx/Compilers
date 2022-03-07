# Generated from mathGrammer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\67\n\13\3\f\3\f\3\f\3\f\5\f=\n\f\3\r\6\r@\n\r")
        buf.write("\r\r\16\rA\3\16\6\16E\n\16\r\16\16\16F\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\3\2\6\5\2\'\',,\61\61\4\2>>@@\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2")
        buf.write("\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2\2\21,")
        buf.write("\3\2\2\2\23/\3\2\2\2\25\66\3\2\2\2\27<\3\2\2\2\31?\3\2")
        buf.write("\2\2\33D\3\2\2\2\35\36\7=\2\2\36\4\3\2\2\2\37 \7*\2\2")
        buf.write(" \6\3\2\2\2!\"\7+\2\2\"\b\3\2\2\2#$\t\2\2\2$\n\3\2\2\2")
        buf.write("%&\7-\2\2&\f\3\2\2\2\'(\7/\2\2(\16\3\2\2\2)*\7~\2\2*+")
        buf.write("\7~\2\2+\20\3\2\2\2,-\7(\2\2-.\7(\2\2.\22\3\2\2\2/\60")
        buf.write("\7#\2\2\60\24\3\2\2\2\61\67\t\3\2\2\62\63\7>\2\2\63\67")
        buf.write("\7?\2\2\64\65\7@\2\2\65\67\7?\2\2\66\61\3\2\2\2\66\62")
        buf.write("\3\2\2\2\66\64\3\2\2\2\67\26\3\2\2\289\7?\2\29=\7?\2\2")
        buf.write(":;\7#\2\2;=\7?\2\2<8\3\2\2\2<:\3\2\2\2=\30\3\2\2\2>@\t")
        buf.write("\4\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\32\3\2")
        buf.write("\2\2CE\t\5\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("GH\3\2\2\2HI\b\16\2\2I\34\3\2\2\2\7\2\66<AF\3\b\2\2")
        return buf.getvalue()


class mathGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    BIN_OP2 = 4
    PLUS = 5
    MIN = 6
    LOG_OR = 7
    LOG_AND = 8
    LOG_NOT = 9
    COMP_OP = 10
    EQ_OP = 11
    INT = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'", "'+'", "'-'", "'||'", "'&&'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "BIN_OP2", "PLUS", "MIN", "LOG_OR", "LOG_AND", "LOG_NOT", "COMP_OP", 
            "EQ_OP", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BIN_OP2", "PLUS", "MIN", "LOG_OR", 
                  "LOG_AND", "LOG_NOT", "COMP_OP", "EQ_OP", "INT", "WS" ]

    grammarFileName = "mathGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


