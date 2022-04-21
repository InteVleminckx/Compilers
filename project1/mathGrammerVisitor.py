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


    # Visit a parse tree produced by mathGrammerParser#import_stat_list.
    def visitImport_stat_list(self, ctx:mathGrammerParser.Import_stat_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#import_statement.
    def visitImport_statement(self, ctx:mathGrammerParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#statement.
    def visitStatement(self, ctx:mathGrammerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#extern_decl.
    def visitExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#scan_stmt.
    def visitScan_stmt(self, ctx:mathGrammerParser.Scan_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#print_stmt.
    def visitPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#print_values.
    def visitPrint_values(self, ctx:mathGrammerParser.Print_valuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#function_def.
    def visitFunction_def(self, ctx:mathGrammerParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#stat.
    def visitStat(self, ctx:mathGrammerParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#comp_stat.
    def visitComp_stat(self, ctx:mathGrammerParser.Comp_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#it_statement.
    def visitIt_statement(self, ctx:mathGrammerParser.It_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#sel_statement.
    def visitSel_statement(self, ctx:mathGrammerParser.Sel_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#j_statement.
    def visitJ_statement(self, ctx:mathGrammerParser.J_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#expr_statement.
    def visitExpr_statement(self, ctx:mathGrammerParser.Expr_statementContext):
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


    # Visit a parse tree produced by mathGrammerParser#initializer_list.
    def visitInitializer_list(self, ctx:mathGrammerParser.Initializer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#direct_declarator.
    def visitDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#identifier_list.
    def visitIdentifier_list(self, ctx:mathGrammerParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#parameter_type_list.
    def visitParameter_type_list(self, ctx:mathGrammerParser.Parameter_type_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#parameter_decl.
    def visitParameter_decl(self, ctx:mathGrammerParser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#ttype.
    def visitTtype(self, ctx:mathGrammerParser.TtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#pointer.
    def visitPointer(self, ctx:mathGrammerParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#reference.
    def visitReference(self, ctx:mathGrammerParser.ReferenceContext):
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


    # Visit a parse tree produced by mathGrammerParser#ampersandsign.
    def visitAmpersandsign(self, ctx:mathGrammerParser.AmpersandsignContext):
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


    # Visit a parse tree produced by mathGrammerParser#func_call.
    def visitFunc_call(self, ctx:mathGrammerParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathGrammerParser#func_call_par_list.
    def visitFunc_call_par_list(self, ctx:mathGrammerParser.Func_call_par_listContext):
        return self.visitChildren(ctx)



del mathGrammerParser