# Generated from .\mathGrammer.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\34\n\2\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\62\n\5\f\5\16")
        buf.write("\5\65\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16\6@")
        buf.write("\13\6\3\7\3\7\3\7\5\7E\n\7\3\b\3\b\3\b\7\bJ\n\b\f\b\16")
        buf.write("\bM\13\b\3\t\3\t\3\t\7\tR\n\t\f\t\16\tU\13\t\3\n\3\n\3")
        buf.write("\n\5\nZ\n\n\3\13\3\13\3\13\3\13\3\13\5\13a\n\13\3\13\2")
        buf.write("\4\b\n\f\2\4\6\b\n\f\16\20\22\24\2\2\2b\2\33\3\2\2\2\4")
        buf.write("\"\3\2\2\2\6)\3\2\2\2\b+\3\2\2\2\n\66\3\2\2\2\fD\3\2\2")
        buf.write("\2\16F\3\2\2\2\20N\3\2\2\2\22Y\3\2\2\2\24`\3\2\2\2\26")
        buf.write("\27\5\16\b\2\27\30\7\3\2\2\30\31\5\2\2\2\31\34\3\2\2\2")
        buf.write("\32\34\7\2\2\3\33\26\3\2\2\2\33\32\3\2\2\2\34\3\3\2\2")
        buf.write("\2\35\36\5\6\4\2\36\37\7\f\2\2\37 \5\6\4\2 #\3\2\2\2!")
        buf.write("#\5\6\4\2\"\35\3\2\2\2\"!\3\2\2\2#\5\3\2\2\2$%\5\b\5\2")
        buf.write("%&\7\13\2\2&\'\5\b\5\2\'*\3\2\2\2(*\5\b\5\2)$\3\2\2\2")
        buf.write(")(\3\2\2\2*\7\3\2\2\2+,\b\5\1\2,-\5\n\6\2-\63\3\2\2\2")
        buf.write("./\f\4\2\2/\60\7\t\2\2\60\62\5\n\6\2\61.\3\2\2\2\62\65")
        buf.write("\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\t\3\2\2\2\65\63")
        buf.write("\3\2\2\2\66\67\b\6\1\2\678\5\f\7\28>\3\2\2\29:\f\4\2\2")
        buf.write(":;\7\n\2\2;=\5\f\7\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3")
        buf.write("\2\2\2?\13\3\2\2\2@>\3\2\2\2AB\7\r\2\2BE\5\f\7\2CE\5\24")
        buf.write("\13\2DA\3\2\2\2DC\3\2\2\2E\r\3\2\2\2FK\5\20\t\2GH\7\4")
        buf.write("\2\2HJ\5\20\t\2IG\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2")
        buf.write("\2L\17\3\2\2\2MK\3\2\2\2NS\5\22\n\2OP\7\5\2\2PR\5\22\n")
        buf.write("\2QO\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\21\3\2\2\2")
        buf.write("US\3\2\2\2VW\7\6\2\2WZ\5\22\n\2XZ\5\4\3\2YV\3\2\2\2YX")
        buf.write("\3\2\2\2Z\23\3\2\2\2[a\7\16\2\2\\]\7\7\2\2]^\5\b\5\2^")
        buf.write("_\7\b\2\2_a\3\2\2\2`[\3\2\2\2`\\\3\2\2\2a\25\3\2\2\2\f")
        buf.write("\33\")\63>DKSY`")
        return buf.getvalue()


