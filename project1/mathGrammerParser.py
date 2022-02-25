# Generated from mathGrammer.g4 by ANTLR 4.9.3
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
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5*\n\5\f\5\16\5-\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6\65")
        buf.write("\n\6\f\6\16\68\13\6\3\7\3\7\3\7\5\7=\n\7\3\b\3\b\3\b\7")
        buf.write("\bB\n\b\f\b\16\bE\13\b\3\t\3\t\3\t\7\tJ\n\t\f\t\16\tM")
        buf.write("\13\t\3\n\3\n\3\n\5\nR\n\n\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13Y\n\13\3\13\2\4\b\n\f\2\4\6\b\n\f\16\20\22\24\2\2\2")
        buf.write("W\2\26\3\2\2\2\4\33\3\2\2\2\6\37\3\2\2\2\b#\3\2\2\2\n")
        buf.write(".\3\2\2\2\f<\3\2\2\2\16>\3\2\2\2\20F\3\2\2\2\22Q\3\2\2")
        buf.write("\2\24X\3\2\2\2\26\27\5\16\b\2\27\30\7\3\2\2\30\31\7\4")
        buf.write("\2\2\31\32\5\2\2\2\32\3\3\2\2\2\33\34\5\6\4\2\34\35\7")
        buf.write("\r\2\2\35\36\5\6\4\2\36\5\3\2\2\2\37 \5\b\5\2 !\7\f\2")
        buf.write("\2!\"\5\b\5\2\"\7\3\2\2\2#$\b\5\1\2$%\5\n\6\2%+\3\2\2")
        buf.write("\2&\'\f\4\2\2\'(\7\n\2\2(*\5\n\6\2)&\3\2\2\2*-\3\2\2\2")
        buf.write("+)\3\2\2\2+,\3\2\2\2,\t\3\2\2\2-+\3\2\2\2./\b\6\1\2/\60")
        buf.write("\5\f\7\2\60\66\3\2\2\2\61\62\f\4\2\2\62\63\7\13\2\2\63")
        buf.write("\65\5\f\7\2\64\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66")
        buf.write("\67\3\2\2\2\67\13\3\2\2\28\66\3\2\2\29:\7\16\2\2:=\5\f")
        buf.write("\7\2;=\5\24\13\2<9\3\2\2\2<;\3\2\2\2=\r\3\2\2\2>C\5\20")
        buf.write("\t\2?@\7\5\2\2@B\5\20\t\2A?\3\2\2\2BE\3\2\2\2CA\3\2\2")
        buf.write("\2CD\3\2\2\2D\17\3\2\2\2EC\3\2\2\2FK\5\22\n\2GH\7\6\2")
        buf.write("\2HJ\5\22\n\2IG\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2")
        buf.write("L\21\3\2\2\2MK\3\2\2\2NO\7\7\2\2OR\5\22\n\2PR\5\4\3\2")
        buf.write("QN\3\2\2\2QP\3\2\2\2R\23\3\2\2\2SY\7\17\2\2TU\7\b\2\2")
        buf.write("UV\5\b\5\2VW\7\t\2\2WY\3\2\2\2XS\3\2\2\2XT\3\2\2\2Y\25")
        buf.write("\3\2\2\2\t+\66<CKQX")
        return buf.getvalue()


class mathGrammerParser ( Parser ):

    grammarFileName = "mathGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'/n'", "'||'", "'&&'", "'!'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BIN_OP1", "BIN_OP2", "COMP_OP", "EQ_OP", "UN_OP", 
                      "INT" ]

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
    T__6=7
    BIN_OP1=8
    BIN_OP2=9
    COMP_OP=10
    EQ_OP=11
    UN_OP=12
    INT=13

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
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.log_op1()
            self.state = 21
            self.match(mathGrammerParser.T__0)
            self.state = 22
            self.match(mathGrammerParser.T__1)
            self.state = 23
            self.math()
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
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.comp_expr1()
            self.state = 26
            self.match(mathGrammerParser.EQ_OP)
            self.state = 27
            self.comp_expr1()
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
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.expr(0)
            self.state = 30
            self.match(mathGrammerParser.COMP_OP)
            self.state = 31
            self.expr(0)
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
            self.state = 34
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mathGrammerParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 36
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 37
                    self.match(mathGrammerParser.BIN_OP1)
                    self.state = 38
                    self.factor(0) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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
            self.state = 45
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mathGrammerParser.FactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 47
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 48
                    self.match(mathGrammerParser.BIN_OP2)
                    self.state = 49
                    self.term() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.UN_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(mathGrammerParser.UN_OP)
                self.state = 56
                self.term()
                pass
            elif token in [mathGrammerParser.T__5, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
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
            self.state = 60
            self.log_op2()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.T__2:
                self.state = 61
                self.match(mathGrammerParser.T__2)
                self.state = 62
                self.log_op2()
                self.state = 67
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
            self.state = 68
            self.log_op3()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.T__3:
                self.state = 69
                self.match(mathGrammerParser.T__3)
                self.state = 70
                self.log_op3()
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(mathGrammerParser.T__4)
                self.state = 77
                self.log_op3()
                pass
            elif token in [mathGrammerParser.T__5, mathGrammerParser.UN_OP, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(mathGrammerParser.INT)
                pass
            elif token in [mathGrammerParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(mathGrammerParser.T__5)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(mathGrammerParser.T__6)
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
         




