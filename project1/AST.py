from mathGrammerListener import mathGrammerListener
from mathGrammerParser import mathGrammerParser
import os


def createNodeItem(token, value, parent):
    node = Node(token, value, parent)
    return node


class Node:

    def __init__(self, token, value, parent):
        self.value = value
        self.token = token
        self.parent = parent
        self.children = []

    def getValue(self):
        return self.value

    def getToken(self):
        return self.token


class AST:

    def __init__(self, root=None):
        self.root = root
        self.parentsList = []

    def createNode(self, value, token, numberOfChilds):
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
            node = createNodeItem(token, value, None)
            for i in range(numberOfChilds):
                node.children.append(None)
            self.root = node
            if token != "INT" and token != "!":
                self.parentsList.append(node)

        else:
            curParent = self.parentsList[len(self.parentsList) - 1]

            if token == "INT" or token == "!":
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinder aan toevoegen.
                node = createNodeItem(token, value, curParent)
                for i in range(len(curParent.children)):
                    if curParent.children[i] is None:
                        curParent.children[i] = node
                        break

            else:
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinderen aan toevoegen.
                node = createNodeItem(token, value, curParent)
                for i in range(numberOfChilds):
                    node.children.append(None)
                for i in range(len(curParent.children)):
                    if curParent.children[i] is None:
                        curParent.children[i] = node
                        break
                self.parentsList.append(node)

    def inorderTraversal(self,visit,node=None):

        if self.root is None:
            return None

        elif node is None: #Hebben we de root
            count = 0
            if len(self.root.children) > 0:
                for child in self.root.children:
                    self.inorderTraversal(visit, child)
                    count+=1
                    if count == len(self.root.children) / 2:
                        visit(self.root.value)

            else:
                #Heeft geen kinderen dus er is enkel een root
                visit(self.root.value)

        else:
            count = 0
            if len(node.children) > 0:
                for child in node.children:
                    self.inorderTraversal(visit, child)
                    count+=1
                    if count == len(node.children) / 2:
                        visit(node.value)
            else:
                #Heeft geen kinderen dus er is enkel een root
                visit(node.value)


ast = AST()

#De self.root kan eigenlijk nooit None zijn dan dus we voegen deze gewoon al toe aan het begin van de expressie
ast.root = createNodeItem("ROOT", "ROOT", None)


