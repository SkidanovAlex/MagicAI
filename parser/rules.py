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
OCard = 1022
OPermanent = 1023
OPlayer = 1024
OOpponent = 1025
OYou = 1026
OIt = 1027

EChosenAbility = 2000
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
EIntimidate = 2018
EHexproof = 2019

TEndOfTurn = 3001
TBeginningOfEachCombat = 3002

ClrRed = 3101
ClrBlue = 3102
ClrGreen = 3103
ClrWhite = 3104
ClrBlack = 3105
ClrMultiColored = 3106

MAExile = 4001
MADestroy = 4002
MARegenerate = 4003
MATap = 4004
MAUntap = 4005
MAReturn = 4006
MADetain = 4007
MASacrifice = 4008

OQYouControl = 4101
OQOpponentsControl = 4102
OQAttacking = 4103
OQBlocking = 4104
OQAnother = 4105
OQTarget = 4106
OQEach = 4107
OQUntapped = 4108
OQAny = 4109
OQEquipped = 4110
OQAll = 4111
OQEvery = 4112
OQDealtDamage = 4113
OQThat = 4114
OQEnchanted = 4115
OQYouDontControl = 4116
OQBlocked = 4117

ETBTapped = 4201

PoFBattlefield = 4300
PoFGraveyard = 4301
PoFLibrary = 4302
PoFHand = 4303

WhoseAnyones = 4400
WhoseYour = 4401
WhoseHis = 4402
WhoseOwners = 4403
WhoseControllers = 4404

ODsAttacks = 4501
ODsDealsDamage = 4502
ODsDies = 4503


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
T_UNTIL = 10
T_MOVE_ACTION = 11
T_OBJECT_INTERNAL = 12
T_WHOSE = 13
T_ENTER_THE_BATTLEFIELD_MOD = 14
T_ACTION = 15
T_COST = 16
T_COST_PART = 17
T_COLOR = 18
T_COLORS = 19
T_CREATURE_TYPE = 20
T_ONTO_THE_BF = 21
T_NUMBER = 22
T_OBJECT_TYPE = 23
T_PART_OF_FIELD_INTERNAL = 24
T_PART_OF_FIELD = 25
T_OBJECT_QUALIFIER_AFTER = 26
T_OBJECT_QUALIFIER_BEFORE = 27
T_OBJECT_QUALIFIERS_AFTER = 28
T_OBJECT_QUALIFIERS_BEFORE = 29
T_PROTECTION = 30
T_CONDITION = 31
T_ENTERS_THE_BF_PREFIX = 32
T_ENTERS_THE_BF = 33
T_PUT_COUNTER = 34
T_MOVE_ACTION_TYPE = 35
T_OBJECT_DOES = 36
T_FOR_EACH = 37
T_CARD_TYPE = 38
T_ACTIONS = 39
T_WHERE_X_INTERNAL = 40
T_WHERE_X = 41
T_ACTION_INTERNAL = 42
T_ACTION_QUALIFIER_AFTER = 43
T_MOVE_TO = 44
T_COUNTERS = 45
T_COUNTERS_ON = 46
T_REMOVE_COUNTER = 47

W_GETS = 1001
W_HAVE = 1002
W_CARD = 1003
W_IS = 1004
W_DRAW = 1005
W_DISCARD = 1006

T_BATTALION = 50
T_BLOODRUSH = 51


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

def IdentSkip2nd(elem, _):
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

def MergeStatements(elem, obj):
    if isinstance(obj, tree.MultiStatement):
        obj.add_statement(elem)
        return obj
    else:
        multistatement = tree.MultiStatement(obj)
        multistatement.add_statement(elem)
        return multistatement

def MergeStatementsSkip1(elem, _, obj):
    MergeStatements(elem, obj)

def MergeStatementsSkip2(elem, _1, _2, obj):
    MergeStatements(elem, obj)

rules = {}
def AddRule(emits, body, retFunc, retObj = None):
    if emits not in rules:
        rules[emits] = []
    rules[emits].append(Rule(emits, body, retFunc, retObj))

AddRule(T_AND_OR, ["and"], None, TAnd)
AddRule(T_AND_OR, ["or"], None, TOr)
AddRule(T_AND_OR, ["COMMA"], None, TComma)

