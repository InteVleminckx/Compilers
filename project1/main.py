import sys
from antlr4 import *
from mathGrammerLexer import mathGrammerLexer
from mathGrammerParser import mathGrammerParser
from AST import *

import os

def createGraph(ast):
    f = open("graph.gv", "w")

    f.write("strict digraph G{\n")

    tempLabel = "l1"
    tempLabel2 = ""
    createVerticesAndEdges(tempLabel2, ast, f, tempLabel)

    # f.write("B1 [label=\"B\"]\n")
    # f.write("B2 [label=\"B\"]\n")
    # f.write("A -> B1\n")
    # f.write("A -> B2\n")
    # f.write("B1 -> C\n")

    f.write("}\n")

    f.close()
    os.system("dot -Tpng graph.gv -o ast.png")

def createVerticesAndEdges(tempLabel2, ast, graphFile, tempLabel, node=None):

    if ast.root is None:
        return None

    elif node is None: # root root
        if len(ast.root.children) > 0:
            a = False
            if (tempLabel2 != ""):
                a = True

            tempLabels = []
            for child in ast.root.children:
                tempLabel = tempLabel + "1"

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n")
                tempLabels.append(tempLabel)

            for child in range(len(ast.root.children)):

                graphFile.write("\"" + str(ast.root.value) + "\"" + "->")
                if (len(ast.root.children[child].children) > 0):
                    graphFile.write("\"" + tempLabels[child] + "\"" + "\n")
                else:
                    graphFile.write(tempLabels[child] + "\n")

                tempLabel = tempLabel + "3"
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, ast.root.children[child])

    else:
        if len(node.children) > 0:

            a = False
            if (tempLabel2 != ""):
                a = True

            tempLabels = []
            for child in node.children:
                tempLabel = tempLabel + "1"

                graphFile.write(tempLabel + "[label = \"" + str(child.value) + "\"]" + "\n")
                tempLabels.append(tempLabel)

            for child in range(len(node.children)):

                if (not a):
                    graphFile.write("\"" + str(node.value) + "\"" + "->")
                else:
                    graphFile.write("\"" + tempLabel2 + "\"" + "->")  # str(node.value)

                if len(node.children[child].children) > 0:
                    graphFile.write("\"" + tempLabels[child] + "\"" + "\n")
                else:
                    graphFile.write(tempLabels[child] + "\n")
                tempLabel = tempLabel + "3"
                createVerticesAndEdges(tempLabels[child], ast, graphFile, tempLabel, node.children[child])

def printA(a, root):

    if root and root is not None:
        if len(a.root.children) != 0:
            for i in range(len(a.root.children)):
                if i == 1:
                    print(a.root.value)

                printA(a.root.children[i], False)
        else:
            print(a.root.value)

    elif a is not None:
        if len(a.children) != 0:
            for i in range(len(a.children)):

                if i == 1:
                    print(a.value)

                printA(a.children[i], False)

        else:
            print(a.value)


def main(argv):

    input_stream = FileStream(argv[1])
    lexer = mathGrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathGrammerParser(stream)
    tree = parser.math()
    printer = ASTprinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    a = ast
    print("-------------------------------------------------")
    printA(a,True)
    # a.inorderTraversal(print)
    print("-------------------------------------------------")

    createGraph(a)



if __name__ == '__main__':
    main(sys.argv)