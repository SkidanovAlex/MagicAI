# This file contains functions to build statement objects out of
#    parse trees.
#

class Object:
    def __init__(self, value):
        self.value = value

class AndList:
    def __init__(self, value):
        self.list = [value]
    def add_element(self, value):
        self.list.append(value)

class OrList:
    def __init__(self, value):
        self.list = [value]
    def add_element(self, value):
        self.list.append(value)

class AndOrList:
    def __init__(self, value):
        self.list = [value]
    def add_element(self, value):
        self.list.append(value)

class CommaSeparatedList:
    def __init__(self, value):
        self.list = [value]
    def add_element(self, value):
        self.list.append(value)

class Statement:
    pass

class MultiStatement:
    def __init__(self, statement):
        self.statements = [statement]
    def add_statement(self, statement):
        self.statements.append(statement)

class EmptyStatement(Statement):
    pass
