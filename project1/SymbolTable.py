class Value:
    def __init__(self, type=None, value=None, isConst=False,
                 isOverwritten=False, inputTypes=None, outputTypes=None,
                 functionParameters = None, pointer = None, reference = None):
        self.type = type
        self.value = value
        self.isConst = isConst # bool
        self.isOverwritten = isOverwritten # bool
        self.inputTypes = inputTypes # parameter type (e.g. for functions)
        self.outputTypes = outputTypes # return type (e.g. for functions)
        self.functionParameters = functionParameters
        self.register = []

        self.pointer = pointer
        self.reference = reference


class SymbolTable:
    def __init__(self):
        self.dict = dict() #key: varname; value: type, constness,...
        self.enclosingSTable = None
        self.astNode = None

    def addVar(self, key, value):
        self.dict[key] = value

    def getValue(self, key):
        return self.dict[key]