AddRule(T_NUMBER, ["a"], None, 1)
AddRule(T_NUMBER, ["an"], None, 1)
AddRule(T_NUMBER, ["one"], None, 1)
AddRule(T_NUMBER, ["two"], None, 2)
AddRule(T_NUMBER, ["three"], None, 3)
AddRule(T_NUMBER, ["four"], None, 4)
AddRule(T_NUMBER, ["five"], None, 5)
AddRule(T_NUMBER, ["six"], None, 6)
for i in range(20):
    AddRule(T_NUMBER, [str(i)], None, i)
AddRule(T_NUMBER, ["up", "to", T_NUMBER], None, Object(0)) # TODO
AddRule(T_NUMBER, ["x"], None, 'x')
AddRule(T_NUMBER, ["any", "number", "of"], None, Object(0)) # TODO

AddRule(T_CARD_TYPE, ["creature"], Ident)
AddRule(T_CARD_TYPE, ["creatures"], Ident)
AddRule(T_CARD_TYPE, ["instant"], Ident)
AddRule(T_CARD_TYPE, ["sorcery"], Ident)
AddRule(T_CARD_TYPE, ["artifact"], Ident)
AddRule(T_CARD_TYPE, ["artifacts"], Ident)
AddRule(T_CARD_TYPE, ["land"], Ident)
AddRule(T_CARD_TYPE, ["nonland"], Ident)
AddRule(T_CARD_TYPE, ["noncreature"], Ident)

AddRule(T_OBJECT_TYPE, ["enchantment"], None, Object(OEnchantment))
AddRule(T_OBJECT_TYPE, ["enchantments"], None, Object(OEnchantments))
AddRule(T_OBJECT_TYPE, ["gate"], None, Object(OGate))
AddRule(T_OBJECT_TYPE, ["card"], None, Object(OCard))
AddRule(T_OBJECT_TYPE, ["player"], None, Object(OPlayer))
AddRule(T_OBJECT_TYPE, ["you"], None, Object(OYou))
AddRule(T_OBJECT_TYPE, ["opponent"], None, Object(OOpponent))

AddRule(T_OBJECT_TYPE, ["permanent"], None, Object(OPermanent))
AddRule(T_OBJECT_TYPE, ["spell"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE], Ident) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "spell"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "permanent"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "card"], IdentSkip2nd)
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "spells"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "permanents"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "cards"], IdentSkip2nd)

AddRule(T_OBJECT_INTERNAL, ["it"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, [T_OBJECT_TYPE], Ident)
AddRule(T_OBJECT_INTERNAL, ["THIS"], None, Object(OThis))
# TODO
AddRule(T_OBJECT_INTERNAL, [T_OBJECT_TYPE, "token"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_OBJECT_TYPE, "tokens"], None, Object(0))

AddRule(T_OBJECT_QUALIFIER_AFTER, ["you", "control"], None, OQYouControl)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["you", "don't", "control"], None, OQYouDontControl)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["your", "opponents", "control"], None, OQOpponentsControl)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["an", "opponent", "controls"], None, OQOpponentsControl)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "dealt", "damage", "this", "turn"], None, OQDealtDamage)
#TODO
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_ABILITIES], None, IdentSkip1)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_COUNTERS_ON], None, IdentSkip1)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_COUNTERS], None, IdentSkip1)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "the", "same", "controller"], None, IdentSkip1)

AddRule(T_OBJECT_QUALIFIER_BEFORE, ["another"], None, Object(OQAnother))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["attacking"], None, Object(OQAttacking))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["blocking"], None, Object(OQBlocking))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["blocked"], None, Object(OQBlocked))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["untapped"], None, Object(OQUntapped))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["each"], None, Object(OQEach))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["any"], None, Object(OQAny))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["all"], None, Object(OQAll))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["every"], None, Object(OQEvery))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["equipped"], None, Object(OQEquipped))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["target"], None, Object(OQTarget))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["that"], None, Object(OQThat))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["enchanted"], None, Object(OQEnchanted))
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_NUMBER], Ident)
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_COLORS], Ident)

