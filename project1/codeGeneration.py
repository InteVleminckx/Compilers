from AST import *

registerCount = 1

types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1")}


def toLLVM(tree):

    file = open("tempFolder/llvmCode1.ll", "w")

    if tree.root is None:
        return

    generate(tree.root, file)

    file.close()

def generate(node, file):

    # We controleren eerst of er geen globale variable zijn aangemaakt
    # We controleren dus eerst of we in de root zitten
    # Controleren ook ineens of er wel globale variable zijn, anders is dit overbodig
    if node.value == "ROOT" and len(node.symbolTablePointer.dict) > 0:
        table = node.symbolTablePointer.dict
        for key in table:
            file.write(globall(str(key), table[key].value.token, table[key].value.value))

    for child in node.children:
        # We weten dat de parent alle informatie bevat over de functie want
        # deze bevat de symboltable
        if child.token == "FUNC_DEF":
            file.write("\n")
            file.write(function(child.parent.symbolTablePointer.dict))

        elif child.token == "=":
            # store()
            pass
        generate(child, file)

def globall(name, type, value):
    line = "@" + name + " = dso_local global " + types[type][0] + " "

    if type == "CHAR":
        line += str(ord(str(value)[1]))
    elif type == "FLOAT":
        placedot = 0
        for cha in str(value):
            if cha != '.':
                placedot += 1
            else:
                break
        line += str(value)
        for i in range(7-len(str(value)[placedot:len(str(value))])):
            line += "0"
        line += "e+00"

    else:
        line += str(value)

    line += ", " + types[type][1] + "\n"
    return line


def allocate(register):
    pass

def store(register, type, value):
    pass

def function(table):

    name = None
    parameters = []
    type = []
    for key in table:
        if table[key].value.token == "FUNC_DEF":
            name = str(key)
            parameters = table[key].functionParamaters
            type = table[key].outputTypes

    line = "; Function Attrs: noinline nounwind optnone uwtable\ndefine dso_local "

    if len(type) == 1 and type[0] is None:
        line += "void "
    elif len(type) >= 1:
        for i, tt in enumerate(type):
            line += types[tt][0]
            if i < len(type)-1:
                line += ", "

    line += " @" + name + "("

    regCount = 0
    for key in table:
        for register,para in enumerate(parameters):
            if str(para) == str(key):
                table[key].register = register
                line += types[table[key].type][0] + " %" + str(register)
                regCount = register
                if register < len(parameters) - 1:
                    line += ", "
                break

    line += ") #0 {\n"



    return line


def returnn(type, register):
    pass



def codeGenerator(tree):
    f = open("generatedLLVMIR_files/llvmCode1.ll", "w")
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
