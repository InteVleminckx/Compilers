# Generated from mathGrammer.g4 by ANTLR 4.9.3
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


    # Enter a parse tree produced by mathGrammerParser#import_stat_list.
    def enterImport_stat_list(self, ctx:mathGrammerParser.Import_stat_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#import_stat_list.
    def exitImport_stat_list(self, ctx:mathGrammerParser.Import_stat_listContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#import_statement.
    def enterImport_statement(self, ctx:mathGrammerParser.Import_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#import_statement.
    def exitImport_statement(self, ctx:mathGrammerParser.Import_statementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#statement.
    def enterStatement(self, ctx:mathGrammerParser.StatementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#statement.
    def exitStatement(self, ctx:mathGrammerParser.StatementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#extern_decl.
    def enterExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#extern_decl.
    def exitExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#scan_stmt.
    def enterScan_stmt(self, ctx:mathGrammerParser.Scan_stmtContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#scan_stmt.
    def exitScan_stmt(self, ctx:mathGrammerParser.Scan_stmtContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#print_stmt.
    def enterPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#print_stmt.
    def exitPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#print_values.
    def enterPrint_values(self, ctx:mathGrammerParser.Print_valuesContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#print_values.
    def exitPrint_values(self, ctx:mathGrammerParser.Print_valuesContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#function_def.
    def enterFunction_def(self, ctx:mathGrammerParser.Function_defContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#function_def.
    def exitFunction_def(self, ctx:mathGrammerParser.Function_defContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#stat.
    def enterStat(self, ctx:mathGrammerParser.StatContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#stat.
    def exitStat(self, ctx:mathGrammerParser.StatContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#comp_stat.
    def enterComp_stat(self, ctx:mathGrammerParser.Comp_statContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_stat.
    def exitComp_stat(self, ctx:mathGrammerParser.Comp_statContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#it_statement.
    def enterIt_statement(self, ctx:mathGrammerParser.It_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#it_statement.
    def exitIt_statement(self, ctx:mathGrammerParser.It_statementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#sel_statement.
    def enterSel_statement(self, ctx:mathGrammerParser.Sel_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#sel_statement.
    def exitSel_statement(self, ctx:mathGrammerParser.Sel_statementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#j_statement.
    def enterJ_statement(self, ctx:mathGrammerParser.J_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#j_statement.
    def exitJ_statement(self, ctx:mathGrammerParser.J_statementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#expr_statement.
    def enterExpr_statement(self, ctx:mathGrammerParser.Expr_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#expr_statement.
    def exitExpr_statement(self, ctx:mathGrammerParser.Expr_statementContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#declaration.
    def enterDeclaration(self, ctx:mathGrammerParser.DeclarationContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#declaration.
    def exitDeclaration(self, ctx:mathGrammerParser.DeclarationContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#decl_spec.
    def enterDecl_spec(self, ctx:mathGrammerParser.Decl_specContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#decl_spec.
    def exitDecl_spec(self, ctx:mathGrammerParser.Decl_specContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#init_decl_list.
    def enterInit_decl_list(self, ctx:mathGrammerParser.Init_decl_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#init_decl_list.
    def exitInit_decl_list(self, ctx:mathGrammerParser.Init_decl_listContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#init_declarator.
    def enterInit_declarator(self, ctx:mathGrammerParser.Init_declaratorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#init_declarator.
    def exitInit_declarator(self, ctx:mathGrammerParser.Init_declaratorContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#declarator.
    def enterDeclarator(self, ctx:mathGrammerParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#declarator.
    def exitDeclarator(self, ctx:mathGrammerParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#initializer.
    def enterInitializer(self, ctx:mathGrammerParser.InitializerContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#initializer.
    def exitInitializer(self, ctx:mathGrammerParser.InitializerContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#initializer_list.
    def enterInitializer_list(self, ctx:mathGrammerParser.Initializer_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#initializer_list.
    def exitInitializer_list(self, ctx:mathGrammerParser.Initializer_listContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#direct_declarator.
    def enterDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#direct_declarator.
    def exitDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#identifier_list.
    def enterIdentifier_list(self, ctx:mathGrammerParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#identifier_list.
    def exitIdentifier_list(self, ctx:mathGrammerParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#parameter_type_list.
    def enterParameter_type_list(self, ctx:mathGrammerParser.Parameter_type_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#parameter_type_list.
    def exitParameter_type_list(self, ctx:mathGrammerParser.Parameter_type_listContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#parameter_decl.
    def enterParameter_decl(self, ctx:mathGrammerParser.Parameter_declContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#parameter_decl.
    def exitParameter_decl(self, ctx:mathGrammerParser.Parameter_declContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#ttype.
    def enterTtype(self, ctx:mathGrammerParser.TtypeContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#ttype.
    def exitTtype(self, ctx:mathGrammerParser.TtypeContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#pointer.
    def enterPointer(self, ctx:mathGrammerParser.PointerContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#pointer.
    def exitPointer(self, ctx:mathGrammerParser.PointerContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#reference.
    def enterReference(self, ctx:mathGrammerParser.ReferenceContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#reference.
    def exitReference(self, ctx:mathGrammerParser.ReferenceContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#type_qualifier_list.
    def enterType_qualifier_list(self, ctx:mathGrammerParser.Type_qualifier_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#type_qualifier_list.
    def exitType_qualifier_list(self, ctx:mathGrammerParser.Type_qualifier_listContext):
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


    # Enter a parse tree produced by mathGrammerParser#pointersign.
    def enterPointersign(self, ctx:mathGrammerParser.PointersignContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#pointersign.
    def exitPointersign(self, ctx:mathGrammerParser.PointersignContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#ampersandsign.
    def enterAmpersandsign(self, ctx:mathGrammerParser.AmpersandsignContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#ampersandsign.
    def exitAmpersandsign(self, ctx:mathGrammerParser.AmpersandsignContext):
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


    # Enter a parse tree produced by mathGrammerParser#func_call.
    def enterFunc_call(self, ctx:mathGrammerParser.Func_callContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#func_call.
    def exitFunc_call(self, ctx:mathGrammerParser.Func_callContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#func_call_par_list.
    def enterFunc_call_par_list(self, ctx:mathGrammerParser.Func_call_par_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#func_call_par_list.
    def exitFunc_call_par_list(self, ctx:mathGrammerParser.Func_call_par_listContext):
        pass



del mathGrammerParser