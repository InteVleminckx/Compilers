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


    # Enter a parse tree produced by mathGrammerParser#extern_decl.
    def enterExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#extern_decl.
    def exitExtern_decl(self, ctx:mathGrammerParser.Extern_declContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#comment.
    def enterComment(self, ctx:mathGrammerParser.CommentContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#comment.
    def exitComment(self, ctx:mathGrammerParser.CommentContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#single_comment.
    def enterSingle_comment(self, ctx:mathGrammerParser.Single_commentContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#single_comment.
    def exitSingle_comment(self, ctx:mathGrammerParser.Single_commentContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#multi_comment.
    def enterMulti_comment(self, ctx:mathGrammerParser.Multi_commentContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#multi_comment.
    def exitMulti_comment(self, ctx:mathGrammerParser.Multi_commentContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#print_stmt.
    def enterPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#print_stmt.
    def exitPrint_stmt(self, ctx:mathGrammerParser.Print_stmtContext):
        pass


    # Enter a parse tree produced by mathGrammerParser#function_def.
    def enterFunction_def(self, ctx:mathGrammerParser.Function_defContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#function_def.
    def exitFunction_def(self, ctx:mathGrammerParser.Function_defContext):
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


    # Enter a parse tree produced by mathGrammerParser#direct_declarator.
    def enterDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#direct_declarator.
    def exitDirect_declarator(self, ctx:mathGrammerParser.Direct_declaratorContext):
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