class mathGrammerParser ( Parser ):

    grammarFileName = "mathGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'||'", "'&&'", "'!'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BIN_OP1", 
                      "BIN_OP2", "COMP_OP", "EQ_OP", "UN_OP", "INT", "WS" ]

    RULE_math = 0
    RULE_comp_expr = 1
    RULE_comp_expr1 = 2
    RULE_expr = 3
    RULE_factor = 4
    RULE_term = 5
    RULE_log_op1 = 6
    RULE_log_op2 = 7
    RULE_log_op3 = 8
    RULE_var = 9

    ruleNames =  [ "math", "comp_expr", "comp_expr1", "expr", "factor", 
                   "term", "log_op1", "log_op2", "log_op3", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    BIN_OP1=7
    BIN_OP2=8
    COMP_OP=9
    EQ_OP=10
    UN_OP=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_op1(self):
            return self.getTypedRuleContext(mathGrammerParser.Log_op1Context,0)


        def math(self):
            return self.getTypedRuleContext(mathGrammerParser.MathContext,0)


        def EOF(self):
            return self.getToken(mathGrammerParser.EOF, 0)

        def getRuleIndex(self):
            return mathGrammerParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = mathGrammerParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_math)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.T__3, mathGrammerParser.T__4, mathGrammerParser.UN_OP, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.log_op1()
                self.state = 21
                self.match(mathGrammerParser.T__0)
                self.state = 22
                self.math()
                pass
            elif token in [mathGrammerParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(mathGrammerParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp_expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathGrammerParser.Comp_expr1Context)
            else:
                return self.getTypedRuleContext(mathGrammerParser.Comp_expr1Context,i)


        def EQ_OP(self):
            return self.getToken(mathGrammerParser.EQ_OP, 0)

        def getRuleIndex(self):
            return mathGrammerParser.RULE_comp_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_expr" ):
                listener.enterComp_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_expr" ):
                listener.exitComp_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_expr" ):
                return visitor.visitComp_expr(self)
            else:
                return visitor.visitChildren(self)




    def comp_expr(self):

        localctx = mathGrammerParser.Comp_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comp_expr)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.comp_expr1()
                self.state = 28
                self.match(mathGrammerParser.EQ_OP)
                self.state = 29
                self.comp_expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.comp_expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathGrammerParser.ExprContext)
            else:
                return self.getTypedRuleContext(mathGrammerParser.ExprContext,i)


        def COMP_OP(self):
            return self.getToken(mathGrammerParser.COMP_OP, 0)

        def getRuleIndex(self):
            return mathGrammerParser.RULE_comp_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_expr1" ):
                listener.enterComp_expr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_expr1" ):
                listener.exitComp_expr1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_expr1" ):
                return visitor.visitComp_expr1(self)
            else:
                return visitor.visitChildren(self)




    def comp_expr1(self):

        localctx = mathGrammerParser.Comp_expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comp_expr1)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(mathGrammerParser.COMP_OP)
                self.state = 36
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(mathGrammerParser.FactorContext,0)


        def expr(self):
            return self.getTypedRuleContext(mathGrammerParser.ExprContext,0)


        def BIN_OP1(self):
            return self.getToken(mathGrammerParser.BIN_OP1, 0)

        def getRuleIndex(self):
            return mathGrammerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathGrammerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mathGrammerParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 44
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 45
                    self.match(mathGrammerParser.BIN_OP1)
                    self.state = 46
                    self.factor(0) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(mathGrammerParser.TermContext,0)


        def factor(self):
            return self.getTypedRuleContext(mathGrammerParser.FactorContext,0)


        def BIN_OP2(self):
            return self.getToken(mathGrammerParser.BIN_OP2, 0)

        def getRuleIndex(self):
            return mathGrammerParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathGrammerParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mathGrammerParser.FactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 55
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 56
                    self.match(mathGrammerParser.BIN_OP2)
                    self.state = 57
                    self.term() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UN_OP(self):
            return self.getToken(mathGrammerParser.UN_OP, 0)

        def term(self):
            return self.getTypedRuleContext(mathGrammerParser.TermContext,0)


        def var(self):
            return self.getTypedRuleContext(mathGrammerParser.VarContext,0)


        def getRuleIndex(self):
            return mathGrammerParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = mathGrammerParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.UN_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(mathGrammerParser.UN_OP)
                self.state = 64
                self.term()
                pass
            elif token in [mathGrammerParser.T__4, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_op1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_op2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathGrammerParser.Log_op2Context)
            else:
                return self.getTypedRuleContext(mathGrammerParser.Log_op2Context,i)


        def getRuleIndex(self):
            return mathGrammerParser.RULE_log_op1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_op1" ):
                listener.enterLog_op1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_op1" ):
                listener.exitLog_op1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_op1" ):
                return visitor.visitLog_op1(self)
            else:
                return visitor.visitChildren(self)




    def log_op1(self):

        localctx = mathGrammerParser.Log_op1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_log_op1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.log_op2()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.T__1:
                self.state = 69
                self.match(mathGrammerParser.T__1)
                self.state = 70
                self.log_op2()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_op2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_op3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathGrammerParser.Log_op3Context)
            else:
                return self.getTypedRuleContext(mathGrammerParser.Log_op3Context,i)


        def getRuleIndex(self):
            return mathGrammerParser.RULE_log_op2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_op2" ):
                listener.enterLog_op2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_op2" ):
                listener.exitLog_op2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_op2" ):
                return visitor.visitLog_op2(self)
            else:
                return visitor.visitChildren(self)




    def log_op2(self):

        localctx = mathGrammerParser.Log_op2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_log_op2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.log_op3()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.T__2:
                self.state = 77
                self.match(mathGrammerParser.T__2)
                self.state = 78
                self.log_op3()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_op3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_op3(self):
            return self.getTypedRuleContext(mathGrammerParser.Log_op3Context,0)


        def comp_expr(self):
            return self.getTypedRuleContext(mathGrammerParser.Comp_exprContext,0)


        def getRuleIndex(self):
            return mathGrammerParser.RULE_log_op3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_op3" ):
                listener.enterLog_op3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_op3" ):
                listener.exitLog_op3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_op3" ):
                return visitor.visitLog_op3(self)
            else:
                return visitor.visitChildren(self)




    def log_op3(self):

        localctx = mathGrammerParser.Log_op3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_log_op3)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(mathGrammerParser.T__3)
                self.state = 85
                self.log_op3()
                pass
            elif token in [mathGrammerParser.T__4, mathGrammerParser.UN_OP, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.comp_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(mathGrammerParser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(mathGrammerParser.ExprContext,0)


        def getRuleIndex(self):
            return mathGrammerParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = mathGrammerParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var)
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(mathGrammerParser.INT)
                pass
            elif token in [mathGrammerParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(mathGrammerParser.T__4)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(mathGrammerParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




