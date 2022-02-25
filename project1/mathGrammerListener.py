# Generated from .\mathGrammer.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathGrammerParser import mathGrammerParser
else:
    from mathGrammerParser import mathGrammerParser

# This class defines a complete listener for a parse tree produced by mathGrammerParser.
class mathGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx:mathGrammerParser.MathContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx:mathGrammerParser.MathContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx:mathGrammerParser.Comp_exprContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx:mathGrammerParser.Comp_exprContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx:mathGrammerParser.Comp_expr1Context):
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx:mathGrammerParser.Comp_expr1Context):
        pass


    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx:mathGrammerParser.ExprContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx:mathGrammerParser.ExprContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx:mathGrammerParser.FactorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx:mathGrammerParser.FactorContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx:mathGrammerParser.TermContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx:mathGrammerParser.TermContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx:mathGrammerParser.Log_op1Context):
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx:mathGrammerParser.Log_op1Context):
        pass


    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx:mathGrammerParser.Log_op2Context):
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx:mathGrammerParser.Log_op2Context):
        pass


    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx:mathGrammerParser.Log_op3Context):
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx:mathGrammerParser.Log_op3Context):
        pass


    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx:mathGrammerParser.VarContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx:mathGrammerParser.VarContext):
        pass



del mathGrammerParser