# If card says "A and B and C", the result will be
#   { 'type': TAnd, 'value': [elements] } 
# correspondingly, if it says "or", then it will be
#   { 'type': TOr, 'value': [elements] }
# and these could be nested
# if an element is not a list,
#   { 'type': TSignle, 'value': val }

import tree
from tree import Object

EndOfStatement = 0

Dummy = -1

TAnd = 1
TOr = 2
TComma = 3
TSingle = 4

OThis = 1000
OCreature = 1001
OCreatures = 1101
OArtifact = 1002
OArtifacts = 1003
OEnchantment = 1004
OEnchantments = 1005
OLand = 1020
OGate = 1021

EFlying = 2001
EFirstStrike = 2002
EHaste = 2003
ETrample = 2004
EVigilance = 2005
EExtort = 2006
ECipher = 2007
EEvolve = 2008
EDefender = 2009
EReach = 2010
EDoubleStrike = 2011
EUnleash = 2012
EScavenge = 2013
ESwampwalk = 2014
ELifelink = 2015
EDeathtouch = 2016
EFlash = 2017

TEndOfTurn = 3001

MAExile = 4001
MADestroy = 4002
MARegenerate = 4002
MATap = 4002
MAUntap = 4002

OQYouControl = 4101
OQOpponentsControl = 4102

ETBTapped = 4201

T_END_OF_STATEMENT = 0
T_AND_OR = 1
T_OBJECT = 2
T_OBJECTS = 3
T_ABILITY = 4
T_ABILITIES = 5
T_PLUS_X_PLUS_X = 6
T_GET_EFFECT = 7
T_GET_EFFECTS = 8
T_PIC_COST = 9 # mana or tap or anything as a picture
T_TIME = 10
T_MOVE_ACTION = 11
T_OBJECT_INTERNAL = 12
T_OBJECT_QUALIFIER = 13
T_ENTER_THE_BATTLEFIELD_MOD = 14
T_ACTION = 15
T_COST = 16
T_PROTECTION = 17

T_BATTALION = 50


T_STATEMENT = 400
T_STATEMENTS = 401
T_CARD = 499

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
    return isinstance(state, basestring) or state == T_PLUS_X_PLUS_X or state == T_PIC_COST

def Ident(elem):
    return elem

def IdentSkip1(_, elem):
    return elem

def IdentSkip2(_1, _2, elem):
    return elem

def AndOr(elem, what, obj):
    lst = None
    if what == TAnd and not isinstance(obj, tree.AndList):
        lst = tree.AndList(obj)
    elif what == TOr and not isinstance(obj, tree.OrList):
        lst = tree.OrList(obj)
    elif what == TComma and not isinstance(obj, tree.CommaSeparatedList):
        lst = tree.CommaSeparatedList(obj)
    lst.add_element(elem)

def MergeStatemets(elem, obj):
    if isinstance(obj, tree.MultiStatement):
        obj.add_statement(elem)
        return obj
    else:
        multistatement = tree.MultiStatement(obj)
        multistatement.add_statement(elem)
        return multistatement

# TODO
def ObjectWithQualifiers(obj, qual):
    return None

rules = {}
def AddRule(emits, body, retFunc, retObj = None):
    if emits not in rules:
        rules[emits] = []
    rules[emits].append(Rule(emits, body, retFunc, retObj))

AddRule(T_AND_OR, ["and"], None, TAnd)
AddRule(T_AND_OR, ["or"], None, TOr)
AddRule(T_AND_OR, ["COMMA"], None, TComma)

AddRule(T_OBJECT_INTERNAL, ["creature"], None, Object(OCreature))
AddRule(T_OBJECT_INTERNAL, ["creatures"], None, Object(OCreatures))
AddRule(T_OBJECT_INTERNAL, ["enchantment"], None, Object(OEnchantment))
AddRule(T_OBJECT_INTERNAL, ["enchantments"], None, Object(OEnchantments))
AddRule(T_OBJECT_INTERNAL, ["artifact"], None, Object(OArtifact))
AddRule(T_OBJECT_INTERNAL, ["artifacts"], None, Object(OArtifacts))
AddRule(T_OBJECT_INTERNAL, ["land"], None, Object(OLand))
AddRule(T_OBJECT_INTERNAL, ["gate"], None, Object(OGate))
AddRule(T_OBJECT_INTERNAL, ["THIS"], None, Object(OThis))

AddRule(T_OBJECT_QUALIFIER, ["you", "control"], None, OQYouControl)
AddRule(T_OBJECT_QUALIFIER, ["your", "opponents", "control"], None, OQOpponentsControl)
AddRule(T_OBJECT_QUALIFIER, ["an", "opponent", "controls"], None, OQOpponentsControl)

AddRule(T_OBJECT, [T_OBJECT_INTERNAL], Ident)
AddRule(T_OBJECT, [T_OBJECT_INTERNAL, T_OBJECT_QUALIFIER], ObjectWithQualifiers)

AddRule(T_OBJECTS, [T_OBJECT], Ident)
AddRule(T_OBJECTS, ["target", T_OBJECTS], IdentSkip1)
AddRule(T_OBJECTS, [T_OBJECT, T_AND_OR, T_OBJECTS], AndOr)

AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ["enter", 'the', 'battlefield', 'tapped'], None, ETBTapped)

AddRule(T_ABILITY, ["defender"], None, Object(EDefender))
AddRule(T_ABILITY, ["flying"], None, Object(EFlying))
AddRule(T_ABILITY, ["vigilance"], None, Object(EVigilance))
AddRule(T_ABILITY, ["first", "strike"], None, Object(EFirstStrike))
AddRule(T_ABILITY, ["haste"], None, Object(EHaste))
AddRule(T_ABILITY, ["trample"], None, Object(ETrample))
AddRule(T_ABILITY, ["extort"], None, Object(EExtort))
AddRule(T_ABILITY, ["cipher"], None, Object(ECipher))
AddRule(T_ABILITY, ["evolve"], None, Object(EEvolve))
AddRule(T_ABILITY, ["reach"], None, Object(EReach))
AddRule(T_ABILITY, ["double", "strike"], None, Object(EDoubleStrike))
AddRule(T_ABILITY, ["unleash"], None, Object(EUnleash))
AddRule(T_ABILITY, ["scavenge", T_COST], None, Object(EScavenge)) # TODO
AddRule(T_ABILITY, ["swampwalk"], None, Object(ESwampwalk))
AddRule(T_ABILITY, ["lifelink"], None, Object(ELifelink))
AddRule(T_ABILITY, ["deathtouch"], None, Object(EDeathtouch))
AddRule(T_ABILITY, ["flash"], None, Object(EFlash))

AddRule(T_ABILITIES, [T_ABILITY], Ident)
AddRule(T_ABILITIES, [T_ABILITY, T_AND_OR, T_ABILITIES], AndOr)

# TODO
AddRule(T_PROTECTION, ["protection", "from", T_OBJECTS], IdentSkip2)

AddRule(T_GET_EFFECT, ["gets", T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, ["get", T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, ["gains", T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, ["gain", T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, ["has", T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, ["has", T_PROTECTION], IdentSkip1)

AddRule(T_GET_EFFECTS, [T_GET_EFFECT], Ident)
AddRule(T_GET_EFFECTS, [T_GET_EFFECT, T_AND_OR, T_GET_EFFECTS], AndOr)

# TODO
AddRule(T_TIME, ['until', 'end', 'of', 'turn'], None, Object(TEndOfTurn))

AddRule(T_MOVE_ACTION, ["exile"], None, Object(MAExile))
AddRule(T_MOVE_ACTION, ["destroy"], None, Object(MADestroy))
AddRule(T_MOVE_ACTION, ["regenerate"], None, Object(MARegenerate))
AddRule(T_MOVE_ACTION, ["tap"], None, Object(MATap))
AddRule(T_MOVE_ACTION, ["untap"], None, Object(MAUntap))

AddRule(T_BATTALION, ['battalion', 'DASH', 'whenever', 'THIS', 'and', 'at', 'least', 'two', 'other', 'creatures', 'attack', 'COMMA'], None, Object(Dummy))

AddRule(T_COST, [T_PIC_COST], Ident)
AddRule(T_COST, [T_PIC_COST, T_COST], None, Object(0)) # TODO

AddRule(T_END_OF_STATEMENT, ["DOT"], None, Object(EndOfStatement))

AddRule(T_ACTION, [T_OBJECTS, T_GET_EFFECTS, T_TIME, T_END_OF_STATEMENT], tree.BuildAction_TargetGetEffect)
AddRule(T_ACTION, [T_MOVE_ACTION, T_OBJECTS, T_END_OF_STATEMENT], tree.BuildAction_Move)

AddRule(T_STATEMENT, [T_ACTION], tree.BuildStatement_Action)
AddRule(T_STATEMENT, [T_COST, "COLON", T_ACTION], tree.BuildStatement_PaidAction)
AddRule(T_STATEMENT, [T_BATTALION, T_ACTION], tree.BuildStatement_Battalion)
AddRule(T_STATEMENT, [T_ABILITIES, T_END_OF_STATEMENT], tree.BuildStatement_CreatureAbility)
AddRule(T_STATEMENT, ["enchant", T_OBJECT], tree.BuildStatement_EnchantWhat)
AddRule(T_STATEMENT, [T_OBJECTS, T_ENTER_THE_BATTLEFIELD_MOD, T_END_OF_STATEMENT], tree.BuildStatement_EnterTheBattleFieldMod)
AddRule(T_STATEMENT, ["enchanted", T_OBJECT, "has", "DQ", T_STATEMENT, "DQ", T_END_OF_STATEMENT], tree.BuildStatement_EnchantedObjectHasX)
AddRule(T_STATEMENT, ["enchanted", T_OBJECT, T_GET_EFFECTS], tree.BuildStatement_EnchantedObjectGetsEffect)
AddRule(T_STATEMENT, [T_END_OF_STATEMENT], tree.BuildStatement_Empty)
AddRule(T_STATEMENTS, [T_STATEMENT], Ident)
AddRule(T_STATEMENTS, [T_STATEMENT, T_STATEMENTS], MergeStatemets)

AddRule(T_CARD, [T_STATEMENTS], Ident)

