# If card says "A and B and C", the result will be
#   { 'type': TAnd, 'value': [elements] } 
# correspondingly, if it says "or", then it will be
#   { 'type': TOr, 'value': [elements] }
# and these could be nested
# if an element is not a list,
#   { 'type': TSignle, 'value': val }

EndOfStatement = 0

TAnd = 1
TOr = 2
TStatements = 3
TSingle = 4

OCreature = 1001
OCreatures = 1101
OArtifact = 1002
OEnchantment = 1003

EFlying = 2001
EFirstStrike = 2002
EHaste = 2003
ETrample = 2004
EVigilance = 2005
EExtort = 2006
ECipher = 2007
EEvolve = 2008
EDefender = 2009

TEndOfTurn = 3001

MAExile = 4001
MADestroy = 4002

OQYouControl = 4101

T_END_OF_STATEMENT = 0
T_AND_OR = 1
T_OBJECT = 2
T_OBJECTS = 3
T_ABILITY = 4
T_ABILITIES = 5
T_PLUS_X_PLUS_X = 6
T_GET_EFFECT = 7
T_GET_EFFECTS = 8
T_TARGET = 9
T_TIME = 10
T_MOVE_ACTION = 11
T_OBJECT_INTERNAL = 12
T_OBJECT_QUALIFIER = 13
T_STATEMENT = 400
T_STATEMENTS = 401
T_CARD = 499

class Object:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Rule:
    def __init__(self, emits, body, retFunc, retObj):
        assert retObj == None or retFunc == None
        self.emits = emits
        self.body = body
        self.retObj = retObj
        self.retFunc = retFunc
    def apply(self, children):
        if self.retObj != None:
            return self.retObj
        return self.retFunc(*children)

def IsTerminal(state):
    return isinstance(state, basestring) or state == T_PLUS_X_PLUS_X

def Ident(elem):
    return elem

def IdentSkip1(_, elem):
    return elem

def AndOr(elem, what, obj):
    if obj.type == what:
        return Object(what, [elem, obj.value])
    else:
        return Object(what, [elem, obj])

def MergeStatemets(elem, obj):
    if obj.type == TStatements:
        return Object(TStatements, [elem, obj.value])
    else:
        assert obj.type == TSingle
        return Object(TStatements, [elem, obj])

# TODO
def ObjectWithQualifiers(obj, qual):
    return None

def ConstructCard_TargetGetEffect(obj, effect, time, _):
    return None

def ConstructCard_MoveAction(action, obj, _):
    return None

def ConstructCard_CreatureAbility(ability, _):
    return None

def ConstructCard_Empty(_):
    return None

rules = {}
def AddRule(emits, body, retFunc, retObj = None):
    if emits not in rules:
        rules[emits] = []
    rules[emits].append(Rule(emits, body, retFunc, retObj))

AddRule(T_AND_OR, ["and"], None, TAnd)
AddRule(T_AND_OR, ["or"], None, TOr)

AddRule(T_OBJECT_INTERNAL, ["creature"], None, Object(TSingle, OCreature))
AddRule(T_OBJECT_INTERNAL, ["creatures"], None, Object(TSingle, OCreatures))
AddRule(T_OBJECT_INTERNAL, ["enchantment"], None, Object(TSingle, OEnchantment))
AddRule(T_OBJECT_INTERNAL, ["artifact"], None, Object(TSingle, OArtifact))

AddRule(T_OBJECT_QUALIFIER, ["you", "control"], None, OQYouControl)

AddRule(T_OBJECT, [T_OBJECT_INTERNAL], ObjectWithQualifiers)
AddRule(T_OBJECT, [T_OBJECT_INTERNAL, T_OBJECT_QUALIFIER], ObjectWithQualifiers)

AddRule(T_OBJECTS, [T_OBJECT], Ident)
AddRule(T_OBJECTS, [T_OBJECT, T_AND_OR, T_OBJECTS], AndOr)

AddRule(T_ABILITY, ["defender"], EDefender)
AddRule(T_ABILITY, ["flying"], EFlying)
AddRule(T_ABILITY, ["vigilance"], EVigilance)
AddRule(T_ABILITY, ["first", "strike"], EFirstStrike)
AddRule(T_ABILITY, ["haste"], EHaste)
AddRule(T_ABILITY, ["trample"], ETrample)
AddRule(T_ABILITY, ["extort"], EExtort)
AddRule(T_ABILITY, ["cipher"], ECipher)
AddRule(T_ABILITY, ["evolve"], EEvolve)

AddRule(T_ABILITIES, [T_ABILITY], Ident)
AddRule(T_ABILITIES, [T_ABILITY, T_AND_OR, T_ABILITIES], Ident)

AddRule(T_GET_EFFECT, ["gets", T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, ["get", T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, ["gains", T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, ["gain", T_ABILITIES], IdentSkip1)

AddRule(T_GET_EFFECTS, [T_GET_EFFECT], Ident)
AddRule(T_GET_EFFECTS, [T_GET_EFFECT, T_AND_OR, T_GET_EFFECTS], AndOr)

AddRule(T_TARGET, ["target", T_OBJECTS], IdentSkip1)
AddRule(T_TARGET, [T_OBJECTS], Ident)

# TODO
AddRule(T_TIME, ['until', 'end', 'of', 'turn'], None, Object(TSingle, TEndOfTurn))

AddRule(T_MOVE_ACTION, ["exile"], None, Object(TSingle, MAExile))
AddRule(T_MOVE_ACTION, ["destroy"], None, Object(TSingle, MADestroy))

AddRule(T_END_OF_STATEMENT, ["DOT"], None, Object(TSingle, EndOfStatement))

AddRule(T_STATEMENT, [T_TARGET, T_GET_EFFECTS, T_TIME, T_END_OF_STATEMENT], ConstructCard_TargetGetEffect)
AddRule(T_STATEMENT, [T_MOVE_ACTION, T_TARGET, T_END_OF_STATEMENT], ConstructCard_MoveAction)
AddRule(T_STATEMENT, [T_ABILITY, T_END_OF_STATEMENT], ConstructCard_CreatureAbility)
AddRule(T_STATEMENT, [T_END_OF_STATEMENT], ConstructCard_Empty)
AddRule(T_STATEMENTS, [T_STATEMENT], Ident)
AddRule(T_STATEMENTS, [T_STATEMENT, T_STATEMENTS], MergeStatemets)

AddRule(T_CARD, [T_STATEMENTS], Ident)

