from mathGrammerListener import mathGrammerListener
from mathGrammerParser import mathGrammerParser
from SymbolTable import *
import os
import re

var_list = ["CHAR", "INT", "FLOAT", "IDENTIFIER"]


def createNodeItem(token, value, parent,line=0,column=0 ,type="", isConst=False, isOverwritten=False):
    node = Node(token, value, parent, line, column, type, isConst, isOverwritten)
    return node


class Node:

    def __init__(self, token, value, parent,line, column, type, isConst, isOverwritten=None):
        self.value = value
        self.token = token
        self.parent = parent
        self.line = line
        self.column = column
        self.children = []

        self.type = type
        self.isConst = isConst
        self.isOverwritten = isOverwritten

        self.symbolTablePointer = None

    def getValue(self):
        return self.value

    def getToken(self):
        return self.token


class AST:

    def __init__(self, root=None):
        self.root = root
        self.parentsList = []
        self.unaries = []

        self.nextConst = False
        self.nextType = ""
        self.nextOverwrite = False # for debugging purposes, can be removed (but then all references to this should be removed)

        globalTable = SymbolTable()
        globalTable.astNode = self.root
        self.symbolTableList = [globalTable]
        self.symbolTableStack = [globalTable] # herkent dat niet als een stack in een andere functie, top() werkt niet

    def createNode(self, value, token, numberOfChilds, line, column,type="", isConst=False, isOverwritten=False, unaryParenth=False):
        # Als er parents tussen zitten waarbij die children al volledig zijn opgevuld dan zijn deze niet meer nodig
        for parent in self.parentsList:
            hasUnfilledChildren = False
            for child in parent.children:
                if child is None:
                    hasUnfilledChildren = True
                    break

            if not hasUnfilledChildren:
                self.parentsList.remove(parent)

        # We maken een node aan en pre-fillen al de children
        if self.root is None:
            node = createNodeItem(token, value, None,line,column, type, isConst, isOverwritten)
            for i in range(numberOfChilds):
                node.children.append(None)
            self.root = node
            if not var_list.count(token):
                self.parentsList.append(node)

        else:
            curParent = self.parentsList[len(self.parentsList) - 1]

            if var_list.count(token):
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinderen aan toevoegen.
                node = createNodeItem(token, value, curParent,line,column, type, isConst, isOverwritten)
                for i in range(len(curParent.children)):
                    if curParent.children[i] is None:
                        curParent.children[i] = node
                        break

            elif (token == "LOG_NOT" or token == "UN_OP") and not unaryParenth:
                self.unaries.append((token, value))

            else:
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinderen aan toevoegen.
                node = createNodeItem(token, value, curParent,line,column, type, isConst, isOverwritten)
                for i in range(numberOfChilds):
                    node.children.append(None)
                for i in range(len(curParent.children)):
                    if curParent.children[i] is None:
                        curParent.children[i] = node
                        break
                self.parentsList.append(node)

                if len(self.unaries) != 0:
                    for unary in self.unaries:
                        curParent = self.parentsList[len(self.parentsList) - 1]

                        node = createNodeItem(unary[0], unary[1], curParent,line,column, type, isConst, isOverwritten)
                        node.children.append(None)
                        for i in range(len(curParent.children)):
                            if curParent.children[i] is None:
                                curParent.children[i] = node
                                break
                        self.parentsList.append(node)

                    self.unaries = []

    def inorderTraversal(self, visit, node=None):

        if self.root is None:
            return None

        elif node is None:  # Hebben we de root
            count = 0
            if len(self.root.children) > 0:
                for child in self.root.children:
                    self.inorderTraversal(visit, child)
                    count += 1
                    if count == len(self.root.children) / 2:
                        visit(self.root.value)

            else:
                # Heeft geen kinderen dus er is enkel een root
                visit(self.root.value)

        else:
            count = 0
            if len(node.children) > 0:
                for child in node.children:
                    self.inorderTraversal(visit, child)
                    count += 1
                    if count == len(node.children) / 2:
                        visit(node.value)
            else:
                # Heeft geen kinderen dus er is enkel een root
                visit(node.value)


ast = AST()

# De self.root kan eigenlijk nooit None zijn dan dus we voegen deze gewoon al toe aan het begin van de expressie
ast.root = createNodeItem("ROOT", "ROOT", None)
ast.root.symbolTablePointer = ast.symbolTableList[0]

