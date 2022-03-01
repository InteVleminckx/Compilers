from mathGrammerListener import mathGrammerListener
from mathGrammerParser import mathGrammerParser


# void AST::createAstDot() {
#
#     m_astFile.clear();
#
#     m_astFile << "digraph G{" << "\n";
#
#     makeAllNodes();
#     makeAllEdges();
#
#     m_astFile << "}" << "\n";
#     m_astFile.close();
#
#     system("dot -Tpng ast.dot -o ast.png");
# }
#
# void AST::makeAllNodes(const shared_ptr<ast::Node> &curNode) {
#
#     static int nodeNumber = 0;
#
#     //root
#     if (curNode == nullptr){
#         m_astFile << "n" << nodeNumber << "[label=<<B>" << m_root->m_token << "</B>>, color=\"#FF595E\", fontcolor=\"#FF595E\"]" << endl;
#         m_root->m_dotNode = to_string(nodeNumber);
#         for (const auto& child : m_root->m_childeren) {
#             nodeNumber++;
#             if (child->m_isLeaf){
#                 string token;
#                 if (child->m_token == "<"){
#                     token = "lt";
#                 }
#                 else if (child->m_token == ">"){
#                     token = "gt";
#                 }
#                 else if (child->m_token == "<="){
#                     token = "lte";
#                 }
#                 else if (child->m_token == ">="){
#                     token = "gte";
#                 }
#                 else{
#                     token = child->m_token;
#                 }
#                 m_astFile << "n" << nodeNumber << "[label=<<B> " << token << " </B>>, color=\"#242038\", fontcolor=\"#242038\"]" << endl;
#                 child->m_dotNode = to_string(nodeNumber);
#             }
#             else{
#                 makeAllNodes(child);
#             }
#         }
#         //reset de node number.
#         nodeNumber = 0;
#     }
#         //no root
#     else {
#         m_astFile << "n" << nodeNumber << "[label=<<B>" << curNode->m_token << "</B>>, color=\"#FF595E\", fontcolor=\"#FF595E\"]" << endl;
#         curNode->m_dotNode = to_string(nodeNumber);
#         for (const auto& child : curNode->m_childeren) {
#             nodeNumber++;
#             if (child->m_isLeaf){
#                 string token;
#                 if (child->m_token == "<"){
#                     token = "lt";
#                 }
#                 else if (child->m_token == ">"){
#                     token = "gt";
#                 }
#                 else if (child->m_token == "<="){
#                     token = "lte";
#                 }
#                 else if (child->m_token == ">="){
#                     token = "gte";
#                 }
#                 else{
#                     token = child->m_token;
#                 }
#                 m_astFile << "n" << nodeNumber << "[label=<<B> " << token << " </B>>, color=\"#242038\", fontcolor=\"#242038\"]" << endl;
#                 child->m_dotNode = to_string(nodeNumber);
#             }
#             else{
#                 makeAllNodes(child);
#             }
#         }
#     }
#
# }
#
# void AST::makeAllEdges(const shared_ptr<ast::Node> &curNode) {
#     //root
#     if (curNode == nullptr){
#         for (const auto& child : m_root->m_childeren) {
#             if (child->m_isLeaf){
#                 m_astFile << "n" << m_root->m_dotNode << "->n" << child->m_dotNode << "[color=\"#242038\"]" << endl;
#             }
#             else{
#                 m_astFile << "n" << m_root->m_dotNode << "->n" << child->m_dotNode << "[color=\"#FF595E\"]" << endl;
#                 makeAllEdges(child);
#             }
#         }
#     }
#
#         //no root
#     else {
#         for (const auto& child : curNode->m_childeren) {
#             if (child->m_isLeaf){
#                 m_astFile << "n" << curNode->m_dotNode << "->n" << child->m_dotNode << "[color=\"#242038\"]" << endl;
#             }
#             else{
#                 m_astFile << "n" << curNode->m_dotNode << "->n" << child->m_dotNode << "[color=\"#FF595E\"]" << endl;
#                 makeAllEdges(child);
#             }
#         }
#     }


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
                # We nemen de laatste parent in de list, want deze is als laatste toegevoegd en moeten daar dan de kinder aan toevoegen.
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


class ASTprinter(mathGrammerListener):

    def __init__(self):
        self.prevParents = []

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
            ast.createNode(ctx.EQ_OP(), "EQ_OP", 2)

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
            ast.createNode( ctx.COMP_OP(), "COMP_OP", 2)
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
            ast.createNode(ctx.BIN_OP1(), "BIN_OP1", 2)

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
            ast.createNode( ctx.BIN_OP2(), "BIN_OP2", 2)

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
            ast.createNode( ctx.UN_OP(), "UN_OP", 1)

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
                ast.createNode( log, "LOG_OR", ctx.getChildCount()-1)

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
                ast.createNode( log, "LOG_AND", ctx.getChildCount()-1)

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
            ast.createNode( ctx.LOG_NOT(), "LOG_NOT", ctx.getChildCount()-1)

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
            ast.createNode( ctx.INT(), "INT", 0)
            # print("var heeft 1 child")
        else: # if there are 3 children
            print(ctx.INT())
            # print("var heeft 3 children")

        # Exit a parse tree produced by mathGrammerParser#var.
    def exitVar(self, ctx: mathGrammerParser.VarContext):
        # # print(ctx)
        # print("exitVar")
        pass
