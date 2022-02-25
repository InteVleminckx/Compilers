# Generated from mathGrammer.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathGrammerParser import mathGrammerParser
else:
    from mathGrammerParser import mathGrammerParser

# This class defines a complete generic visitor for a parse tree produced by mathGrammerParser.

class mathGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mathGrammerParser#math.
    def visitMath(self, ctx:mathGrammerParser.MathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#comp_expr.
    def visitComp_expr(self, ctx:mathGrammerParser.Comp_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#comp_expr1.
    def visitComp_expr1(self, ctx:mathGrammerParser.Comp_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#expr.
    def visitExpr(self, ctx:mathGrammerParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#factor.
    def visitFactor(self, ctx:mathGrammerParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#term.
    def visitTerm(self, ctx:mathGrammerParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#log_op1.
    def visitLog_op1(self, ctx:mathGrammerParser.Log_op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#log_op2.
    def visitLog_op2(self, ctx:mathGrammerParser.Log_op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#log_op3.
    def visitLog_op3(self, ctx:mathGrammerParser.Log_op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#var.
    def visitVar(self, ctx:mathGrammerParser.VarContext):
        return self.visitChildren(ctx)



del mathGrammerParser