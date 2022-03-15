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


    # Visit a parse tree produced by mathGrammerParser#statement.
    def visitStatement(self, ctx:mathGrammerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#extern_decl.
    def visitExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#print_stmt.
    def visitPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#function_def.
    def visitFunction_def(self, ctx:mathGrammerParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#declaration.
    def visitDeclaration(self, ctx:mathGrammerParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#decl_spec.
    def visitDecl_spec(self, ctx:mathGrammerParser.Decl_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#init_decl_list.
    def visitInit_decl_list(self, ctx:mathGrammerParser.Init_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#init_declarator.
    def visitInit_declarator(self, ctx:mathGrammerParser.Init_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#declarator.
    def visitDeclarator(self, ctx:mathGrammerParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#initializer.
    def visitInitializer(self, ctx:mathGrammerParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#direct_declarator.
    def visitDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#ttype.
    def visitTtype(self, ctx:mathGrammerParser.TtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#pointer.
    def visitPointer(self, ctx:mathGrammerParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#type_qualifier_list.
    def visitType_qualifier_list(self, ctx:mathGrammerParser.Type_qualifier_listContext):
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


    # Visit a parse tree produced by mathGrammerParser#pointersign.
    def visitPointersign(self, ctx:mathGrammerParser.PointersignContext):
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