AddRule(T_OBJECT_QUALIFIERS_AFTER, [T_OBJECT_QUALIFIER_AFTER], Ident)
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE], Ident)

#TODO
AddRule(T_OBJECT_QUALIFIERS_AFTER, [T_OBJECT_QUALIFIER_AFTER, T_OBJECT_QUALIFIERS_AFTER], None, Object(0))
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE, T_OBJECT_QUALIFIERS_BEFORE], None, Object(0))
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE, T_AND_OR, T_OBJECT_QUALIFIERS_BEFORE], AndOr)

AddRule(T_OBJECT, [T_OBJECT_INTERNAL], Ident)
AddRule(T_OBJECT, [T_OBJECT_INTERNAL, T_OBJECT_QUALIFIERS_AFTER], None, Object(0)) # TODO
AddRule(T_OBJECT, [T_OBJECT_QUALIFIERS_BEFORE, T_OBJECT_INTERNAL, T_OBJECT_QUALIFIERS_AFTER], None, Object(0)) # TODO
AddRule(T_OBJECT, [T_OBJECT_QUALIFIERS_BEFORE, T_OBJECT_INTERNAL], None, Object(0)) # TODO

AddRule(T_OBJECTS, [T_OBJECT], Ident)
AddRule(T_OBJECTS, [T_OBJECT, T_AND_OR, T_OBJECTS], AndOr)

AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ["enter", 'the', 'battlefield', 'tapped'], None, ETBTapped)

AddRule(T_PART_OF_FIELD_INTERNAL, ["battlefield"], None, PoFBattlefield)
AddRule(T_PART_OF_FIELD_INTERNAL, ["graveyard"], None, PoFGraveyard)
AddRule(T_PART_OF_FIELD_INTERNAL, ["graveyards"], None, PoFGraveyard)
AddRule(T_PART_OF_FIELD_INTERNAL, ["library"], None, PoFLibrary)
AddRule(T_PART_OF_FIELD_INTERNAL, ["libraries"], None, PoFLibrary)
AddRule(T_PART_OF_FIELD_INTERNAL, ["hand"], None, PoFHand)
AddRule(T_PART_OF_FIELD_INTERNAL, ["hands"], None, PoFHand)

# TODO
AddRule(T_PART_OF_FIELD, [T_WHOSE, T_PART_OF_FIELD_INTERNAL], None, Object(0))

AddRule(T_WHOSE, ["a"], None, WhoseAnyones)
AddRule(T_WHOSE, ["your"], None, WhoseYour)
AddRule(T_WHOSE, ["its", "owner's"], None, WhoseOwners)
AddRule(T_WHOSE, ["its", "controller's"], None, WhoseControllers)
AddRule(T_WHOSE, ["their", "owners'"], None, WhoseOwners)
AddRule(T_WHOSE, ["your", "opponents'"], None, WhoseOwners)

AddRule(T_ABILITY, ["that", "ability"], None, Object(EChosenAbility))
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
AddRule(T_ABILITY, ["intimidate"], None, Object(EIntimidate))
AddRule(T_ABILITY, ["hexproof"], None, Object(EHexproof))

AddRule(T_ABILITIES, [T_ABILITY], Ident)
AddRule(T_ABILITIES, [T_ABILITY, T_AND_OR, T_ABILITIES], AndOr)

AddRule(T_CREATURE_TYPE, ["horror"], Ident)
AddRule(T_CREATURE_TYPE, ["knight"], Ident)
AddRule(T_CREATURE_TYPE, ["soldier"], Ident)
AddRule(T_CREATURE_TYPE, ["angel"], Ident)
AddRule(T_CREATURE_TYPE, ["rat"], Ident)
AddRule(T_CREATURE_TYPE, ["ooze"], Ident)
AddRule(T_CREATURE_TYPE, ["centaur"], Ident)
AddRule(T_CREATURE_TYPE, ["spirit"], Ident)
AddRule(T_CREATURE_TYPE, ["bird"], Ident)
 

