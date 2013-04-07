# If card says "A and B and C", the result will be
#   { 'type': TAnd, 'value': [elements] } 
# correspondingly, if it says "or", then it will be
#   { 'type': TOr, 'value': [elements] }
# and these could be nested
# if an element is not a list,
#   { 'type': TSignle, 'value': val }

# UNDONE: +X/+X

EndOfStatement = 0

TAnd = 1
TOr = 2
TSingle = 3

OCreature = 1001
OArtifact = 1002
OEnchantment = 1003

EFlying = 2001
EFirstStrike = 2002
EHaste = 2003
ETrample = 2004

TEndOfTurn = 3001

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

# TODO
def ConstructCard_TargetGetEffect(obj, effect, time):
    return None

rules = {}
def AddRule(emits, body, retFunc, retObj = None):
    if emits not in rules:
        rules[emits] = []
    rules[emits].append(Rule(emits, body, retFunc, retObj))

AddRule(T_AND_OR, ["and"], None, TAnd)
AddRule(T_AND_OR, ["or"], None, TOr)

AddRule(T_OBJECT, ["creature"], None, Object(TSingle, OCreature))
AddRule(T_OBJECT, ["enchantment"], None, Object(TSingle, OEnchantment))
AddRule(T_OBJECT, ["artifact"], None, Object(TSingle, OArtifact))

AddRule(T_OBJECTS, [T_OBJECT], Ident)
AddRule(T_OBJECTS, [T_OBJECT, T_AND_OR, T_OBJECTS], AndOr)

AddRule(T_ABILITY, ["flying"], EFlying)
AddRule(T_ABILITY, ["first", "strike"], EFirstStrike)
AddRule(T_ABILITY, ["haste"], EHaste)
AddRule(T_ABILITY, ["trample"], ETrample)

AddRule(T_ABILITIES, [T_ABILITY], Ident)
AddRule(T_ABILITIES, [T_ABILITY, T_AND_OR, T_ABILITIES], Ident)

AddRule(T_GET_EFFECT, ["gets", T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, ["gains", T_ABILITIES], IdentSkip1)

AddRule(T_GET_EFFECTS, [T_GET_EFFECT], Ident)
AddRule(T_GET_EFFECTS, [T_GET_EFFECT, T_AND_OR, T_GET_EFFECTS], AndOr)

AddRule(T_TARGET, ["target", T_OBJECTS], IdentSkip1)

# TODO
AddRule(T_TIME, ['until', 'end', 'of', 'turn'], None, Object(TSingle, TEndOfTurn))

AddRule(T_END_OF_STATEMENT, ["DOT"], None, Object(TSingle, EndOfStatement))

AddRule(T_CARD, [T_TARGET, T_GET_EFFECTS, T_TIME, T_END_OF_STATEMENT], ConstructCard_TargetGetEffect)
