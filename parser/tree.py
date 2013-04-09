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

class Statement:
    pass

class MultiStatement:
    def __init__(self, statement):
        self.statements = [statement]
    def add_statement(self, statement):
        self.statements.append(statement)

class EmptyStatement(Statement):
    pass

class TargetGetEffectStatement(Statement):
    def __init__(self, target, effect, time):
        self.target = target
        self.effect = effect
        self.time = time

class BattalionStatement(Statement):
    def __init__(self, stmt):
        self.child_stmt = stmt
        print "Battalion: %s %s %s" % (stmt.target, stmt.effect, stmt.time)

class MoveActionStatement(Statement):
    def __init__(self, target, action):
        self.target = target
        self.action = action

class CreatureAbilityStatement(Statement):
    def __init__(self, ability):
        self.ability = ability

def BuildStatement_TargetGetEffect(obj, effect, time, _):
    return TargetGetEffectStatement(obj, effect, time)

def BuildStatement_Battalion(_, stmt):
    return BattalionStatement(stmt)

def BuildStatement_MoveAction(action, obj, _):
    return MoveActionStatement(obj, action)

def BuildStatement_CreatureAbility(ability, _):
    return CreatureAbilityStatement(ability)

def BuildStatement_Empty(_):
    return EmptyStatement()