AddRule(T_COLOR, ["red"], None, Object(ClrRed))
AddRule(T_COLOR, ["blue"], None, Object(ClrBlue))
AddRule(T_COLOR, ["green"], None, Object(ClrGreen))
AddRule(T_COLOR, ["white"], None, Object(ClrWhite))
AddRule(T_COLOR, ["black"], None, Object(ClrBlack))
AddRule(T_COLOR, ["multicolored"], None, Object(ClrMultiColored))

AddRule(T_COLORS, [T_COLOR], Ident)
AddRule(T_COLORS, [T_COLOR, T_AND_OR, T_COLORS], AndOr)

# TODO
AddRule(T_PROTECTION, ["protection", "from", T_OBJECTS], IdentSkip2)
AddRule(T_PROTECTION, ["protection", "from", T_COLORS], IdentSkip2)

AddRule(W_GETS, ["get"], None, Object(0))
AddRule(W_GETS, ["gets"], None, Object(0))
AddRule(W_GETS, ["gain"], None, Object(0))
AddRule(W_GETS, ["gains"], None, Object(0))

AddRule(W_HAVE, ["have"], None, Object(0))
AddRule(W_HAVE, ["has"], None, Object(0))

AddRule(W_CARD, ["card"], None, Object(0))
AddRule(W_CARD, ["cards"], None, Object(0))

AddRule(W_IS, ["is"], None, Object(0))
AddRule(W_IS, ["are"], None, Object(0))

AddRule(W_DRAW, ["draw"], None, Object(0))
AddRule(W_DRAW, ["draws"], None, Object(0))

AddRule(W_DISCARD, ["discard"], None, Object(0))
AddRule(W_DISCARD, ["discards"], None, Object(0))

