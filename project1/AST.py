from mathGrammerListener import mathGrammerListener
from mathGrammerParser import  mathGrammerParser


class Node:

    def __init__(self, parent, value, token):
        self.parent = parent
        self.value = value
        self.token = token
        self.children = []


class AST:

    def __init__(self, root):
        self.root = root

    def addNode(self):
        pass


class ASTprinter(mathGrammerListener):
    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx: mathGrammerParser.MathContext):
        if ctx.getChildCount() == 3:
            pass
        else:
            pass
        # print("enterMath")
        pass

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx: mathGrammerParser.MathContext):
        # # print(ctx)
        # print("exitMath")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # # print(ctx)
        # print("enterComp_expr")
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # # print(ctx)
        # print("exitComp_expr")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # # print(ctx)
        # print("enterComp_expr1")
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # # print(ctx)
        # print("exitComp_expr1")
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        # # print(ctx)
        # print("enterExpr")
        pass

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        # # print(ctx)
        # print("exitExpr")
        pass
    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        # # print(ctx)
        # print("enterFactor")
        pass

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        # # print(ctx)
        # print("exitFactor")
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        # # print(ctx)
        # print("enterTerm")
        pass

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        # # print(ctx)
        # print("exitTerm")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # # print(ctx)
        # print("enterLog_op1")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # # print(ctx)
        # print("exitLog_op1")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # # print(ctx)
        # print("enterLog_op2")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # # print(ctx)
        # print("exitLog_op2")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # # print(ctx)
        # print("enterLog_op3")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # # print(ctx)
        # print("exitLog_op3")
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        # # print(ctx)
        # print("enterVar")
        pass

    # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        # # print(ctx)
        # print("exitVar")
        pass
