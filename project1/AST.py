from mathGrammerListener import mathGrammerListener
from mathGrammerParser import mathGrammerParser

"""
getChildCount():
    Geeft het aantal kinderen weer -> als deze 0 is hebben we een blad




"""



class Node:

    def __init__(self, value, token):
        self.value = value
        self.token = token

    def getValue(self):
        return self.value

    def getToken(self):
        return self.token

def createNodeItem(value, token):
    node = Node(value, token)
    return node

class AST:

    def __init__(self, parent=None, root=None):
        self.root = root
        self.parent = parent
        self.children = []

    def addNode(self, node, parent):
        if self.root is None:
            self.root = node
        elif parent is None:
            self.children.append(AST(self, node))
        else:
            self.getParent(parent).children.append(AST(self.getParent(parent), node))

    def getParent(self, parent):

        if self.root is not None:
            for child in self.children:
                if child == parent:
                    return child
                else:
                    return self.getParent(child)
        else:
            return None

ast = AST()

def createNode(parent, ctx, token, value):

    node = createNodeItem(value, token)

    if value != "INT":
        parent = node
    # if ctx.getChild(ctx.getChildCount()-1) == token:
    #     parent = parent.parent
    elif ctx.getChildCount == 1:
        pass
    else:
        pass

    ast.addNode(node, parent)

class ASTprinter(mathGrammerListener):

    def __init__(self, prevNode=None):
        self.prevNode = prevNode

    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx: mathGrammerParser.MathContext):
        # print("enterMath")
        pass

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx: mathGrammerParser.MathContext):
        # # print(ctx)
        # print("exitMath")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # print("enterComp_expr")
        if ctx.getChildCount() == 3:
            print(ctx.EQ_OP())
            # node = Node(None, ctx.EQ_OP(), "EQ_OP")
            createNode(self.prevNode, ctx, ctx.EQ_OP(), "EQ_OP")

        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # # print(ctx)
        # print("exitComp_expr")
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # print("enterComp_expr1")
        if ctx.getChildCount() == 3:
            print(ctx.COMP_OP())
            # node = Node(None, ctx.COMP_OP(), "COMP_OP")
            createNode(self.prevNode, ctx, ctx.COMP_OP(), "COMP_OP")
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # # print(ctx)
        # print("exitComp_expr1")
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        # print("enterExpr")

        if ctx.getChildCount() == 3:
            print(ctx.BIN_OP1())
            # node = Node(None, ctx.BIN_OP1(), "BIN_OP1")
            createNode(self.prevNode, ctx, ctx.BIN_OP1(), "BIN_OP1")

        pass

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        # # print(ctx)
        # print("exitExpr")
        pass

    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        # print("enterFactor")

        if ctx.getChildCount() == 3:
            print(ctx.BIN_OP2())
            createNode(self.prevNode, ctx, ctx.BIN_OP2(), "BIN_OP2")

        pass

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        # # print(ctx)
        # print("exitFactor")
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        # print("enterTerm")

        if ctx.getChildCount() == 2:
            print(ctx.UN_OP())
            createNode(self.prevNode, ctx, ctx.UN_OP(), "UN_OP")

        pass

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        # # print(ctx)
        # print("exitTerm")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print(ctx)
        # print("enterLog_op1")
        if ctx.getChildCount() > 1:
            for log in ctx.LOG_OR():
                createNode(self.prevNode, ctx, log, "LOG_OR")

        pass

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print(ctx)
        # print("exitLog_op1")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # print(ctx)
        # print("enterLog_op2")
        if ctx.getChildCount() > 1:
            for log in ctx.LOG_AND():
                createNode(self.prevNode, ctx, log, "LOG_AND")

        pass

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # print(ctx)
        # print("exitLog_op2")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # print(ctx)
        # print("enterLog_op3")
        if ctx.getChildCount() > 1:
            createNode(self.prevNode, ctx, ctx.LOG_NOT(), "LOG_NOT")

        pass

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # print(ctx)
        # print("exitLog_op3")
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        if ctx.INT() is None: # speciale regel => zie grammar
            return
        if ctx.getChildCount() == 1:
            print(ctx.INT())
            createNode(self.prevNode, ctx, ctx.INT(), "INT")
            # print("var heeft 1 child")
        else: # if there are 3 children
            print(ctx.INT())
            # print("var heeft 3 children")

        # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        # # print(ctx)
        # print("exitVar")
        pass