AddRule(T_FOR_EACH, ["for", "each", T_OBJECTS], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", T_OBJECTS, "in", T_PART_OF_FIELD], None, Object(0))

AddRule(T_GET_EFFECT, [W_GETS, T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT, [W_GETS, T_PLUS_X_PLUS_X, T_FOR_EACH], None, Object(0)) # TODO
AddRule(T_GET_EFFECT, [W_GETS, T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, [W_HAVE, T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT, [W_HAVE, T_PROTECTION], IdentSkip1)
AddRule(T_GET_EFFECT, [W_IS, "indestructible"], IdentSkip1)
AddRule(T_GET_EFFECT, [W_IS, "unblockable"], IdentSkip1)

AddRule(T_GET_EFFECTS, [T_GET_EFFECT], Ident)
AddRule(T_GET_EFFECTS, [T_GET_EFFECT, T_AND_OR, T_GET_EFFECTS], AndOr)

AddRule(T_COUNTERS, [T_NUMBER, T_PLUS_X_PLUS_X, "counter"], None, Object(0)) # TODO
AddRule(T_COUNTERS, [T_NUMBER, T_PLUS_X_PLUS_X, "counters"], None, Object(0)) # TODO
AddRule(T_COUNTERS, [T_NUMBER, "counter"], None, Object(0)) # TODO
AddRule(T_COUNTERS, [T_NUMBER, "counters"], None, Object(0)) # TODO

AddRule(T_COUNTERS_ON, [T_COUNTERS, "on", T_OBJECTS], None, Object(0)) # TODO

AddRule(T_PUT_COUNTER, ["put", T_COUNTERS_ON], None, Object(0)) # TODO
AddRule(T_PUT_COUNTER, ["put", T_COUNTERS_ON, T_FOR_EACH], None, Object(0)) # TODO

AddRule(T_REMOVE_COUNTER, ["remove", T_COUNTERS, "from", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_REMOVE_COUNTER, ["remove", T_COUNTERS, "from", T_OBJECTS, T_FOR_EACH], None, Object(0)) # TODO

AddRule(T_UNTIL, ['until', 'end', 'of', 'turn'], None, Object(TEndOfTurn))
AddRule(T_UNTIL, ['this', 'turn'], None, Object(TEndOfTurn))

AddRule(T_MOVE_ACTION_TYPE, ["exile"], None, Object(MAExile))
AddRule(T_MOVE_ACTION_TYPE, ["destroy"], None, Object(MADestroy))
AddRule(T_MOVE_ACTION_TYPE, ["regenerate"], None, Object(MARegenerate))
AddRule(T_MOVE_ACTION_TYPE, ["tap"], None, Object(MATap))
AddRule(T_MOVE_ACTION_TYPE, ["untap"], None, Object(MAUntap))
AddRule(T_MOVE_ACTION_TYPE, ["return"], None, Object(MAReturn))
AddRule(T_MOVE_ACTION_TYPE, ["detain"], None, Object(MADetain))
AddRule(T_MOVE_ACTION_TYPE, ["sacrifice"], None, Object(MASacrifice))
AddRule(T_MOVE_ACTION_TYPE, ["put"], None, Object(MASacrifice))

AddRule(T_BATTALION, ['battalion', 'DASH', 'whenever', 'THIS', 'and', 'at', 'least', 'two', 'other', 'creatures', 'attack', 'COMMA'], None, Object(Dummy))
AddRule(T_BLOODRUSH, ['bloodrush', 'DASH'], None, Object(Dummy))

AddRule(T_COST_PART, [T_PIC_COST], Ident)
AddRule(T_COST_PART, [T_MOVE_ACTION], Ident)
AddRule(T_COST_PART, ["discard", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_COST_PART, ["pay", T_NUMBER, "life"], None, Object(0)) # TODO
AddRule(T_COST, [T_COST_PART], Ident)
AddRule(T_COST, [T_COST_PART, T_COST], None, Object(0)) # TODO
AddRule(T_COST, [T_COST_PART, "COMMA", T_COST], None, Object(0)) # TODO

AddRule(T_ONTO_THE_BF, ["onto", "the", "battlefield"], None, Object(0)) # TODO

AddRule(T_ENTERS_THE_BF_PREFIX, ["enters", "the", "battlefield"], None, Object(0)) # TODO
AddRule(T_ENTERS_THE_BF, [T_ENTERS_THE_BF_PREFIX], None, Object(0)) # TODO
AddRule(T_ENTERS_THE_BF, [T_ENTERS_THE_BF_PREFIX, "under", "your", "control"], None, Object(0)) # TODO

AddRule(T_OBJECT_DOES, [T_ENTERS_THE_BF], Ident)
AddRule(T_OBJECT_DOES, ['attacks'], None, Object(ODsAttacks))
AddRule(T_OBJECT_DOES, ['dies'], None, Object(ODsAttacks))
AddRule(T_OBJECT_DOES, ['deals', 'combat', 'damage'], None, Object(ODsDealsDamage))
AddRule(T_OBJECT_DOES, ['deals', 'combat', 'damage', "to", T_OBJECTS], None, Object(0)) # TODO

AddRule(T_WHERE_X_INTERNAL, ["that", "spell's", "converted", "mana", "cost"], None, Object(0)) # TODO
AddRule(T_WHERE_X_INTERNAL, ["its", "power"], None, Object(0)) # TODO
AddRule(T_WHERE_X_INTERNAL, ["the", "number", "of", T_OBJECTS, "in", T_PART_OF_FIELD], None, Object(0)) # TODO
AddRule(T_WHERE_X, ["where", "x", "is", T_WHERE_X_INTERNAL], None, Object(0)) # TODO

AddRule(T_END_OF_STATEMENT, ["DOT"], None, Object(EndOfStatement))

AddRule(T_MOVE_TO, ["to", T_PART_OF_FIELD], None, Object(0))
AddRule(T_MOVE_TO, ["on", "top", "of", T_WHOSE, "library"], None, Object(0))

AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPE, T_OBJECTS], tree.BuildAction_Move)
AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPE, T_OBJECTS, "from", T_PART_OF_FIELD], tree.BuildAction_MoveFrom)
AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPE, T_OBJECTS, T_MOVE_TO], None, Object(0)) # TODO
AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPE, T_OBJECTS, "from", T_PART_OF_FIELD, T_MOVE_TO], None, Object(0)) # TODO

AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_GET_EFFECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_UNTIL, "COMMA", T_OBJECTS, T_GET_EFFECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_GET_EFFECTS, T_UNTIL], tree.BuildAction_TargetGetEffect) # TODO
AddRule(T_ACTION_INTERNAL, [T_PUT_COUNTER], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_REMOVE_COUNTER], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["put", T_NUMBER, T_PLUS_X_PLUS_X, T_COLORS, T_CREATURE_TYPE, T_OBJECT, T_ONTO_THE_BF], tree.BuildAction_PutToken)
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, "damage", "to", T_OBJECTS], tree.BuildAction_DealDamage)
AddRule(T_ACTION_INTERNAL, [T_MOVE_ACTION], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["choose", T_ABILITIES], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [W_DRAW, T_NUMBER, W_CARD], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [W_DISCARD, T_NUMBER, W_CARD], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECT, W_DRAW, T_NUMBER, W_CARD], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECT, W_DISCARD, T_NUMBER, W_CARD], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["populate"], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["counter", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["gain", "control", "of", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["gain", "control", "of", T_OBJECTS, T_UNTIL], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["move", T_COUNTERS, "from", T_OBJECTS, "onto", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "gain", T_NUMBER, "life"], None, Object(0));

AddRule(T_ACTION_QUALIFIER_AFTER, ["COMMA", T_WHERE_X], None, Object(0)) # TODO

AddRule(T_ACTION, [T_ACTION_INTERNAL], None, Object(0))
AddRule(T_ACTION, [T_ACTION_INTERNAL, T_ACTION_QUALIFIER_AFTER], None, Object(0))

AddRule(T_ACTIONS, [T_ACTION], Ident)
AddRule(T_ACTIONS, [T_ACTION, "unless", "you", T_ACTION], None, Object(0)) # TODO

AddRule(T_CONDITION, ["whenever", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["when", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ['at', 'the', 'beginning', 'of', 'each', 'combat'], None, Object(TBeginningOfEachCombat))
AddRule(T_CONDITION, ['at', 'the', 'beginning', 'of', 'your', 'upkeep'], None, Object(0)) # TODO generalize this

AddRule(T_STATEMENT, [T_ACTIONS], tree.BuildStatement_Action)
AddRule(T_STATEMENT, [T_CONDITION, "COMMA", T_ACTIONS], None, Object(0)) # TODO
AddRule(T_STATEMENT, [T_COST, "COLON", T_ACTIONS], tree.BuildStatement_PaidAction)
AddRule(T_STATEMENT, [T_ABILITIES], tree.BuildStatement_CreatureAbility)
AddRule(T_STATEMENT, ["enchant", T_OBJECT], tree.BuildStatement_EnchantWhat)
AddRule(T_STATEMENT, ["equip", T_COST], None, Object(0)) # TODO
AddRule(T_STATEMENT, [T_OBJECTS, T_ENTER_THE_BATTLEFIELD_MOD], tree.BuildStatement_EnterTheBattleFieldMod)
AddRule(T_STATEMENT, [T_OBJECT, W_HAVE, "DQ", T_STATEMENT, "DQ"], None, Object(0)) # TODO
AddRule(T_STATEMENT, [T_OBJECT, W_HAVE, "DQ", T_STATEMENT, T_END_OF_STATEMENT, "DQ"], None, Object(0)) # TODO
AddRule(T_STATEMENT, [T_OBJECT, T_GET_EFFECTS, "as", "long", "as", "you", "control", T_OBJECTS], None, Object(0)) # TODO

AddRule(T_STATEMENT, [T_BATTALION, T_ACTIONS], tree.BuildStatement_Battalion)
AddRule(T_STATEMENT, [T_BLOODRUSH, T_STATEMENT], IdentSkip1)
AddRule(T_STATEMENT, ["overload", T_COST], IdentSkip1)

AddRule(T_STATEMENTS, [T_END_OF_STATEMENT], Ident)
AddRule(T_STATEMENTS, [T_END_OF_STATEMENT, T_STATEMENTS], IdentSkip1)
AddRule(T_STATEMENTS, [T_STATEMENT, T_END_OF_STATEMENT], IdentSkip2nd)
AddRule(T_STATEMENTS, [T_STATEMENT, T_END_OF_STATEMENT, T_STATEMENTS], MergeStatementsSkip1)
AddRule(T_STATEMENTS, [T_STATEMENT, "COMMA", "then", T_STATEMENTS], MergeStatementsSkip2)

AddRule(T_CARD, [T_STATEMENTS], Ident)

