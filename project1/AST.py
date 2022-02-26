from mathGrammerListener import mathGrammerListener
from mathGrammerParser import mathGrammerParser


class Node:

    def __init__(self, parent, value, token):
        self.parent = parent
        self.value = value
        self.token = token
        self.children = []


class AST:

    def __init__(self, root=None):
        self.root = root

    def addNode(self, node):

        pass

    # def inorderTraverse(self, visit):
    #
    #     if self.root is not None:
    #
    #         if self.linkerKind is not None:
    #             self.linkerKind.inorderTraverse(visit)
    #         visit(self.waarde.getSearchkey())
    #         if self.rechterKind is not None:
    #             self.rechterKind.inorderTraverse(visit)
    #     else:
    #         return None


class ASTprinter(mathGrammerListener):

    # def __init__(self, prevNode, ast):
    #     self.prevNode = prevNode
    #     self.ast = ast

    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx: mathGrammerParser.MathContext):
        print("enterMath")
        pass

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx: mathGrammerParser.MathContext):
        # # print(ctx)
        print("exitMath")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        print(ctx.EQ_OP())
        print("enterComp_expr")
        if ctx.getChildCount() == 3:
            node = Node(None, ctx.EQ_OP(), "EQ_OP")

        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # # print(ctx)
        print("exitComp_expr")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        print(ctx.COMP_OP())
        print("enterComp_expr1")
        if ctx.getChildCount() == 3:
            node = Node(None, ctx.COMP_OP(), "COMP_OP")

        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # # print(ctx)
        print("exitComp_expr1")
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        print(ctx.BIN_OP1())
        print("enterExpr")

        if ctx.getChildCount() == 3:
            node = Node(None, ctx.BIN_OP1(), "BIN_OP1")

        pass

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        # # print(ctx)
        print("exitExpr")
        pass

    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        print(ctx.BIN_OP2())
        print("enterFactor")

        if ctx.getChildCount() == 3:
            node = Node(None, ctx.BIN_OP2(), "BIN_OP2")

        pass

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        # # print(ctx)
        print("exitFactor")
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        print(ctx.UN_OP())
        print("enterTerm")

        if ctx.getChildCount() == 2:
            node = Node(None, ctx.UN_OP(), "UN_OP")

        pass

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        # # print(ctx)
        print("exitTerm")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print(ctx)
        print("enterLog_op1")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print(ctx)
        print("exitLog_op1")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # print(ctx)
        print("enterLog_op2")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # print(ctx)
        print("exitLog_op2")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # print(ctx)
        print("enterLog_op3")
        pass

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # print(ctx)
        print("exitLog_op3")
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        print(ctx.INT())
        print("enterVar")

        if ctx.INT() is None: # speciale regel => zie grammar
            return
        if ctx.getChildCount() == 1:
            node = Node(None, ctx.INT(), "INT")
            print("var heeft 1 child")
        else: # if there are 3 children
            print("var heeft 3 children")

        # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        # # print(ctx)
        print("exitVar")
        pass