class ASTprinter(mathGrammerListener):

    def __init__(self):
        self.prevParents = []

    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx: mathGrammerParser.MathContext):
        # print("enterMath")

        # #Elke keer als we een nieuwe lijn tegen komen betekent dat de parent een extra child gaat krijgen
        # #We voegen dus een placeholder toe aan de root zijn children
        # ast.root.children.append(None)
        #
        # #bij het enteren van een math beginnen we aan een nieuwe expressie/lijn code
        # #We resetten hier eigen dan de self.prevParents want we beginnen dan aan een nieuwe ast.
        # #Waarbij de eerste parent direct de root gewoon gaat zijn, dus deze voegen we al toe aan de lijst
        # ast.parentsList = [ast.root]
        #
        # #Het is wel zo dat we altijd een extra kind gaan toevoegen als None type en dat is niet de bedoeling
        # #We moeten zijn dat dit voorkomen wordt, we kunnen deze verwijderen als de child count == 1
        # #Want dan hebben we een EOF
        # if ctx.getChildCount() == 0:
        #     ast.root.children.pop()
        #     ast.parentsList = []

        for i in range(ctx.getChildCount() - 1):
            ast.root.children.append(None)

        ast.parentsList = [ast.root]

        if ctx.getChildCount() == 1:
            ast.root.children.pop()
            ast.parentsList = []

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx: mathGrammerParser.MathContext):

        for i in range(len(ast.root.children)):
            if ast.root.children[i] is None:
                ast.root.children.remove(ast.root.children[i])

    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        # print("enterComp_expr")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.EQ_OP(), "EQ_OP", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        # print("enterComp_expr1")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.COMP_OP(), "COMP_OP", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        # print("enterExpr")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.getChild(1), "BIN_OP1", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        # print("enterFactor")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.getChild(1), "BIN_OP2", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        # print("enterTerm")

        if ctx.getChildCount() > 1:

            if str(ctx.getChild(1)) != "++" and str(ctx.getChild(1)) != "--" and  str(ctx.getChild(0)) != "++" and str(ctx.getChild(0)) != "--":
                for x in range(ctx.getChildCount() - 1):
                    if ctx.getChild(ctx.getChildCount() - 1).start.text == "(" or ctx.getChild(
                            ctx.getChildCount() - 1).start.text == ctx.getChild(ctx.getChildCount() - 1).stop.text:
                        ast.createNode(ctx.getChild(x), "UN_OP", 1, ctx.start.line, ctx.start.column, "", False, False, True)
                    else:
                        ast.createNode(ctx.getChild(x), "UN_OP", 1, ctx.start.line, ctx.start.column)

            else:
                if str(ctx.getChild(0)) == "++":
                    ast.createNode(ctx.getChild(0), "UN_OP", 1, ctx.start.line, ctx.start.column)
                elif str(ctx.getChild(1)) == "++":
                    ast.createNode(ctx.getChild(1), "UN_OP", 1, ctx.start.line, ctx.start.column)
                elif str(ctx.getChild(0)) == "--":
                    ast.createNode(ctx.getChild(0), "UN_OP", 1, ctx.start.line, ctx.start.column)
                elif str(ctx.getChild(1)) == "--":
                    ast.createNode(ctx.getChild(1), "UN_OP", 1, ctx.start.line, ctx.start.column)


    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print("enterLog_op1")

        # Geen OR operation
        if ctx.getChildCount() == 1:
            # Dit is niet speciaal moet niets gebeuren we gaan gewoon verder door de parse tree
            pass
        # Een enkele OR operation
        elif ctx.getChildCount() == 3:
            # Hier bij hebben we een standaard geval
            # We kunnen hier al een parent aanmaken waarbij de value == ||
            # De 2 volgende waardes die we dan tegenkomen worden de kinderen van deze node
            ast.createNode("||", "LOG_OR", 2, ctx.start.line, ctx.start.column)

        # multiple OR operations
        else:
            # We maken al het aantal ORs die we hebben, de eerste OR wordt dan een child van de laatst aangemaakt parent
            # En Elke OR heeft dan nog 2 kinderen, waarbij telkens dan het eerste kind een nieuwe OR wordt
            numberOfORs = int((ctx.getChildCount() - 1) / 2)
            for x in range(numberOfORs):
                ast.createNode("||", "LOG_OR", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        # print("exitLog_op1")
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        # print("enterLog_op2")

        # Geen AND operation
        if ctx.getChildCount() == 1:
            # Dit is niet speciaal moet niets gebeuren we gaan gewoon verder door de parse tree
            pass
        # Een enkele AND operation
        elif ctx.getChildCount() == 3:
            ast.createNode("&&", "LOG_OR", 2, ctx.start.line, ctx.start.column)

        # multiple AND operations
        else:
            numberOfANDs = int((ctx.getChildCount() - 1) / 2)
            for x in range(numberOfANDs):
                ast.createNode("&&", "LOG_AND", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        # print("enterLog_op3")

        # Als we 1 kind hebben, is er niets speciaals
        # if ctx.getChildCount() == 1:
        #     pass

        # Anders hebben we 2 kinderen
        if ctx.getChildCount() == 2:
            if ctx.getChild(1).start.text == "(" or ctx.getChild(1).start.text == ctx.getChild(1).stop.text:
                ast.createNode("!", "LOG_NOT", 1, ctx.start.line, ctx.start.column, "", False, False, True)
            else:
                ast.createNode("!", "LOG_NOT", 1, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        # print("enterVar")

        if ctx.INT() and ctx.getChildCount() == 1:
            ast.createNode(ctx.INT(), "INT", 0, ctx.start.line, ctx.start.column)
        elif ctx.CHAR() and ctx.getChildCount() == 1:
            ast.createNode(ctx.CHAR(), "CHAR", 0, ctx.start.line, ctx.start.column)
        elif ctx.FLOAT() and ctx.getChildCount() == 1:
            ast.createNode(ctx.FLOAT(), "FLOAT", 0, ctx.start.line, ctx.start.column)
        elif ctx.IDENTIFIER() and ctx.getChildCount() == 1:
            ast.createNode(ctx.IDENTIFIER(), "IDENTIFIER", 0, ctx.start.line, ctx.start.column, ast.nextType, ast.nextConst, ast.nextOverwrite)
            if ast.nextConst:
                ast.nextConst = False
            ast.nextType = ""
            ast.nextOverwrite = False

    # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        pass

    # ------------------------------------------- Start new part--------------------------------------------------#

    # Enter a parse tree produced by mathGrammerParser#statement.
    def enterStatement(self, ctx: mathGrammerParser.StatementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#statement.
    def exitStatement(self, ctx: mathGrammerParser.StatementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#extern_decl.
    def enterExtern_decl(self, ctx: mathGrammerParser.Extern_declContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#extern_decl.
    def exitExtern_decl(self, ctx: mathGrammerParser.Extern_declContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#print_stmt.
    def enterPrint_stmt(self, ctx: mathGrammerParser.Print_stmtContext):
        ast.createNode(ctx.getChild(0), "PRINTF", 1, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#print_stmt.
    def exitPrint_stmt(self, ctx: mathGrammerParser.Print_stmtContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#function_def.
    def enterFunction_def(self, ctx: mathGrammerParser.Function_defContext):

        if ctx.getChildCount() == 4:
            ast.createNode("FUNC_DEF", "FUNC_DEF", 4, ctx.start.line, ctx.start.column)
        elif ctx.getChildCount() == 3:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print(ctx.getChild(2).getText())
            print(ctx.getChild(1).getText())
            print(ctx.getChild(1).getChildCount())
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            ast.createNode("FUNC_DEF", "FUNC_DEF", 4, ctx.start.line, ctx.start.column)
        else:
            pass

    # Exit a parse tree produced by mathGrammerParser#function_def.
    def exitFunction_def(self, ctx: mathGrammerParser.Function_defContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#declaration.
    def enterDeclaration(self, ctx: mathGrammerParser.DeclarationContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#declaration.
    def exitDeclaration(self, ctx: mathGrammerParser.DeclarationContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#decl_spec.
    def enterDecl_spec(self, ctx: mathGrammerParser.Decl_specContext):
        if ctx.getChildCount() == 2:
            ast.nextConst = True
        else:
            if ctx.CONST():
                ast.nextConst = True
            elif ctx.ttype():
                pass
            else: # geen type, e.g. x = 5
                ast.nextOverwrite = True

    # Exit a parse tree produced by mathGrammerParser#decl_spec.
    def exitDecl_spec(self, ctx: mathGrammerParser.Decl_specContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#init_decl_list.
    def enterInit_decl_list(self, ctx: mathGrammerParser.Init_decl_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#init_decl_list.
    def exitInit_decl_list(self, ctx: mathGrammerParser.Init_decl_listContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#init_declarator.
    def enterInit_declarator(self, ctx: mathGrammerParser.Init_declaratorContext):

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.getChild(1), "=", 2, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#init_declarator.
    def exitInit_declarator(self, ctx: mathGrammerParser.Init_declaratorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#declarator.
    def enterDeclarator(self, ctx: mathGrammerParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#declarator.
    def exitDeclarator(self, ctx: mathGrammerParser.DeclaratorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#initializer.
    def enterInitializer(self, ctx: mathGrammerParser.InitializerContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#initializer.
    def exitInitializer(self, ctx: mathGrammerParser.InitializerContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#direct_declarator.
    def enterDirect_declarator(self, ctx: mathGrammerParser.Direct_declaratorContext):

        if ctx.IDENTIFIER() and ctx.getChildCount() == 1:
            ast.createNode(ctx.IDENTIFIER(), "IDENTIFIER", 0, ctx.start.line, ctx.start.column, ast.nextType, ast.nextConst, ast.nextOverwrite)
            if ast.nextConst:
                ast.nextConst = False
            ast.nextType = ""
            ast.nextOverwrite = False

    # Exit a parse tree produced by mathGrammerParser#direct_declarator.
    def exitDirect_declarator(self, ctx: mathGrammerParser.Direct_declaratorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#initializer_list.
    def enterInitializer_list(self, ctx: mathGrammerParser.Initializer_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#initializer_list.
    def exitInitializer_list(self, ctx: mathGrammerParser.Initializer_listContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#ttype.
    def enterTtype(self, ctx: mathGrammerParser.TtypeContext):
        if ctx.CHAR_KEY():
            ast.nextType = "CHAR"
        elif ctx.INT_KEY():
            ast.nextType = "INT"
        elif ctx.FLOAT_KEY():
            ast.nextType = "FLOAT"

    # Exit a parse tree produced by mathGrammerParser#ttype.
    def exitTtype(self, ctx: mathGrammerParser.TtypeContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#pointer.
    def enterPointer(self, ctx: mathGrammerParser.PointerContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#pointer.
    def exitPointer(self, ctx: mathGrammerParser.PointerContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#reference.
    def enterReference(self, ctx: mathGrammerParser.ReferenceContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#reference.
    def exitReference(self, ctx: mathGrammerParser.ReferenceContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#type_qualifier_list.
    def enterType_qualifier_list(self, ctx: mathGrammerParser.Type_qualifier_listContext):
        ast.nextConst = True

    # Exit a parse tree produced by mathGrammerParser#type_qualifier_list.
    def exitType_qualifier_list(self, ctx: mathGrammerParser.Type_qualifier_listContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#pointersign.
    def enterPointersign(self, ctx: mathGrammerParser.PointersignContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#pointersign.
    def exitPointersign(self, ctx: mathGrammerParser.PointersignContext):
        pass

# ------------------------------------------- End new part --------------------------------------------------#

    # Enter a parse tree produced by mathGrammerParser#import_stat_list.
    def enterImport_stat_list(self, ctx: mathGrammerParser.Import_stat_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#import_stat_list.
    def exitImport_stat_list(self, ctx: mathGrammerParser.Import_stat_listContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#import_statement.
    def enterImport_statement(self, ctx: mathGrammerParser.Import_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#import_statement.
    def exitImport_statement(self, ctx: mathGrammerParser.Import_statementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#stat.
    def enterStat(self, ctx: mathGrammerParser.StatContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#stat.
    def exitStat(self, ctx: mathGrammerParser.StatContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#stat_list.
    def enterStat_list(self, ctx: mathGrammerParser.Stat_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#stat_list.
    def exitStat_list(self, ctx: mathGrammerParser.Stat_listContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_stat.
    def enterComp_stat(self, ctx: mathGrammerParser.Comp_statContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#comp_stat.
    def exitComp_stat(self, ctx: mathGrammerParser.Comp_statContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#it_statement.
    def enterIt_statement(self, ctx: mathGrammerParser.It_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#it_statement.
    def exitIt_statement(self, ctx: mathGrammerParser.It_statementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#sel_statement.
    def enterSel_statement(self, ctx: mathGrammerParser.Sel_statementContext):


        #begin met condition aan te maken
        #dan if node met zijn huidige info
        #dan else node als dit aanwezig is

        #condition == child 2

        if ctx.getChildCount() == 5:
            ast.createNode("BRANCH", "BRANCH", 2, ctx.start.line, ctx.start.column)

        elif ctx.getChildCount() == 7:
            ast.createNode("BRANCH", "BRANCH", 3, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#sel_statement.
    def exitSel_statement(self, ctx: mathGrammerParser.Sel_statementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#j_statement.
    def enterJ_statement(self, ctx: mathGrammerParser.J_statementContext):

        if ctx.CONTINUE():
            ast.createNode("CONTINUE", "CONTINUE", 0, ctx.start.line, ctx.start.column)
        elif ctx.BREAK():
            ast.createNode("BREAK", "BREAK", 0, ctx.start.line, ctx.start.column)
        elif ctx.RETURN():
            ast.createNode("RETURN", "RETURN", 1, ctx.start.line, ctx.start.column)

    # Exit a parse tree produced by mathGrammerParser#j_statement.
    def exitJ_statement(self, ctx: mathGrammerParser.J_statementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#expr_statement.
    def enterExpr_statement(self, ctx: mathGrammerParser.Expr_statementContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#expr_statement.
    def exitExpr_statement(self, ctx: mathGrammerParser.Expr_statementContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#declaration_list.
    def enterDeclaration_list(self, ctx: mathGrammerParser.Declaration_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#declaration_list.
    def exitDeclaration_list(self, ctx: mathGrammerParser.Declaration_listContext):
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

    # Enter a parse tree produced by mathGrammerParser#func_call.
    def enterFunc_call(self, ctx: mathGrammerParser.Func_callContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#func_call.
    def exitFunc_call(self, ctx: mathGrammerParser.Func_callContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#func_call_par_list.
    def enterFunc_call_par_list(self, ctx: mathGrammerParser.Func_call_par_listContext):
        pass

    # Exit a parse tree produced by mathGrammerParser#func_call_par_list.
    def exitFunc_call_par_list(self, ctx: mathGrammerParser.Func_call_par_listContext):
        pass

def createGraph(ast, inputfile, number=0):
    path = "./ast_files/"
    afterSlash = re.search("[^/]+$", inputfile)  # build folder changes inputfile path
    pos = afterSlash.start()
    inputfile = inputfile[pos:]
    graphname = str(inputfile[:len(inputfile) - 2]) + "_graph" + str(number) + ".gv"
    astname = str(inputfile[:len(inputfile) - 2]) + "_ast" + str(number) + ".png"

    graph_path = path + graphname

    f = open(graph_path, "w")

    f.write("strict digraph G{\n")  # we gebruiken een directed graph met max. één edge tussen twee vertices

    tempLabel = "l1"  # label die gebruikt wordt om nodes (kinderen) met dezelfde waarde te onderscheiden van elkaar.
    tempLabel2 = ""  # gelijkaardig aan tempLabel, maar tempLabel2 zorgt ervoor dat we de root juist onthouden en gebruiken.
    createVerticesAndEdges(tempLabel2, ast, f, tempLabel)

    f.write("}\n")

    f.close()

    os.chdir('./ast_files/')

    os.system(
        "dot -Tpng " + graphname + " -o " + astname)  # "run" command voor graphviz, "ast#.png" bevat het schema van de AST.

    os.chdir('../')


def createVerticesAndEdges(tempLabel2, ast, graphFile, tempLabel, node=None):
    # graphviz werkt op een manier waarbij, als je één vertice 'A' hebt,
    # die je naar twee aparte vertices wil laten gaan d.m.v. twee directed/undirected edges
    # waarbij de twee vertices dezelfde waarde (bv. 'B') bevatten, dat er maar één
    # vertice 'B' wordt aangemaakt met twee edges hiernaartoe vanuit 'A', wat niet de bedoeling is.
    # Het grotendeel van onderstaande code (gebruik van labels, tempLabel en dergelijke) probeert dit op te lossen.

    if ast.root is None:
        return None

    elif node is None:  # we zitten in de ROOT root
        if len(ast.root.children) > 0:

            tempLabels = []  # bevat de labels voor de kinderen, hebben we nodig voor de volgende for loop.
            for child in ast.root.children:
                tempLabel = tempLabel + "1"  # unieke templabel per kind.

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n")  # labeled vertices maken
                tempLabels.append(tempLabel)

            for child in range(len(ast.root.children)):

                graphFile.write("\"" + str(ast.root.value) + "\"" + "->")
                if len(ast.root.children[child].children) > 0:
                    graphFile.write(
                        "\"" + tempLabels[child] + "\"" + "\n")  # speciale tekens moeten tussen "" geplaatst worden.
                else:
                    graphFile.write(tempLabels[child] + "\n")
                tempLabel = tempLabel + "3"  # zodat er onder siblings geen zelfde labels ontstaan.
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, ast.root.children[child])
    else:  # we zitten in een node
        if len(node.children) > 0:

            a = False  # kleine contructie om te weten of we met het symbool zelf/met de label ervan moeten werken.
            # Als a False is en blijft, betekent dit dat we ergens in het begin van de boom zitten (merk de if-statement op),
            # en voor het eerste teken onder de root hoeven we niet te vervangen door de label
            if (tempLabel2 != ""):
                a = True

            tempLabels = []  # bevat de labels voor de kinderen, hebben we nodig voor de volgende for loop.
            for child in node.children:
                tempLabel = tempLabel + "1"  # unieke templabel per kind

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n")  # labeled vertices maken
                tempLabels.append(tempLabel)

            for child in range(len(node.children)):

                if (not a):
                    graphFile.write("\"" + str(node.value) + "\"" + "->")
                else:
                    graphFile.write("\"" + tempLabel2 + "\"" + "->")

                if len(node.children[child].children) > 0:
                    graphFile.write(
                        "\"" + tempLabels[child] + "\"" + "\n")  # speciale tekens moeten tussen "" geplaatst worden.
                else:
                    graphFile.write(tempLabels[child] + "\n")
                tempLabel = tempLabel + "3"  # zodat er onder siblings geen zelfde labels ontstaan.
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, node.children[child])


def optimizationVisitor(tree, table=False): # TODO verwijderen?
    # replaces every binary operation node that has
    # two literal nodes as children with a literal node containing the result of the operation.
    # Similarly, it also replaces every unary operation node that has a literal node as its
    # child with a literal node containing the result of the operation.

    newTree = AST()
    newTree.root = createNodeItem("ROOT", "ROOT", None)
    newNode = createNodeItem(tree.token, tree.value, tree.parent)
    childnumber = 0

    loopP = None
    node = None

    if table:
        loopP = tree.children
        node = newNode
    else:
        loopP = tree.root.children
        node = newTree.root

    for actAST in loopP:

        if len(actAST.children) > 0:
            optimized = True
            while optimized:
                # Geen optimalization nodig
                if var_list[1:len(var_list) - 1].count(actAST.token) or actAST.token == "ROOT":
                    optimized = False

                # We moeten gaan optimaliseren
                else:
                    actAST = optimize(actAST)

            node.children.append(actAST.children[childnumber])

        else:
            node.children.append(actAST)

        childnumber += 1

    return newTree


def prepConstanFolding(child):

    if child.token == "=":
        new = constantFolding(child.children[1])
        child.children[1].value = new[0]
        child.children[1].token = new[1]
        child.children[1].children = []
    elif child.token == "PRINTF":
        new = constantFolding(child.children[0])
        child.children[0].value = new[0]
        child.children[0].token = new[1]
        child.children[0].children = []


#########################################################################################################################
# Replaces every binary operation node that has two literal nodes as children with a literal node containing the result #
# of the operation.                                                                                                     #
# Similar for unary operations, it also replace every unary operation node that has a literal node as its               #
# child with a literal node containing the result of the operation.                                                     #
#########################################################################################################################
def constantFolding(tree):
    # We need to look first in what situation we are.
    # We look first at the token of the current node.
    # We can split these up in different parts.
    # 1) If the token is an Integer, Float. Then it cannot have any children so this is a base case
    #    and we cannot go any further in the ast.
    # 2) When the token is an operation like: BIN_OP1, BIN_OP2, etc. then we need to check the children
    #    of this node and check their token
    # So we start with point one. We can split these in 2 statements, so we can return the correct type.

    if tree.token == "INT":
        return int(str(tree.value)), "INT"  # value and token of this node

    elif tree.token == "FLOAT":
        return float(str(tree.value)), "FLOAT"  # value and token of this node

    elif tree.token == "CHAR":
        return str(tree.value), "CHAR"
    # When we didn't match the conditions for point one, we go to point 2.

    else:

        # We need to check what kind operation we need to operate.
        # First we check if it is a binary operation like +,-,*,/,%

        value = None
        token = None

        value_c0, value_c0_t = constantFolding(tree.children[0])
        value_c1, value_c1_t = constantFolding(tree.children[1]) if len(tree.children) == 2 else (None,None)

        if tree.token == "BIN_OP1" or tree.token == "BIN_OP2":

            if value_c0 is not None and value_c1 is not None:
                value_c0 = int(ord(value_c0[1])) if isinstance(value_c0, str) else value_c0
                value_c1 = int(ord(value_c1[1])) if isinstance(value_c1, str) else value_c1

            # Semantic Error
            if value_c0_t != value_c1_t:
                print("[ Warning ] line " + str(tree.children[0].line) + ", position " + str(
                    tree.children[0].column) + " : " + "Operation of incompatible types")

            bin_operations = {
                "+": value_c0 + value_c1,
                "-": value_c0 - value_c1,
                "*": value_c0 * value_c1,
                "/": value_c0 / value_c1,
                "%": value_c0 % value_c1
            }

            # Finding the value recursivly
            value = bin_operations[str(tree.value)]
            # Checking what type the value is, it is a int or a float.
            token = "INT" if isinstance(value, int) else "FLOAT"


        # We check if it is a logaritmise operation like ||, &&, !
        elif tree.token == "LOG_OR" or tree.token == "LOG_AND" or tree.token == "LOG_NOT":

            log_operations = {
                "||": value_c0 == 0 and value_c1 == 0,
                "&&": value_c0 == 0 or value_c1 == 0,
                "!": value_c0 != 0
            }

            # Checking if the value needs to be zero or one.
            value = 0 if log_operations[str(tree.value)] else 1
            # Because this always has value zero or one, the type always gonna be a integer.
            token = "INT"


        # We check if it is a comparison operation like <,>,<=,>=,==,!=
        elif tree.token == "COMP_OP" or tree.token == "EQ_OP":

            comp_operations = {
                ">": value_c0 > value_c1,
                "<": value_c0 < value_c1,
                "<=": value_c0 <= value_c1,
                ">=": value_c0 >= value_c1,
                "==": value_c0 == value_c1,
                "!=": value_c0 != value_c1
            }

            # Checking if the value needs to be zero or one.
            value = 1 if comp_operations[str(tree.value)] else 0
            # Because this always has value zero or one, the type always gonna be a interger.
            token = "INT"


        # We check if it is a unary operation like +,-
        elif tree.token == "UN_OP":
            # The value is just the return value of his child.
            value = -value_c0 if str(tree.value) == "-" else value_c0
            # Checking what type the value is, it is an int or a float.
            token = "INT" if isinstance(value, int) else "FLOAT"

        # At this moment we fold the full branch of this node and need to replace this node
        # with the new value and token.
        return value, token


#########################################################################################################################
# Replaces indentifiers in expressions with their value, if it is know at compile-time, before performing costant       #
# folding.                                                                                                              #
#########################################################################################################################
def constantPropagation(tree, node=None):
    """
    :param tree: The AST where constant propagation needs to be applied on.
    :return: A reconstructed AST, constructed by applying constant propagation on the input AST.
    """

    if node is None:  # Hebben we de root
        # count = 0
        if len(tree.root.children) > 0:
            for child in tree.root.children:
                constantPropagation(tree, child)
                prepConstanFolding(child)

    else:
        if node.token == "=":
            constantPropagation(tree, node.children[1])

        elif node.token == "IDENTIFIER":
            table = tableLookup(node)
            symbol_lookup = symbolLookup(node.value, table)
            if symbol_lookup[0] is True:
                s_list = symbol_lookup[1]
                if s_list.isConst or (symbol_lookup[2] and not s_list.isOverwritten):
                    # parent = node.parent
                    node.value = s_list.value.value
                    node.token = s_list.value.token
                    # node.token = s_list.type
                    # s_list.value = node
        else:
            if len(node.children) > 0:
                for child in node.children:
                    constantPropagation(tree, child)


def optimize(tree):

    constantPropagation(tree)

# ----------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################
# Looks for the symbol table that is connected to the current node, if the node hasn't a symbol table we look in        #
# the parent of this node. And so go on until we find the symbol table that belongs to the scope of this node.          #
#########################################################################################################################
def tableLookup(node):
    """
    :param node: The node where we are searching in for the symbol table
    :return: The symbol table that is connected to the node.
    """

    # First we check if the node has a pointer to a symbol table
    if node.symbolTablePointer is not None:
        return node.symbolTablePointer

    # The node doesn't have an pointer to a table so we look in the parents his node.
    return tableLookup(node.parent)


def symbolLookup(varName, symbolTable, sameScope=True): # zoekt in de symbol tables naar de variabele
    """

    :param varName: identifier (var) name
    :param symbolTable: current symbol table (current scope)
    :param sameScope: says if the variable is in the first symboltable we look in, so if this true, sameScope will be true
                      otherwise it will be false.
    :return: value of the symbol table entry (with key = varName) (which is a list)
    """

    if str(varName) in symbolTable.dict:
        return True, symbolTable.dict[str(varName)], sameScope
    else:
        if symbolTable.enclosingSTable is not None:
            return symbolLookup(varName, symbolTable.enclosingSTable, False)
        else:
            return False, None, None


def setupSymbolTables(tree, node=None):
    if tree.root is None:
        return None

    elif node is None:  # Hebben we de root

        # symbolTable = SymbolTable()

        if len(tree.root.children) > 0:

            for child in tree.root.children:
                setupSymbolTables(tree, child)
    else:
        ## geval 1: we openen een nieuw block

        if node.token == "FUNC_DEF":
            pass

        # symbolTable = SymbolTable()

        ## geval 2: we openen geen nieuw block
        if node.token == "=":

            value = node.children[1]

            type = node.children[0].type
            isConst = node.children[0].isConst

            # if len(node.children[1].children) != 0:  # optimizen
            #     pass
            isOverwritten = False
            if str(node.children[0].value) in tree.symbolTableStack[0].dict:
                isOverwritten = True

                for child in ast.root.children:
                    constantPropagation(ast, child)
                    if child == node:
                        break

                table = tableLookup(node.children[0])
                symbol_lookup = symbolLookup(node.children[0].value, table)
                type = symbol_lookup[1].type
                isConst = symbol_lookup[1].isConst # also in this statement

            semanticAnalysis(node, node.children[0], node.children[1])

            tableValue = Value(type, value, isConst, isOverwritten)
            tree.symbolTableStack[0].addVar(str(node.children[0].value), tableValue)

        elif node.token == "IDENTIFIER" and not node.parent.token == "=":
            semanticAnalysis(node)

        for child in node.children:
            setupSymbolTables(tree, child)

# ----------------------------------------------------------------------------------------------------------------------#

def semanticAnalysis(node, child1=None, child2=None):

    """
    Semantic errors:
    • Use of an undefined or uninitialized variable.
    • Redeclaration or redefinition of an existing variable.
    • Operations or assignments of incompatible types.
    • Assignment to an rvalue.
    • Assignment to a const variable.

     For example, for usage of a variable of the wrong type, you might output:
    “[ Error ] line 54, position 13: variable x has type y while it should be z”.

    :param tree: AST
    :param node: aiding parameter
    :return:
    """

    if child1 is None and child2 is None:
        # check for undefined reference
        table = tableLookup(node)
        symbol_lookup = symbolLookup(node.value, table)

        if symbol_lookup[0] is False:
            # Undefined reference.
            print("[ Error ] line " + str(node.line) + ", position " + str(node.column) + " : " + "Undefined or Uninitialized Reference.")
            exit(1)

    else:
        table = tableLookup(child1)
        symbol_lookup = symbolLookup(child1.value, table)

        if symbol_lookup[0] is False:
            if child1.type == "":
                # Undefined reference.
                print("[ Error ] line " + str(node.line) + ", position " + str(
                    node.column) + " : " + "Uninitialized Reference.")
                exit(1)
        else:

            # Redeclaration or redefinition of an existing variable.
            if child1.type != "":
                print("[ Error ] line " + str(node.line) + ", position " + str(
                    node.column) + " : " + "Duplicate declaration")
                exit(1)

            # Assignment to an rvalue.
            # if 5 == 4:
            #     print("[ Error ] line " + str(node.line) + ", position " + str(node.column) + " : " + "Assignment to an rvalue")

            # Assignment to a const variable.
            if symbol_lookup[1].isConst:
                print("[ Error ] line " + str(node.line) + ", position " + str(node.column) + " : " + "Assignment to a const variable")
                exit(1)

def semanticAnalysisVisitor(node):

    if node.token == "=":

        # table = tableLookup(node.children[0])
        # symbol_lookup = symbolLookup(node.children[0].value, table)

        table_child2 = tableLookup(node.children[1])
        symbol_lookup_child2 = symbolLookup(node.children[1].value, table_child2)

        if len(node.children[1].children) == 0: # if the right child doesn't have any children.
            if symbol_lookup_child2[0]: # if the right child is found in a symbol table.
                if node.children[0].type != symbol_lookup_child2[1].type:
                    # Operation or assignment of incompatible types.
                    print("[ Warning ] line " + str(node.line) + ", position " + str(
                        node.column) + " : " + "Assignment of incompatible types")
            else:
                child2Type = None

                if type(node.children[1].value) == float:
                    child2Type = "FLOAT"
                elif type(node.children[1].value) == int:
                    child2Type = "INT"
                elif type(node.children[1].value) == str and str(node.children[1].value)[0] == "\'":
                    child2Type = "CHAR"
                if node.children[0].type != child2Type:
                    print("[ Warning ] line " + str(node.line) + ", position " + str(
                        node.column) + " : " + "Assignment of incompatible types")
        else: # for a whole expression

            if node.children[0].type != evaluateExpressionType(node.children[1]):
                print("[ Warning ] line " + str(node.line) + ", position " + str(
                    node.line) + " : " + "Assignment of incompatible types")

    if len(node.children) > 0:
        for child in node.children:
            semanticAnalysisVisitor(child)

def evaluateExpressionType(node=None):

    if len(node.children) > 0:

        child0_type = evaluateExpressionType(node.children[0])
        child1_type = evaluateExpressionType(node.children[1])

        if child0_type != child1_type:
            print("[ Warning ] line " + str(node.line) + ", position " + str(
                node.column) + " : " + "Operation of incompatible types")

        node_type = ""

        if child0_type == "FLOAT" or child1_type == "FLOAT":
            node_type = "FLOAT"
        elif child0_type == "INT" or child1_type == "INT":
            node_type = "INT"
        else:
            node_type = "CHAR"

        return node_type

    else:

        table = tableLookup(node)
        symbol_lookup = symbolLookup(node.value, table)

        if symbol_lookup[0]:
            return symbol_lookup[1].type
        else:
            if type(node.value) == float:
                return "FLOAT"
            elif type(node.value) == int:
                return "INT"
            elif type(node.value) == str:
                return "CHAR"

# ----------------------------------------------------------------------------------------------------------------------#