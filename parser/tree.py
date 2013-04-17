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

class CommaSeparatedList:
    def __init__(self, value):
        self.list = [value]
    def add_element(self, value):
        self.list.append(value)

class Action:
    pass

class TargetGetEffectAction(Action):
    def __init__(self, target, effect, time):
        self.target = target
        self.effect = effect
        self.time = time

class MoveAction(Action):
    def __init__(self, target, action, part_of_field = None):
        self.target = target
        self.action = action
        self.part_of_field = part_of_field

class PutTokenAction(Action):
    def __init__(self, stats, colors, creature_type, obj, num):
        self.stats = stats
        self.colors = colors
        self.creature_type = creature_type
        self.obj = obj
        self.num = num

class Statement:
    pass

class MultiStatement:
    def __init__(self, statement):
        self.statements = [statement]
    def add_statement(self, statement):
        self.statements.append(statement)

class EmptyStatement(Statement):
    pass

class ActionStatement(Statement):
    def __init__(self, act):
        self.action = act

class PaidActionStatement(Statement):
    def __init__(self, cost, act):
        self.cost = cost
        self.action = act

class BattalionStatement(Statement):
    def __init__(self, act):
        self.action = act

class EnterTheBattleFieldModStatement(Statement):
    def __init__(self, target, mod):
        self.target = target
        self.mod = mod

class EnchantedObjectHasXStatement(Statement):
    def __init__(self, stmt):
        self.stmt = stmt

class EnchantedObjectGetsEffectStatement(Statement):
    def __init__(self, effect):
        self.effect = effect

class CreatureAbilityStatement(Statement):
    def __init__(self, ability):
        self.ability = ability

class EnchantWhatStatement(Statement):
    def __init__(self, obj):
        self.object = object

def BuildAction_TargetGetEffect(obj, effect, time, _):
    return TargetGetEffectAction(obj, effect, time)

def BuildAction_Move(action, obj, _):
    return MoveAction(obj, action)

def BuildAction_MoveFrom(action, obj, _1 , part_of_field,_2):
    return MoveAction(obj, action, part_of_field)

def BuildAction_PutToken(_1, num, stats, colors, ctype, obj, _4):
    return PutTokenAction(stats, colors, ctype, obj, num)

def BuildStatement_Action(act):
    return ActionStatement(act)

def BuildStatement_PaidAction(cost, _, act):
    return PaidActionStatement(cost, act)

def BuildStatement_Battalion(_, act):
    return BattalionStatement(act)

def BuildStatement_EnterTheBattleFieldMod(obj, mod, _):
    return EnterTheBattleFieldModStatement(obj, mod)

def BuildStatement_EnchantedObjectHasX(_1, _2, _3, _4, stmt, _5, _6):
    return EnchantedObjectHasXStatement(stmt)

def BuildStatement_EnchantedObjectGetsEffect(_1, _2, effect):
    return EnchantedObjectGetsEffectStatement(effect)

def BuildStatement_CreatureAbility(ability, _):
    return CreatureAbilityStatement(ability)

def BuildStatement_EnchantWhat(_, obj):
    return EnchantWhatStatement(obj)

def BuildStatement_Empty(_):
    return EmptyStatement()


#TODO
def BuildAction_DealDamage(dealer, _1, num, _2, _3, target):
    return None