class ASTprinter(mathGrammerListener):

    def __init__(self):
        self.prevParents = []

    # Enter a parse tree produced by mathGrammerParser#math.
    def enterMath(self, ctx: mathGrammerParser.MathContext):

        #Elke keer als we een nieuwe lijn tegen komen betekent dat de parent een extra child gaat krijgen
        #We voegen dus een placeholder toe aan de root zijn children
        ast.root.children.append(None)

        #bij het enteren van een math beginnen we aan een nieuwe expressie/lijn code
        #We resetten hier eigen dan de self.prevParents want we beginnen dan aan een nieuwe ast.
        #Waarbij de eerste parent direct de root gewoon gaat zijn, dus deze voegen we al toe aan de lijst
        ast.parentsList = [ast.root]

        #Het is wel zo dat we altijd een extra kind gaan toevoegen als None type en dat is niet de bedoeling
        #We moeten zijn dat dit voorkomen wordt, we kunnen deze verwijderen als de child count == 1
        #Want dan hebben we een EOF
        if ctx.getChildCount() == 1:
            ast.root.children.pop()
            ast.parentsList = []

    # Exit a parse tree produced by mathGrammerParser#math.
    def exitMath(self, ctx: mathGrammerParser.MathContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr.
    def enterComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        if ctx.getChildCount() == 3:
            ast.createNode(ctx.EQ_OP(), "EQ_OP", 2)

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        if ctx.getChildCount() == 3:
            ast.createNode( ctx.COMP_OP(), "COMP_OP", 2)

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        if ctx.getChildCount() == 3:
            ast.createNode(ctx.BIN_OP1(), "BIN_OP1", 2)

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        if ctx.getChildCount() == 3:
            ast.createNode( ctx.BIN_OP2(), "BIN_OP2", 2)

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        if ctx.getChildCount() == 2:
            ast.createNode( ctx.UN_OP(), "UN_OP", 1)

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        if ctx.getChildCount() > 1:
            for log in ctx.LOG_OR():
                ast.createNode( log, "LOG_OR", ctx.getChildCount()-1)

    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx: mathGrammerParser.Log_op1Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        if ctx.getChildCount() > 1:
            for log in ctx.LOG_AND():
                ast.createNode( log, "LOG_AND", ctx.getChildCount()-1)

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        if ctx.getChildCount() > 1:
            ast.createNode( ctx.LOG_NOT(), "LOG_NOT", ctx.getChildCount()-1)

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        if ctx.INT() is None: # speciale regel => zie grammar
            return
        if ctx.getChildCount() == 1:
            ast.createNode( ctx.INT(), "INT", 0)

    # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        pass


def createGraph(ast):
    f = open("graph.gv", "w")

    f.write("strict digraph G{\n") # we gebruiken een directed graph met max. één edge tussen twee vertices

    tempLabel = "l1" # label die gebruikt wordt om nodes (kinderen) met dezelfde waarde te onderscheiden van elkaar.
    tempLabel2 = "" # gelijkaardig aan tempLabel, maar tempLabel2 zorgt ervoor dat we de root juist onthouden en gebruiken.
    createVerticesAndEdges(tempLabel2, ast, f, tempLabel)

    f.write("}\n")

    f.close()
    os.system("dot -Tpng graph.gv -o ast.png") # "run" command voor graphviz, "ast.png" bevat het schema van de AST.

def createVerticesAndEdges(tempLabel2, ast, graphFile, tempLabel, node=None):

    # graphviz werkt op een manier waarbij, als je één vertice 'A' hebt,
    # die je naar twee aparte vertices wil laten gaan d.m.v. twee directed/undirected edges
    # waarbij de twee vertices dezelfde waarde (bv. 'B') bevatten, dat er maar één
    # vertice 'B' wordt aangemaakt met twee edges hiernaartoe vanuit 'A', wat niet de bedoeling is.
    # Het grotendeel van onderstaande code (gebruik van labels, tempLabel en dergelijke) probeert dit op te lossen.

    if ast.root is None:
        return None

    elif node is None: # we zitten in de ROOT root
        if len(ast.root.children) > 0:

            tempLabels = [] # bevat de labels voor de kinderen, hebben we nodig voor de volgende for loop.
            for child in ast.root.children:
                tempLabel = tempLabel + "1" # unieke templabel per kind.

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n") # labeled vertices maken
                tempLabels.append(tempLabel)

            for child in range(len(ast.root.children)):

                graphFile.write("\"" + str(ast.root.value) + "\"" + "->")
                if len(ast.root.children[child].children) > 0:
                    graphFile.write("\"" + tempLabels[child] + "\"" + "\n") # speciale tekens moeten tussen "" geplaatst worden.
                else:
                    graphFile.write(tempLabels[child] + "\n")
                tempLabel = tempLabel + "3" # zodat er onder siblings geen zelfde labels ontstaan.
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, ast.root.children[child])
    else: # we zitten in een node
        if len(node.children) > 0:

            a = False # kleine contructie om te weten of we met het symbool zelf/met de label ervan moeten werken.
            # Als a False is en blijft, betekent dit dat we ergens in het begin van de boom zitten (merk de if-statement op),
            # en voor het eerste teken onder de root hoeven we niet te vervangen door de label
            if (tempLabel2 != ""):
                a = True

            tempLabels = [] # bevat de labels voor de kinderen, hebben we nodig voor de volgende for loop.
            for child in node.children:
                tempLabel = tempLabel + "1" # unieke templabel per kind

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n") # labeled vertices maken
                tempLabels.append(tempLabel)

            for child in range(len(node.children)):

                if (not a):
                    graphFile.write("\"" + str(node.value) + "\"" + "->")
                else:
                    graphFile.write("\"" + tempLabel2 + "\"" + "->")

                if len(node.children[child].children) > 0:
                    graphFile.write("\"" + tempLabels[child] + "\"" + "\n") # speciale tekens moeten tussen "" geplaatst worden.
                else:
                    graphFile.write(tempLabels[child] + "\n")
                tempLabel = tempLabel + "3" # zodat er onder siblings geen zelfde labels ontstaan.
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, node.children[child])


def optimizationVisitor():

    # replaces every binary operation node that has
    # two literal nodes as children with a literal node containing the result of the operation.
    # Similarly, it also replaces every unary operation node that has a literal node as its
    # child with a literal node containing the result of the operation.

    pass