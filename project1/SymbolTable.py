class Value:
    def __init__(self, type=None, value=None, isConst=False,
                 isOverwritten=False, inputTypes=None, outputTypes=None,
                 functionParameters = None, pointer=None, reference=None,
                 line=None, column=None, arrayData=False):
        self.type = type
        self.value = value
        self.isConst = isConst # bool
        self.isOverwritten = isOverwritten # bool
        self.inputTypes = inputTypes # parameter type (e.g. for functions)
        self.outputTypes = outputTypes # return type (e.g. for functions)
        self.functionParameters = functionParameters
        self.register = int()
        self.stackOffset = int()
        self.isAssigned = False
        self.isGlobal = False
        self.isParam = False

        self.pointer = pointer
        self.reference = reference

        self.line = line
        self.column = column

        self.prevValues = list() # list of tuples (line, column, value) associated with the variable

        self.arrayData = arrayData # [dimensions] if True (array), False if not array

class SymbolTable:
    def __init__(self):
        self.dict = dict() #key: varname; value: type, constness,...
        self.enclosingSTable = None
        self.astNode = None
        self.childrenTables = []

    def addVar(self, key, value):
        self.dict[key] = value

    def getValue(self, key):
        return self.dict[key]


