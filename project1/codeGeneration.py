from AST import *

registerCount = 1

def codeGenerator(tree):
    f = open("generatedLLVMIR_files/llvmCode.ll", "w")
    codeGenerationVisitor(f, tree)
    storeValues(f, tree)
    f.close()


def codeGenerationVisitor(file, tree):
    generateRegisters(file, tree)


def generateRegisters(file, tree):
    global registerCount
    for child in tree.root.children:
        if child.token == "=":
            if child.children[0].isOverwritten is False:
                table = tableLookup(child.children[0])
                list_s = symbolLookup(child.children[0].value, table)
                if list_s[0]:
                    list_s[1].register = registerCount

                    type = ""
                    align = "4"
                    if list_s[1].type == "INT":
                        type = "i32"

                    elif list_s[1].type == "FLOAT":
                        type = "float"

                    elif list_s[1].type == "CHAR":
                        type = "i8"
                        align = "1"

                    file.write("%" + str(registerCount) + " = alloca " + type + ", align " + align + "\n")

                registerCount += 1


def storeValues(file, tree):
    global registerCount
    for child in tree.root.children:
        if child.token == "=":
            table = tableLookup(child.children[0])
            list_s = symbolLookup(child.children[0].value, table)
            if list_s[0]:
                #We have a single value
                if len(child.children[1].children) == 0:
                    type = None
                    value = None
                    align = "4"

                    if list_s[1].type == "INT":
                        type = "i32"
                        value = str(list_s[1].value.value)

                    elif list_s[1].type == "FLOAT":
                        type = "float"
                        value = str(list_s[1].value.value)

                    elif list_s[1].type == "CHAR":
                        type = "i8"
                        value = str(ord(list_s[1].value.value[1]))
                        align = "1"

                    file.write("store " + type + " " + value + ", " + type + "* %" + str(list_s[1].register) + ", align " + align + "\n")


            #ToDo: At this momement when we optimizen the ast al expression are calculated so we don't need to add other things then what we now have for llvm.

def add(file, var1, var2, type):
    pass


def subtract(file, var1, var2, type):  # var1 - var2
    pass


def multiply(file, var1, var2, type):
    pass


def divide(file, var1, var2, type):  # var1 / var2
    pass


# def traverse(ast, node=None):
#     if ast.root is None:
#         return None
#
#     elif node is None:  # Hebben we de root
#
#         visit(ast.root.value)
#
#         if len(ast.root.children) > 0:
#             pass
#             # for child in ast.root.children:
#             #     if child.token == "=":
#             #
#             #     ast.traverse(ast, child)
#     else:
#         visit(node.value)
#         if len(node.children) > 0:
#             pass
#             # for child in node.children:
#             #     ast.traverse(ast, child)
#
#
# def visit(value):
#     if value == "=":
#         pass
#     elif value == "printf":
#         pass
























def assign(file, var1, var2):
    pass
