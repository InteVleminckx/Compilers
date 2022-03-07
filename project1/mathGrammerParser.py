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
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\34\n\2\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4*\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\62\n\5\f\5\16")
        buf.write("\5\65\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16\6@")
        buf.write("\13\6\3\7\7\7C\n\7\f\7\16\7F\13\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\7\bM\n\b\f\b\16\bP\13\b\3\t\3\t\3\t\7\tU\n\t\f\t\16\t")
        buf.write("X\13\t\3\n\3\n\3\n\5\n]\n\n\3\13\3\13\3\13\3\13\3\13\5")
        buf.write("\13d\n\13\3\13\2\4\b\n\f\2\4\6\b\n\f\16\20\22\24\2\3\3")
        buf.write("\2\7\b\2e\2\33\3\2\2\2\4\"\3\2\2\2\6)\3\2\2\2\b+\3\2\2")
        buf.write("\2\n\66\3\2\2\2\fD\3\2\2\2\16I\3\2\2\2\20Q\3\2\2\2\22")
        buf.write("\\\3\2\2\2\24c\3\2\2\2\26\27\5\16\b\2\27\30\7\3\2\2\30")
        buf.write("\31\5\2\2\2\31\34\3\2\2\2\32\34\7\2\2\3\33\26\3\2\2\2")
        buf.write("\33\32\3\2\2\2\34\3\3\2\2\2\35\36\5\6\4\2\36\37\7\r\2")
        buf.write("\2\37 \5\4\3\2 #\3\2\2\2!#\5\6\4\2\"\35\3\2\2\2\"!\3\2")
        buf.write("\2\2#\5\3\2\2\2$%\5\b\5\2%&\7\f\2\2&\'\5\b\5\2\'*\3\2")
        buf.write("\2\2(*\5\b\5\2)$\3\2\2\2)(\3\2\2\2*\7\3\2\2\2+,\b\5\1")
        buf.write("\2,-\5\n\6\2-\63\3\2\2\2./\f\4\2\2/\60\t\2\2\2\60\62\5")
        buf.write("\n\6\2\61.\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3")
        buf.write("\2\2\2\64\t\3\2\2\2\65\63\3\2\2\2\66\67\b\6\1\2\678\5")
        buf.write("\f\7\28>\3\2\2\29:\f\4\2\2:;\7\6\2\2;=\5\f\7\2<9\3\2\2")
        buf.write("\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\13\3\2\2\2@>\3\2\2\2")
        buf.write("AC\t\2\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3")
        buf.write("\2\2\2FD\3\2\2\2GH\5\24\13\2H\r\3\2\2\2IN\5\20\t\2JK\7")
        buf.write("\t\2\2KM\5\20\t\2LJ\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2")
        buf.write("\2\2O\17\3\2\2\2PN\3\2\2\2QV\5\22\n\2RS\7\n\2\2SU\5\22")
        buf.write("\n\2TR\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\21\3\2\2")
        buf.write("\2XV\3\2\2\2YZ\7\13\2\2Z]\5\22\n\2[]\5\4\3\2\\Y\3\2\2")
        buf.write("\2\\[\3\2\2\2]\23\3\2\2\2^d\7\16\2\2_`\7\4\2\2`a\5\16")
        buf.write("\b\2ab\7\5\2\2bd\3\2\2\2c^\3\2\2\2c_\3\2\2\2d\25\3\2\2")
        buf.write("\2\f\33\")\63>DNV\\c")
        return buf.getvalue()


class mathGrammerParser ( Parser ):

    grammarFileName = "mathGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "<INVALID>", "'+'", 
                     "'-'", "'||'", "'&&'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BIN_OP2", "PLUS", "MIN", "LOG_OR", "LOG_AND", "LOG_NOT", 
                      "COMP_OP", "EQ_OP", "INT", "WS" ]

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
    BIN_OP2=4
    PLUS=5
    MIN=6
    LOG_OR=7
    LOG_AND=8
    LOG_NOT=9
    COMP_OP=10
    EQ_OP=11
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
            if token in [mathGrammerParser.T__1, mathGrammerParser.PLUS, mathGrammerParser.MIN, mathGrammerParser.LOG_NOT, mathGrammerParser.INT]:
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

        def comp_expr1(self):
            return self.getTypedRuleContext(mathGrammerParser.Comp_expr1Context,0)


        def EQ_OP(self):
            return self.getToken(mathGrammerParser.EQ_OP, 0)

        def comp_expr(self):
            return self.getTypedRuleContext(mathGrammerParser.Comp_exprContext,0)


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
                self.comp_expr()
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


        def PLUS(self):
            return self.getToken(mathGrammerParser.PLUS, 0)

        def MIN(self):
            return self.getToken(mathGrammerParser.MIN, 0)

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
        self._la = 0 # Token type
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
                    _la = self._input.LA(1)
                    if not(_la==mathGrammerParser.PLUS or _la==mathGrammerParser.MIN):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
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

        def var(self):
            return self.getTypedRuleContext(mathGrammerParser.VarContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(mathGrammerParser.PLUS)
            else:
                return self.getToken(mathGrammerParser.PLUS, i)

        def MIN(self, i:int=None):
            if i is None:
                return self.getTokens(mathGrammerParser.MIN)
            else:
                return self.getToken(mathGrammerParser.MIN, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.PLUS or _la==mathGrammerParser.MIN:
                self.state = 63
                _la = self._input.LA(1)
                if not(_la==mathGrammerParser.PLUS or _la==mathGrammerParser.MIN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.var()
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


        def LOG_OR(self, i:int=None):
            if i is None:
                return self.getTokens(mathGrammerParser.LOG_OR)
            else:
                return self.getToken(mathGrammerParser.LOG_OR, i)

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
            self.state = 71
            self.log_op2()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.LOG_OR:
                self.state = 72
                self.match(mathGrammerParser.LOG_OR)
                self.state = 73
                self.log_op2()
                self.state = 78
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


        def LOG_AND(self, i:int=None):
            if i is None:
                return self.getTokens(mathGrammerParser.LOG_AND)
            else:
                return self.getToken(mathGrammerParser.LOG_AND, i)

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
            self.state = 79
            self.log_op3()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mathGrammerParser.LOG_AND:
                self.state = 80
                self.match(mathGrammerParser.LOG_AND)
                self.state = 81
                self.log_op3()
                self.state = 86
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

        def LOG_NOT(self):
            return self.getToken(mathGrammerParser.LOG_NOT, 0)

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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.LOG_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(mathGrammerParser.LOG_NOT)
                self.state = 88
                self.log_op3()
                pass
            elif token in [mathGrammerParser.T__1, mathGrammerParser.PLUS, mathGrammerParser.MIN, mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
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

        def log_op1(self):
            return self.getTypedRuleContext(mathGrammerParser.Log_op1Context,0)


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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathGrammerParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(mathGrammerParser.INT)
                pass
            elif token in [mathGrammerParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(mathGrammerParser.T__1)
                self.state = 94
                self.log_op1()
                self.state = 95
                self.match(mathGrammerParser.T__2)
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
         




