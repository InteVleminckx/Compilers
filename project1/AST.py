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
        self.unaries = []

    def createNode(self, value, token, numberOfChilds, unaryParenth=False):
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
            if token != "INT":
                self.parentsList.append(node)

        else:
            curParent = self.parentsList[len(self.parentsList) - 1]

            if token == "INT":
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinder aan toevoegen.
                node = createNodeItem(token, value, curParent)
                for i in range(len(curParent.children)):
                    if curParent.children[i] is None:
                        curParent.children[i] = node
                        break

            elif token == "LOG_NOT" and not unaryParenth:
                self.unaries.append((token, value))

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

                if len(self.unaries) != 0:
                    for unary in self.unaries:
                        curParent = self.parentsList[len(self.parentsList) - 1]

                        node = createNodeItem(unary[0], unary[1], curParent)
                        node.children.append(None)
                        for i in range(len(curParent.children)):
                            if curParent.children[i] is None:
                                curParent.children[i] = node
                                break
                        self.parentsList.append(node)

                    self.unaries = []


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
        print("enterMath")


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
        print("enterComp_expr")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.EQ_OP(), "EQ_OP", 2)

    # Exit a parse tree produced by mathGrammerParser#comp_expr.
    def exitComp_expr(self, ctx: mathGrammerParser.Comp_exprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#comp_expr1.
    def enterComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        print("enterComp_expr1")

        if ctx.getChildCount() == 3:
            ast.createNode( ctx.COMP_OP(), "COMP_OP", 2)

    # Exit a parse tree produced by mathGrammerParser#comp_expr1.
    def exitComp_expr1(self, ctx: mathGrammerParser.Comp_expr1Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#expr.
    def enterExpr(self, ctx: mathGrammerParser.ExprContext):
        print("enterExpr")

        if ctx.getChildCount() == 3:
            ast.createNode(ctx.BIN_OP1(), "BIN_OP1", 2)

    # Exit a parse tree produced by mathGrammerParser#expr.
    def exitExpr(self, ctx: mathGrammerParser.ExprContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#factor.
    def enterFactor(self, ctx: mathGrammerParser.FactorContext):
        print("enterFactor")

        if ctx.getChildCount() == 3:
            ast.createNode( ctx.BIN_OP2(), "BIN_OP2", 2)

    # Exit a parse tree produced by mathGrammerParser#factor.
    def exitFactor(self, ctx: mathGrammerParser.FactorContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#term.
    def enterTerm(self, ctx: mathGrammerParser.TermContext):
        print("enterTerm")

        if ctx.getChildCount() == 2:
            ast.createNode( ctx.UN_OP(), "UN_OP", 1)

    # Exit a parse tree produced by mathGrammerParser#term.
    def exitTerm(self, ctx: mathGrammerParser.TermContext):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op1.
    def enterLog_op1(self, ctx:mathGrammerParser.Log_op1Context):
        print("enterLog_op1")

        #Geen OR operation
        if ctx.getChildCount() == 1:
            #Dit is niet speciaal moet niets gebeuren we gaan gewoon verder door de parse tree
            pass
        #Een enkele OR operation
        elif ctx.getChildCount() == 3:
            #Hier bij hebben we een standaard geval
            #We kunnen hier al een parent aanmaken waarbij de value == ||
            #De 2 volgende waardes die we dan tegenkomen worden de kinderen van deze node
            ast.createNode("||", "LOG_OR", 2)

        #multiple OR operations
        else:
            #We maken al het aantal ORs die we hebben, de eerste OR wordt dan een child van de laatst aangemaakt parent
            #En Elke OR heeft dan nog 2 kinderen, waarbij telkens dan het eerste kind een nieuwe OR wordt
            numberOfORs = int((ctx.getChildCount()-1)/2)
            for x in range(numberOfORs):
                ast.createNode("||", "LOG_OR", 2)


    # Exit a parse tree produced by mathGrammerParser#log_op1.
    def exitLog_op1(self, ctx:mathGrammerParser.Log_op1Context):
        print("exitLog_op1")


    # Enter a parse tree produced by mathGrammerParser#log_op2.
    def enterLog_op2(self, ctx:mathGrammerParser.Log_op2Context):
        print("enterLog_op2")

        # Geen AND operation
        if ctx.getChildCount() == 1:
            #Dit is niet speciaal moet niets gebeuren we gaan gewoon verder door de parse tree
            pass
        # Een enkele AND operation
        elif ctx.getChildCount() == 3:
            ast.createNode("&&", "LOG_OR", 2)

        # multiple AND operations
        else:
            numberOfANDs = int((ctx.getChildCount() - 1) / 2)
            for x in range(numberOfANDs):
                ast.createNode("&&", "LOG_AND", 2)

    # Exit a parse tree produced by mathGrammerParser#log_op2.
    def exitLog_op2(self, ctx: mathGrammerParser.Log_op2Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#log_op3.
    def enterLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        print("enterLog_op3")

        #Als we 1 kind hebben, is er niets speciaals
        if ctx.getChildCount() == 1:
            pass

        #Anders hebben we 2 kinderen
        elif ctx.getChildCount() == 2:
            if ctx.getChild(1).start.text == "(":
                ast.createNode("!", "LOG_NOT", 1, True)
            else:
                ast.createNode("!", "LOG_NOT", 1)

    # Exit a parse tree produced by mathGrammerParser#log_op3.
    def exitLog_op3(self, ctx: mathGrammerParser.Log_op3Context):
        pass

    # Enter a parse tree produced by mathGrammerParser#var.
    def enterVar(self, ctx: mathGrammerParser.VarContext):
        print("enterVar")

        if ctx.INT() is None: # speciale regel => zie grammar
            return
        if ctx.getChildCount() == 1:
            ast.createNode( ctx.INT(), "INT", 0)

    # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        pass


def createGraph(ast, number=0):
    graphname = "graph" + str(number) + ".gv"
    astname = "ast" + str(number) + ".png"
    f = open(graphname, "w")

    f.write("strict digraph G{\n") # we gebruiken een directed graph met max. één edge tussen twee vertices

    tempLabel = "l1" # label die gebruikt wordt om nodes (kinderen) met dezelfde waarde te onderscheiden van elkaar.
    tempLabel2 = "" # gelijkaardig aan tempLabel, maar tempLabel2 zorgt ervoor dat we de root juist onthouden en gebruiken.
    createVerticesAndEdges(tempLabel2, ast, f, tempLabel)

    f.write("}\n")

    f.close()
    os.system("dot -Tpng " + graphname + " -o " + astname) # "run" command voor graphviz, "ast#.png" bevat het schema van de AST.

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


def optimizationVisitor(tree):

    # replaces every binary operation node that has
    # two literal nodes as children with a literal node containing the result of the operation.
    # Similarly, it also replaces every unary operation node that has a literal node as its
    # child with a literal node containing the result of the operation.

    newTree = AST()
    newTree.root = createNodeItem("ROOT", "ROOT", None)
    childnumber = 0
    for actAST in tree.root.children:

        if len(actAST.children) > 0:
            optimized = True
            while optimized:
                # Geen optimalization nodig
                if actAST.token == "INT" or actAST.token == "ROOT":
                    optimized = False

                # We moeten gaan optimaliseren
                else:
                    actAST = optimize(actAST)

            newTree.root.children.append(actAST.children[childnumber])

        else:
            newTree.root.children.append(actAST)

        childnumber += 1

    return newTree


def optimize(tree):


    # Eerst kijken we of de kinderen enkel integers zijn of niet

    onlyInt = True
    placeOp = 0

    for child in tree.children:
        if child.token != "INT":
            onlyInt = False
            break
        placeOp += 1

    # We hebben enkel integers als kinderen dus we kunnen deze optellen
    if onlyInt:
        value = 0
        if tree.token == "BIN_OP1" or tree.token == "BIN_OP2":

            if str(tree.value) == "+":
                value = float(str(tree.children[0].value)) + float(str(tree.children[1].value))
            elif str(tree.value) == "-":
                value = float(str(tree.children[0].value)) - float(str(tree.children[1].value))
            elif str(tree.value) == "*":
                value = float(str(tree.children[0].value)) * float(str(tree.children[1].value))
            elif str(tree.value) == "/":
                value = float(str(tree.children[0].value)) / float(str(tree.children[1].value))
            elif str(tree.value) == "%":
                value = float(str(tree.children[0].value)) % float(str(tree.children[1].value))

        elif tree.token == "LOG_OR" or tree.token == "LOG_AND" or tree.token == "LOG_NOT":
            if str(tree.value) == "||":
                if float(str(tree.children[0].value)) == 0 and float(str(tree.children[1].value)) == 0:
                    value = 0
                else:
                    value = 1
            elif str(tree.value) == "&&":
                if float(str(tree.children[0].value)) == 0 or float(str(tree.children[1].value)) == 0:
                    value = 0
                else:
                    value = 1
            elif str(tree.value) == "!":
                if float(str(tree.children[0].value)) == 0:
                    value = 1
                else:
                    value = 0

        elif tree.token == "COMP_OP" or tree.token == "EQ_OP":
            if str(tree.value) == ">":
                if float(str(tree.children[0].value)) > float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0
            elif str(tree.value) == "<":
                if float(str(tree.children[0].value)) < float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0
            elif str(tree.value) == "<=":
                if float(str(tree.children[0].value)) <= float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0
            elif str(tree.value) == ">=":
                if float(str(tree.children[0].value)) >= float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0
            elif str(tree.value) == "==":
                if float(str(tree.children[0].value)) == float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0
            elif str(tree.value) == "!=":
                if float(str(tree.children[0].value)) != float(str(tree.children[1].value)):
                    value = 1
                else:
                    value = 0

        elif tree.token == "UN_OP":
            if str(tree.value) == "+":
                pass
            elif str(tree.value) == "-":
                pass

        tree.value = str(value)
        tree.children = []
        tree.token = "INT"

        return tree.parent

    else:

        return optimize(tree.children[placeOp])
