from AST import *

registerCount = 1

types = {"INT": ("i32", "align 4"), "FLOAT": ("float", "align 4"), "CHAR": ("i8", "align 1")}

class funcNode:

    def __init__(self, line, number, state, register):
        self.line = line
        self.functionNumber = number
        self.isOpen = state
        self.registerCounter = register

class LLVM:

    def __init__(self, tree):
        self.tree = tree
        self.strings = list()
        self.attributes = list()
        self.file = None
        self.functions = list()

    def toLLVM(self):

        self.file = open("tempFolder/llvmCode1.ll", "w")

        if self.tree.root is None:
            return

        self.generateLLVM(self.tree.root)

        self.file.close()


    def generateLLVM(self, node):

        for child in node.children:
            if child.value == "FUNC_DEF":
                self.function(child)

            elif child.value == "RETURN":
                self.returnFunction(node)
            elif child.token == "PRINTF":
                self.
            print(child.value)
            self.generateLLVM(child)


    # def addition(self, value, var, register, float=False):
    #     """
    #     :param value: De waarde/andere variable die bij de var wordt opgeteld (node)
    #     :param var: De variable waar de value wordt opgeteld. (node)
    #     :param register: Het register nummer waar we de uitkomst in wegschrijven
    #     :param float: Geeft aan of een een add of fadd is.
    #     :return: De register nummber en de line die wegschreven moeten worden in het bestand
    #     """
    #
    #     #0 = value, 1 = var
    #     registers = [None, None]
    #     type = "FLOAT"
    #     line = ""
    #
    #     # Moest 1 van de 2 maar een float zijn moeten we eerst nog de int omzetten naar een float
    #     if float:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #         if value.type == "INT":
    #             registers[0], lineValue = intToFloat(registers[0])
    #             line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #         if var.type == "INT":
    #             registers[1], lineVar = intToFloat(registers[1])
    #             line += lineVar
    #
    #         line += "%" + str(registerCount) + " = fadd float %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #
    #     else:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #
    #         line += "%" + str(registerCount) + " = add i32 %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #         type = "INT"
    #
    #     line += store(registerCount, register, type)
    #
    #     return line
    #
    # def subtract(self, value, var, register, float=False):
    #     """
    #     :param value: De waarde/andere variable die bij de var wordt opgeteld (node)
    #     :param var: De variable waar de value wordt opgeteld. (node)
    #     :param register: Het register nummer waar we de uitkomst in wegschrijven
    #     :param float: Geeft aan of een een sub of fsub is.
    #     :return: De register nummber en de line die wegschreven moeten worden in het bestand
    #     """
    #
    #     # 0 = value, 1 = var
    #     registers = [None, None]
    #     type = "FLOAT"
    #     line = ""
    #
    #     # Moest 1 van de 2 maar een float zijn moeten we eerst nog de int omzetten naar een float
    #     if float:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #         if value.type == "INT":
    #             registers[0], lineValue = intToFloat(registers[0])
    #             line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #         if var.type == "INT":
    #             registers[1], lineVar = intToFloat(registers[1])
    #             line += lineVar
    #
    #         line += "%" + str(registerCount) + " = fsub float %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #
    #     else:
    #         symbolValue = getSymbolFromTable(value)
    #         registers[0], lineValue = load(value.type, symbolValue.register)
    #         line += lineValue
    #
    #         symbolVar = getSymbolFromTable(var)
    #         registers[1], lineVar = load(var.type, symbolVar.register)
    #         line += lineVar
    #
    #         line += "%" + str(registerCount) + " = sub i32 %" + str(registers[0]) + ", %" + str(registers[1]) + "\n"
    #         type = "INT"
    #
    #     line += store(registerCount, register, type)
    #
    #     return line

    def function(self, node):
        table, name = getSymbolFromTable(node.parent.children[1].children[0])
        return_type = table.type
        parameters = table.functionParameters
        register = 1

        #TODO: de attribute moet hier nog in komen
        line = "define dso_local " + types[return_type][0] + " @" + name + "() {\n"

        #Alloceer een register voor deze return
        if return_type != "void":
            line += self.allocate(register, return_type)
            #store deze waarde ook
            #TODO: controleer dit nog later
            line += self.store(0, register, return_type)
            register += 1

        #TODO: parameters moeten nog worden toegevoegd maar momenteel doen we dit nog niet

        #Nu gaan we zien dat er assignments zijn
        for child in node.children:
            if child.token == "=":
                #TODO: hier verder werken voor de assignments
                pass

        # voegen de functies toe aan de lijst van functies, zodat we deze later kunnen printen
        # Zo kunne we ook de rest nog toevoegen van functions calls, additions etc...
        self.functions.append(funcNode(line, len(self.functions)-1, True, register))

    def returnFunction(self, node):

        # We nemen de laatst toegevoegde functie waar nog een return aan toegevoegd moet worden

        last = self.functions[len(self.functions)-1]


        returnval = node.children[len(node.children) - 1].children[0]
        if returnval.token == "IDENTIFIER":
            # TODO: zoek in de table naar zijn register
            pass
        else:
            last[0] += "ret " + types[returnval.token][0] + " " + str(returnval.value) + "\n"

        #Na de return mag de functie gesloten worden
        last[2] = "closed"

    def printf(node):
        pass

    def load(self, type, register):

        return registerCount, "%" + str(registerCount) + " = load " + types[type][0] + ", " + types[type][0] + "* " \
                                                                                                               "%" + str(register) + ", " + types[type][1] + "\n"
    def store(self,fromRegister, toRegister, type):
        return "store " + types[type][0] + " %" + str(fromRegister) + ", " + types[type][0] + "* %" + str(toRegister) + "" \
                                                                                                                        ", " + types[type][1] + "\n"

    def allocate(self, register, type):
        return "  %" + str(register) + " = alloca " + types[type][0] + ", " + types[type][1] + "\n"
def multiply():
    pass
def divide():


    pass


def intToFloat(register):
    """
    Krijgt een integer binnen en zet deze om naar een float
    :param register: De ingeladen register
    :return: node als een float
    """

    return registerCount, "%" + str(registerCount) + " = sitofp i32 %" + str(register) + " to float\n"

def getSymbolFromTable(node):

    searchNode = node

    symbolValue = None
    name = None
    if node.token == "IDENTIFIER":
        while symbolValue is None:

            while searchNode.symbolTablePointer is None:
                searchNode = searchNode.parent

            table = searchNode.symbolTablePointer.dict

            for key in table:
                if str(key) == str(node.value):
                    symbolValue = table[key]
                    name = str(key)
                    break

            if symbolValue is None:
                searchNode = searchNode.parent

    return symbolValue, name
