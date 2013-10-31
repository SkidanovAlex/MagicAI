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
TAndOr = 5

OThis = 1000
OCard = 1022
OPlayer = 1024
OOpponent = 1025
OYou = 1026
OIt = 1027
OAura = 1028
OAuras = 1029

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
EThisAbility = 2020
EIslandwalk = 2021
EForestwalk = 2022
EMountainwalk = 2023

TEndOfTurn = 3001
TBeginningOfEachCombat = 3002

ClrRed = 3101
ClrBlue = 3102
ClrGreen = 3103
ClrWhite = 3104
ClrBlack = 3105
ClrMonoColored = 3106
ClrMultiColored = 3107
ClrNonRed = 3108
ClrNonBlue = 3109
ClrNonGreen = 3110
ClrNonWhite = 3111
ClrNonBlack = 3112

MAExile = 4001
MADestroy = 4002
MARegenerate = 4003
MATap = 4004
MAUntap = 4005
MAReturn = 4006
MADetain = 4007
MASacrifice = 4008
MAPut = 4009
MAShuffle = 4010
MADiscard = 4011
MADraw = 4012

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
OQBlocked = 4117
OQOther = 4118
OQRevealed = 4119
OQIndestructible = 4120
OQChosen = 4121
OQDefending = 4122
OQTapped = 4123
OQDiscarded = 4124
OQSacrificed = 4125
OQOneOfThe = 4126

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
WhoseOpponents = 4405
WhoseTargets = 4406

ODsAttacks = 4501


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
T_DMG_NUM = 48
T_PREVENT_DMG_ACTION = 49
T_DMG_WHICH_BEGIN = 50
T_DMG_WHICH_QUALIFIER = 51
T_DMG_WHICH_QUALIFIERS = 52
T_DAMAGE = 53
T_ACTION_QUALIFIER_BEFORE = 54
T_ACTION_QUALIFIERS_BEFORE = 55
T_UNDER_WHOSE_CONTROL = 56
T_TAKE_CONTROL = 57
T_EQUAL_TO = 58
T_CANT_ATC_BLOCK = 59
T_CANT_ATC_BLOCK_QUALIFIER = 60
T_CANT_ATC_BLOCK_QUALIFIERS = 61
T_ATTACK_BLOCK_BE_BLOCKED_ONE = 62
T_ATTACK_BLOCK_BE_BLOCKED = 63
T_NUMBER_INTERNAL = 64
T_MANA = 65
T_GET_EFFECT_QUALIFIER_AFTER = 66
T_GET_EFFECT_QUALIFIERS_AFTER = 67
T_GET_EFFECT_INTERNAL = 68
T_ACTIONS_TO_CHOOSE = 69
T_AT = 70
T_MOVE_ACTION_TYPES = 71
T_ACTIVATION_RESTRICTION = 72
T_CREATURE_TYPE_INTERNAL = 73
T_ACTION_QUALIFIERS_AFTER = 74
T_BASIC_LAND_TYPE = 75
T_PT_EQUAL_TO = 76
T_LOYALTY_COST = 77
T_SEARCH_ACTION = 78
T_COLOR_OR_TYPE_TERM = 79
T_COUNTER_TYPE = 80
T_PHASE_OR_STEP = 81
T_PLANESWALKER_STATEMENT = 82
T_PLANESWALKER_STATEMENTS = 83
T_NAME = 84
T_UNTIL_OPT = 85
T_FOR_EACH_OPT = 86
T_OBJECTS_OPT = 87
T_OBJECT_QUALIFIERS_AFTER_OPT = 88
T_OBJECT_QUALIFIERS_BEFORE_OPT = 89
T_DMG_WHICH = 90
T_OBJECTS_OR_NUMBER = 91
T_MOVE_FROM = 92
T_MOVE_TO_OPT = 93
T_MOVE_FROM_OPT = 94
T_MOVE_ACTION_INTERNAL = 95
T_ENTER_THE_BATTLEFIELD_MOD_OPT = 96
T_MOVE_TO_AFTER = 97
T_MOVE_FROM_OR_TO = 98
T_ROUNDED = 99
T_GREATER_LESS = 100
T_COIN_OUTCOME = 101
T_PLUS_MINUS_NUMBER = 102

W_GETS = 1001
W_HAVE = 1002
W_CARD = 1003
W_IS = 1004
W_DRAW = 1005
W_DISCARD = 1006
W_CONTROL = 1007
W_DONT = 1008
W_GAIN = 1009
W_ENTER = 1010
W_OWN = 1011
W_COUNTER = 1012
W_CAST = 1013
W_ADD = 1014
W_REVEAL = 1015
W_SHUFFLE = 1016
W_COST = 1017
W_TAP = 1018
W_TO_INTO_ONTO = 1019
W_LOSE = 1020

T_BATTALION = 300
T_BLOODRUSH = 301
T_HEROIC = 302


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
            if self.retObj == Object(0):
                return None
            return self.retObj
        return self.retFunc(*children)

def IsTerminal(state):
    return isinstance(state, basestring) or state == T_PLUS_X_PLUS_X or state == T_PIC_COST or state == T_LOYALTY_COST

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
    elif what == TAndOr and not isinstance(obj, tree.AndOrList):
        lst = tree.AndOrList(obj)
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
AddRule(T_AND_OR, ["and/or"], None, TAndOr)
AddRule(T_AND_OR, ["COMMA"], None, TComma)
AddRule(T_AND_OR, ["COMMA", "and"], None, TAnd)
AddRule(T_AND_OR, ["COMMA", "or"], None, TOr)

AddRule(T_NAME, ["THIS"], None, Object(0))
AddRule(T_NAME, ["advocate", "of", "the", "beast"], None, Object(0))
AddRule(T_NAME, ["festering", "newt"], None, Object(0))
AddRule(T_NAME, ["bubbling", "cauldron"], None, Object(0))
AddRule(T_NAME, ["bogbrew", "witch"], None, Object(0))

AddRule(T_COIN_OUTCOME, ["heads"], None, Object(0))
AddRule(T_COIN_OUTCOME, ["tails"], None, Object(0))

AddRule(T_NUMBER_INTERNAL, ["no"], None, 0)
AddRule(T_NUMBER_INTERNAL, ["a"], None, 1)
AddRule(T_NUMBER_INTERNAL, ["an"], None, 1)
AddRule(T_NUMBER_INTERNAL, ["one"], None, 1)
AddRule(T_NUMBER_INTERNAL, ["two"], None, 2)
AddRule(T_NUMBER_INTERNAL, ["three"], None, 3)
AddRule(T_NUMBER_INTERNAL, ["four"], None, 4)
AddRule(T_NUMBER_INTERNAL, ["five"], None, 5)
AddRule(T_NUMBER_INTERNAL, ["six"], None, 6)
AddRule(T_NUMBER_INTERNAL, ["seven"], None, 7)
AddRule(T_NUMBER_INTERNAL, ["eight"], None, 8)
AddRule(T_NUMBER_INTERNAL, ["ten"], None, 10)
AddRule(T_NUMBER_INTERNAL, ["twenty"], None, 20)
AddRule(T_NUMBER_INTERNAL, ["ninety-nine"], None, 99)
AddRule(T_NUMBER_INTERNAL, ["x"], None, 'x')
for i in range(51):
    AddRule(T_NUMBER_INTERNAL, [str(i)], None, i)
AddRule(T_NUMBER, [T_NUMBER_INTERNAL], None, Object(0))
AddRule(T_NUMBER, ["up", "to", T_NUMBER_INTERNAL], None, Object(0))
AddRule(T_NUMBER, ['more', "than", T_NUMBER_INTERNAL], None, Object(0))
AddRule(T_NUMBER, ['fewer', "than", T_NUMBER_INTERNAL], None, Object(0))
AddRule(T_NUMBER, [T_NUMBER_INTERNAL, "or", "more"], None, Object(0))
AddRule(T_NUMBER, [T_NUMBER_INTERNAL, "or", "greater"], None, Object(0))
AddRule(T_NUMBER, [T_NUMBER_INTERNAL, "or", "less"], None, Object(0))
AddRule(T_NUMBER, [T_NUMBER_INTERNAL, "or", "fewer"], None, Object(0))
AddRule(T_NUMBER, [T_NUMBER_INTERNAL, "times", T_NUMBER_INTERNAL], None, Object(0))
AddRule(T_NUMBER, ["any", "number", "of"], None, Object(0))
AddRule(T_NUMBER, ["any", "amount", "of"], None, Object(0))
AddRule(T_NUMBER, ["an", "amount", "of"], None, Object(0))
AddRule(T_NUMBER, ["the", "rest"], None, Object(0))
AddRule(T_NUMBER, ["that", "many"], None, Object(0))
AddRule(T_NUMBER, ["that", "much"], None, Object(0))
AddRule(T_NUMBER, ["twice", "that", "many"], None, Object(0))
AddRule(T_NUMBER, ["all"], None, Object(0))

AddRule(T_PLUS_MINUS_NUMBER, ["plus", T_NUMBER], None, Object(0))
AddRule(T_PLUS_MINUS_NUMBER, ["minus", T_NUMBER], None, Object(0))

AddRule(T_GREATER_LESS, ["greater", "than"], None, Object(0))
AddRule(T_GREATER_LESS, ["less", "than"], None, Object(0))
AddRule(T_GREATER_LESS, ["equal", "to"], None, Object(0))
AddRule(T_GREATER_LESS, ["greater", "than", "or", "equal", "to"], None, Object(0))
AddRule(T_GREATER_LESS, ["less", "than", "or", "equal", "to"], None, Object(0))

AddRule(T_DAMAGE, ["damage"], None, Object(0))
AddRule(T_DAMAGE, ["combat", "damage"], None, Object(0))

AddRule(T_BASIC_LAND_TYPE, ["swamp"], Ident)
AddRule(T_BASIC_LAND_TYPE, ["swamps"], None, "swamp")
AddRule(T_BASIC_LAND_TYPE, ["plains"], Ident)
AddRule(T_BASIC_LAND_TYPE, ["forest"], Ident)
AddRule(T_BASIC_LAND_TYPE, ["forests"], None, "forest")
AddRule(T_BASIC_LAND_TYPE, ["island"], Ident)
AddRule(T_BASIC_LAND_TYPE, ["islands"], None, "island")
AddRule(T_BASIC_LAND_TYPE, ["mountain"], Ident)
AddRule(T_BASIC_LAND_TYPE, ["mountains"], None, "mountain")

AddRule(T_CARD_TYPE, ["permanent"], Ident)
AddRule(T_CARD_TYPE, ["permanents"], Ident)
AddRule(T_CARD_TYPE, ["legendary"], Ident)
AddRule(T_CARD_TYPE, ["creature"], Ident)
AddRule(T_CARD_TYPE, ["creatures"], Ident)
AddRule(T_CARD_TYPE, ["planeswalker"], Ident)
AddRule(T_CARD_TYPE, ["planeswalkers"], Ident)
AddRule(T_CARD_TYPE, ["instant"], Ident)
AddRule(T_CARD_TYPE, ["sorcery"], Ident)
AddRule(T_CARD_TYPE, ["artifact"], Ident)
AddRule(T_CARD_TYPE, ["artifacts"], Ident)
AddRule(T_CARD_TYPE, ["equipment"], Ident)
AddRule(T_CARD_TYPE, ["enchantment"], Ident)
AddRule(T_CARD_TYPE, ["enchantments"], Ident)
AddRule(T_CARD_TYPE, ["land"], Ident)
AddRule(T_CARD_TYPE, ["lands"], Ident)
AddRule(T_CARD_TYPE, ["basic", "land"], None, "basic land")
AddRule(T_CARD_TYPE, ["nonbasic", "land"], None, "nonbasic land")
AddRule(T_CARD_TYPE, ["nonland"], Ident)
AddRule(T_CARD_TYPE, ["noncreature"], Ident)
AddRule(T_CARD_TYPE, ["nonartifact"], Ident)
AddRule(T_CARD_TYPE, ["nontoken"], Ident)
AddRule(T_CARD_TYPE, ["gate"], Ident)
AddRule(T_CARD_TYPE, ["gates"], Ident)
AddRule(T_CARD_TYPE, [T_BASIC_LAND_TYPE], Ident)

AddRule(T_OBJECT_TYPE, ["aura"], None, Object(OAura))
AddRule(T_OBJECT_TYPE, ["auras"], None, Object(OAuras))
AddRule(T_OBJECT_TYPE, [W_CARD], None, Object(OCard))
AddRule(T_OBJECT_TYPE, ["player"], None, Object(OPlayer))
AddRule(T_OBJECT_TYPE, ["players"], None, Object(OPlayer))
AddRule(T_OBJECT_TYPE, ["you"], None, Object(OYou))
AddRule(T_OBJECT_TYPE, ["opponent"], None, Object(OOpponent))
AddRule(T_OBJECT_TYPE, ["opponents"], None, Object(OOpponent))

AddRule(T_OBJECT_TYPE, ["spell"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, ["spells"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, ["ability"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, ["triggered", "ability"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, ["activated", "ability"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, ["abilities"], None, Object(0)) # TODO
AddRule(T_OBJECT_TYPE, [T_CREATURE_TYPE_INTERNAL], Ident) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE], Ident) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "spell"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "permanent"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "card"], IdentSkip2nd)
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "creature"], IdentSkip2nd)
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "spells"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "permanents"], IdentSkip2nd) # TODO
AddRule(T_OBJECT_TYPE, [T_CARD_TYPE, "cards"], IdentSkip2nd)

AddRule(T_OBJECT_INTERNAL, ["it"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, ["they"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, ["him"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, ["he", "or", "she"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, ["them"], None, Object(OIt))
AddRule(T_OBJECT_INTERNAL, [T_OBJECT_TYPE], Ident)
AddRule(T_OBJECT_INTERNAL, ["THIS"], None, Object(OThis))
AddRule(T_OBJECT_INTERNAL, ["the", "other"], None, Object(0)) # Jarad's Orders, revealing cards
AddRule(T_OBJECT_INTERNAL, ["the", "copy"], None, Object(0)) # Elite Arcanist
AddRule(T_OBJECT_INTERNAL, ["the", "copies"], None, Object(0)) # Chandra
# TODO
AddRule(T_OBJECT_INTERNAL, ["source"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["sources"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["pile"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["piles"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["token"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["tokens"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, "token"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, "tokens"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, T_CARD_TYPE, "token"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, T_CARD_TYPE, "tokens"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, T_CARD_TYPE, T_CARD_TYPE, "token"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, [T_CARD_TYPE, T_CARD_TYPE, T_CARD_TYPE, "tokens"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["the", "top", W_CARD], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["the", "top", W_CARD, "of", T_WHOSE, "library"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["the", "top", T_NUMBER, "cards", "of", T_WHOSE, "library"], None, Object(0))
AddRule(T_OBJECT_INTERNAL, ["your", "graveyard"], None, Object(0)) # elixir of immortality

# TODO: generalize 'its'
AddRule(T_OBJECT_QUALIFIER_AFTER, [T_OBJECTS, W_CONTROL], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, [T_OBJECTS, W_OWN], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, [T_OBJECTS, W_DONT, "control"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, [T_OBJECTS, "neither", W_OWN, "or", W_CONTROL], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["dealt", T_DAMAGE, "by", T_OBJECTS, "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "dealt", T_DAMAGE, "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "dealt", T_DAMAGE, "to", T_OBJECTS, "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "died"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "has", T_COUNTERS, "on", "it"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "shares", "a", "card", "type", "with", T_OBJECTS], None, Object(0)) # possibility storm
AddRule(T_OBJECT_QUALIFIER_AFTER, ["each"], None, Object(0))
#TODO
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_ABILITIES], None, IdentSkip1)
AddRule(T_OBJECT_QUALIFIER_AFTER, ["without", T_ABILITIES], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_COUNTERS_ON], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_COUNTERS], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "power", T_NUMBER], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "toughness", T_NUMBER], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "power", T_EQUAL_TO], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "toughness", T_EQUAL_TO], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "the", "same", "controller"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["blocking", "it"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["blocking", "or", "blocked", "by", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "was", "blocked", "by", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["it", "is", "blocking"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["exiled", "with", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "the", "same", "name", "as", T_OBJECT], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "different", "names"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "converted", "mana", "cost", T_NUMBER], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "converted", "mana", "cost", T_GREATER_LESS, T_WHERE_X_INTERNAL], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "converted", "mana", "costs", T_NUMBER, T_AND_OR, T_NUMBER], None, Object(0)) # firemind's foresight
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", T_COST_PART, "in", "its", "mana", "cost"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["attached", "to", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, [W_CAST, "this", "way"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["revealed", "this", "way"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["dealt", "damage", "this", "way"], None, Object(0)) # aurelia's fury
AddRule(T_OBJECT_QUALIFIER_AFTER, ["exiled", "this", "way"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["you", "exiled"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["returned", "this", "way"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["tapped", "this", "way"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["from", "among", "them"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["among", "them"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["named", T_NAME], None, Object(0)) # biovisionary
AddRule(T_OBJECT_QUALIFIER_AFTER, ["named", T_NAME, "or", T_NAME], None, Object(0)) # bogbrew witch
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "the", "chosen", "name"], None, Object(0)) # pitching needle
AddRule(T_OBJECT_QUALIFIER_AFTER, ["of", "the", "chosen", "type"], None, Object(0)) # door of destinies
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "that", "name"], None, Object(0)) # pitching needle
AddRule(T_OBJECT_QUALIFIER_AFTER, ["not", "named", T_NAME], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["with", "the", "same", "name"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["who", "lost", "life", "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "weren't", "cast"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["you", "cast"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["you", "cast", "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["at", "random"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["chosen", "at", "random"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["in", T_PART_OF_FIELD], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["on", T_PART_OF_FIELD], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["that", "was", T_MOVE_ACTION_TYPE, T_MOVE_TO_OPT, T_MOVE_FROM_OPT, "this", "turn"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["other", "than", T_OBJECTS, "card"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_AFTER, ["of", "your", "choice"], None, Object(0))

AddRule(T_OBJECT_QUALIFIER_BEFORE, ["the"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["one", "of"], None, Object(OQOneOfThe))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["another"], None, Object(OQAnother))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["other"], None, Object(OQOther))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["attacking"], None, Object(OQAttacking))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["blocking"], None, Object(OQBlocking))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["blocked"], None, Object(OQBlocked))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["tapped"], None, Object(OQTapped))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["untapped"], None, Object(OQUntapped))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["each"], None, Object(OQEach))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["each", "of", "those"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["any"], None, Object(OQAny))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["every"], None, Object(OQEvery))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["equipped"], None, Object(OQEquipped))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["target"], None, Object(OQTarget))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["that"], None, Object(OQThat))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["this"], None, Object(OQThat))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["those"], None, Object(OQThat))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["enchanted"], None, Object(OQEnchanted))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["indestructible"], None, Object(OQIndestructible))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["discarded"], None, Object(OQDiscarded))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["sacrificed"], None, Object(OQSacrificed))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["revealed"], None, Object(OQRevealed))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["chosen"], None, Object(OQChosen))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["exiled"], None, Object(0)) # angel of serenity
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["defending"], None, Object(OQDefending))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["additional"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["next"], None, Object(0))
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_NUMBER], Ident)
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_COLOR], Ident)
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_PLUS_X_PLUS_X], Ident)
AddRule(T_OBJECT_QUALIFIER_BEFORE, [T_CREATURE_TYPE_INTERNAL], Ident)
AddRule(T_OBJECT_QUALIFIER_BEFORE, ["your"], None, Object(0)) # TODO: T_WHOSE conflicts with T_NUMBER

AddRule(T_OBJECT_QUALIFIERS_AFTER, [T_EQUAL_TO], Ident)
AddRule(T_OBJECT_QUALIFIERS_AFTER, [T_OBJECT_QUALIFIER_AFTER], Ident)
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE], Ident)

#TODO
AddRule(T_OBJECT_QUALIFIERS_AFTER, [T_OBJECT_QUALIFIER_AFTER, T_OBJECT_QUALIFIERS_AFTER], None, Object(0))
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE, T_OBJECT_QUALIFIERS_BEFORE], None, Object(0))
AddRule(T_OBJECT_QUALIFIERS_BEFORE, [T_OBJECT_QUALIFIER_BEFORE, T_AND_OR, T_OBJECT_QUALIFIERS_BEFORE], AndOr)

AddRule(T_OBJECT_QUALIFIERS_AFTER_OPT, [T_OBJECT_QUALIFIERS_AFTER], Ident)
AddRule(T_OBJECT_QUALIFIERS_BEFORE_OPT, [T_OBJECT_QUALIFIERS_BEFORE], Ident)
AddRule(T_OBJECT_QUALIFIERS_AFTER_OPT, [], None, Object(0))
AddRule(T_OBJECT_QUALIFIERS_BEFORE_OPT, [], None, Object(0))

AddRule(T_OBJECT, [T_WHOSE, "controller"], None, Object(0))
AddRule(T_OBJECT, [T_WHOSE, "owner"], None, Object(0))
AddRule(T_OBJECT, [T_OBJECT_QUALIFIERS_BEFORE_OPT, T_OBJECT_INTERNAL, T_OBJECT_QUALIFIERS_AFTER_OPT], None, Object(0)) # TODO

AddRule(T_OBJECTS, [T_OBJECT], Ident)
AddRule(T_OBJECTS, ["a", "number", "of", T_OBJECTS, T_EQUAL_TO], None, Object(0))
AddRule(T_OBJECTS, ["a", "number", "of", T_OBJECTS, "from", T_PART_OF_FIELD, T_EQUAL_TO], None, Object(0)) # hack for Disciple of Phenax
AddRule(T_OBJECTS, ["a", "number", "of", T_OBJECTS, W_TO_INTO_ONTO, T_PART_OF_FIELD, T_EQUAL_TO], None, Object(0)) # hack for Evangel of Heliod
AddRule(T_OBJECTS, [T_OBJECT, T_AND_OR, T_OBJECTS], AndOr)
AddRule(T_OBJECTS, ["the", "controller", "of", T_OBJECTS], None, Object(0))
AddRule(T_OBJECTS, ["the", "owner", "of", T_OBJECTS], None, Object(0))
AddRule(T_OBJECTS_OPT, [T_OBJECTS], Ident)
AddRule(T_OBJECTS_OPT, [], None, Object(0))

AddRule(T_COLOR_OR_TYPE_TERM, ["type"], None, Object(0))
AddRule(T_COLOR_OR_TYPE_TERM, ["types"], None, Object(0))
AddRule(T_COLOR_OR_TYPE_TERM, ["color", "and", "type"], None, Object(0))
AddRule(T_COLOR_OR_TYPE_TERM, ["colors", "and", "types"], None, Object(0))
AddRule(T_COLOR_OR_TYPE_TERM, [T_OBJECT_QUALIFIER_BEFORE, T_COLOR_OR_TYPE_TERM], None, Object(0))

AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ['tapped'], None, ETBTapped)
AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ['with', "a", "number", "of", "additional", T_COUNTER_TYPE, T_COUNTERS_ON, T_EQUAL_TO, "and", "as", "a", T_CREATURE_TYPE, T_GET_EFFECT_QUALIFIER_AFTER], None, Object(0)) # master biomancer
AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ['with', T_NUMBER, "additional", T_COUNTER_TYPE, T_COUNTERS_ON], None, Object(0)) # master biomancer
AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ['with', T_COUNTERS_ON], None, Object(0)) # master biomancer
AddRule(T_ENTER_THE_BATTLEFIELD_MOD, [T_UNDER_WHOSE_CONTROL], None, Object(0)) # master biomancer
AddRule(T_ENTER_THE_BATTLEFIELD_MOD, ["attached", "to", T_OBJECTS], None, Object(0))

AddRule(T_ENTER_THE_BATTLEFIELD_MOD_OPT, [], None, Object(0))
AddRule(T_ENTER_THE_BATTLEFIELD_MOD_OPT, [T_ENTER_THE_BATTLEFIELD_MOD], Ident)
AddRule(T_ENTER_THE_BATTLEFIELD_MOD_OPT, [T_ENTER_THE_BATTLEFIELD_MOD, T_ENTER_THE_BATTLEFIELD_MOD], None, Object(0))

AddRule(T_PART_OF_FIELD_INTERNAL, ["battlefield"], None, PoFBattlefield)
AddRule(T_PART_OF_FIELD_INTERNAL, ["graveyard"], None, PoFGraveyard)
AddRule(T_PART_OF_FIELD_INTERNAL, ["graveyards"], None, PoFGraveyard)
AddRule(T_PART_OF_FIELD_INTERNAL, ["library"], None, PoFLibrary)
AddRule(T_PART_OF_FIELD_INTERNAL, ["libraries"], None, PoFLibrary)
AddRule(T_PART_OF_FIELD_INTERNAL, ["hand"], None, PoFHand)
AddRule(T_PART_OF_FIELD_INTERNAL, ["hands"], None, PoFHand)

# TODO
AddRule(T_PART_OF_FIELD, [T_PART_OF_FIELD_INTERNAL], Ident)
AddRule(T_PART_OF_FIELD, [T_WHOSE, T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_PART_OF_FIELD, [T_WHOSE, T_PART_OF_FIELD_INTERNAL, T_AND_OR, T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_PART_OF_FIELD, [T_WHOSE, T_PART_OF_FIELD_INTERNAL, "COMMA", T_PART_OF_FIELD_INTERNAL, "COMMA", T_AND_OR, T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_PART_OF_FIELD, ["a", "single", T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_PART_OF_FIELD, ["the", "top", "of", T_WHOSE, "library"], None, Object(0))
AddRule(T_PART_OF_FIELD, ["anywhere"], None, Object(0))

AddRule(T_WHOSE, ["a"], None, Object(0))
AddRule(T_WHOSE, ["the"], None, Object(0))
AddRule(T_WHOSE, ["all"], None, WhoseAnyones)
AddRule(T_WHOSE, ["your"], None, WhoseYour)
AddRule(T_WHOSE, ["its"], None, WhoseYour)
AddRule(T_WHOSE, ["their"], None, WhoseYour)
AddRule(T_WHOSE, ["its", "owner's"], None, WhoseOwners)
AddRule(T_WHOSE, ["its", "controller's"], None, WhoseControllers)
AddRule(T_WHOSE, ["their", "owners'"], None, WhoseOwners)
AddRule(T_WHOSE, ["their", "owner's"], None, WhoseOwners)
AddRule(T_WHOSE, ["their", "controllers'"], None, WhoseControllers)
AddRule(T_WHOSE, ["their", "controller's"], None, WhoseControllers)
AddRule(T_WHOSE, ["your", "opponents'"], None, WhoseOpponents)
AddRule(T_WHOSE, ["all", "opponents'"], None, WhoseOpponents)
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "opponent's"], None, WhoseOpponents)
AddRule(T_WHOSE, ["his", "or", "her"], None, WhoseHis)
AddRule(T_WHOSE, ["THIS's"], None, Object(0))
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "player's"], None, WhoseTargets)
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "spell's"], None, Object(0))
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "creature's"], None, Object(0))
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "land's"], None, Object(0))
AddRule(T_WHOSE, [T_OBJECT_QUALIFIERS_BEFORE, "permanent's"], None, Object(0))

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
AddRule(T_ABILITY, ["scavenge", T_COST], None, Object(0))
AddRule(T_ABILITY, ["bestow", T_COST], None, Object(0))
AddRule(T_ABILITY, ["monstrosity", T_NUMBER], None, Object(0))
AddRule(T_ABILITY, ["swampwalk"], None, Object(ESwampwalk))
AddRule(T_ABILITY, ["islandwalk"], None, Object(EIslandwalk))
AddRule(T_ABILITY, ["forestwalk"], None, Object(EForestwalk))
AddRule(T_ABILITY, ["mountainwalk"], None, Object(EMountainwalk))
AddRule(T_ABILITY, ["lifelink"], None, Object(ELifelink))
AddRule(T_ABILITY, ["deathtouch"], None, Object(EDeathtouch))
AddRule(T_ABILITY, ["scavenge"], None, Object(0))
AddRule(T_ABILITY, ["flash"], None, Object(EFlash))
AddRule(T_ABILITY, ["intimidate"], None, Object(EIntimidate))
AddRule(T_ABILITY, ["hexproof"], None, Object(EHexproof))
AddRule(T_ABILITY, ["this", "ability"], None, Object(EThisAbility))
AddRule(T_ABILITY, ["indestructible"], None, Object(0))
AddRule(T_ABILITY, [T_PROTECTION], None, Object(0))

AddRule(T_ABILITIES, [T_ABILITY], Ident)
AddRule(T_ABILITIES, [T_ABILITY, T_AND_OR, T_ABILITIES], AndOr)

AddRule(T_CREATURE_TYPE_INTERNAL, ["angel"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["assassin"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["beast"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["bird"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["boar"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["cat"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["centaur"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["cleric"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["crab"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["devil"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["demon"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["demons"], None, "demon")
AddRule(T_CREATURE_TYPE_INTERNAL, ["non-demon"], None, Object(0))
AddRule(T_CREATURE_TYPE_INTERNAL, ["dragon"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["dragons"], None, "dragon")
AddRule(T_CREATURE_TYPE_INTERNAL, ["elemental"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["frog"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["giant"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["goat"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["goblin"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["golem"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["gorgon"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["non-gorgon"], None, Object(0))
AddRule(T_CREATURE_TYPE_INTERNAL, ["harpy"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["horror"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["human"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["illusion"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["insect"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["knight"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["lizard"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["minotaur"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["mutant"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["nightmare"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["ooze"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["thrull"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["rat"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["rats"], None, "rat")
AddRule(T_CREATURE_TYPE_INTERNAL, ["saproling"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["satyr"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["sliver"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["slivers"], None, "sliver")
AddRule(T_CREATURE_TYPE_INTERNAL, ["soldier"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["spirit"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["rhino"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["rogue"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["rogues"], None, "rogue")
AddRule(T_CREATURE_TYPE_INTERNAL, ["wall"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["walls"], None, "wall")
AddRule(T_CREATURE_TYPE_INTERNAL, ["warrior"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["weird"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["wolf"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["wurm"], Ident)
AddRule(T_CREATURE_TYPE_INTERNAL, ["zombie"], Ident)

AddRule(T_CREATURE_TYPE, [T_CREATURE_TYPE_INTERNAL], Ident)
AddRule(T_CREATURE_TYPE, [T_CREATURE_TYPE_INTERNAL, T_CREATURE_TYPE], None, Object(0))
 

AddRule(T_COLOR, ["red"], None, Object(ClrRed))
AddRule(T_COLOR, ["blue"], None, Object(ClrBlue))
AddRule(T_COLOR, ["green"], None, Object(ClrGreen))
AddRule(T_COLOR, ["white"], None, Object(ClrWhite))
AddRule(T_COLOR, ["black"], None, Object(ClrBlack))
AddRule(T_COLOR, ["nonred"], None, Object(ClrNonRed))
AddRule(T_COLOR, ["nonblue"], None, Object(ClrNonBlue))
AddRule(T_COLOR, ["nongreen"], None, Object(ClrNonGreen))
AddRule(T_COLOR, ["nonwhite"], None, Object(ClrNonWhite))
AddRule(T_COLOR, ["nonblack"], None, Object(ClrNonBlack))
AddRule(T_COLOR, ["colorless"], None, Object(0))
AddRule(T_COLOR, ["monocolored"], None, Object(ClrMonoColored))
AddRule(T_COLOR, ["multicolored"], None, Object(ClrMultiColored))
AddRule(T_COLOR, ["the", "chosen", "color"], None, Object(0))

AddRule(T_COLORS, [T_COLOR], Ident)
AddRule(T_COLORS, [T_COLOR, T_AND_OR, T_COLORS], AndOr)
AddRule(T_COLORS, ["the", "color", "of", "your", "choice"], None, Object(0))
AddRule(T_COLORS, ["at", "least", "one", "of", "the", "chosen", "colors"], None, Object(0)) # tablet of giulds -- consider generalizing
AddRule(T_COLORS, ["that", "color"], None, Object(0))

# TODO
AddRule(T_PROTECTION, ["protection", "from", T_OBJECTS], IdentSkip2)
AddRule(T_PROTECTION, ["protection", "from", T_COLORS], IdentSkip2)
AddRule(T_PROTECTION, ["protection", "from", T_COLORS, T_AND_OR, "from", T_COLORS], None, Object(0))

AddRule(W_GAIN, ["gain"], None, Object(0))
AddRule(W_GAIN, ["gains"], None, Object(0))

AddRule(W_ENTER, ["enter"], None, Object(0))
AddRule(W_ENTER, ["enters"], None, Object(0))

AddRule(W_GETS, ["get"], None, Object(0))
AddRule(W_GETS, ["gets"], None, Object(0))
AddRule(W_GETS, [W_GAIN], None, Object(0))

AddRule(W_HAVE, ["have"], None, Object(0))
AddRule(W_HAVE, ["has"], None, Object(0))

AddRule(W_CARD, ["card"], None, Object(0))
AddRule(W_CARD, ["cards"], None, Object(0))

AddRule(W_REVEAL, ["reveal"], None, Object(0))
AddRule(W_REVEAL, ["reveals"], None, Object(0))

AddRule(W_SHUFFLE, ["shuffle"], None, Object(0))
AddRule(W_SHUFFLE, ["shuffles"], None, Object(0))

AddRule(W_IS, ["is"], None, Object(0))
AddRule(W_IS, ["are"], None, Object(0))

AddRule(W_CAST, ["cast"], None, Object(0))
AddRule(W_CAST, ["casts"], None, Object(0))

AddRule(W_COST, ["cost"], None, Object(0))
AddRule(W_COST, ["costs"], None, Object(0))

AddRule(W_TAP, ["tap"], None, Object(0))
AddRule(W_TAP, ["taps"], None, Object(0))

AddRule(W_TO_INTO_ONTO, ["to"], None, Object(0))
AddRule(W_TO_INTO_ONTO, ["into"], None, Object(0))
AddRule(W_TO_INTO_ONTO, ["onto"], None, Object(0))

AddRule(W_LOSE, ["lose"], None, Object(0))
AddRule(W_LOSE, ["loses"], None, Object(0))

AddRule(W_ADD, ["add"], None, Object(0))
AddRule(W_ADD, ["adds"], None, Object(0))

AddRule(W_DRAW, ["draw"], None, Object(0))
AddRule(W_DRAW, ["draws"], None, Object(0))

AddRule(W_DISCARD, ["discard"], None, Object(0))
AddRule(W_DISCARD, ["discards"], None, Object(0))

AddRule(W_CONTROL, ["control"], None, Object(0))
AddRule(W_CONTROL, ["controls"], None, Object(0))

AddRule(W_OWN, ["own"], None, Object(0))
AddRule(W_OWN, ["owns"], None, Object(0))

AddRule(W_COUNTER, ["counter"], None, Object(0))
AddRule(W_COUNTER, ["counters"], None, Object(0))

AddRule(W_DONT, ["doesn't"], None, Object(0))
AddRule(W_DONT, ["don't"], None, Object(0))

AddRule(T_FOR_EACH, ["for", "each", T_OBJECTS], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", "of", T_OBJECTS], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", T_OBJECTS, "put", "into", T_PART_OF_FIELD, "this", "way"], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", T_OBJECTS, "destroyed", "this", "way"], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", T_COUNTERS_ON], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", "of", "its", "colors"], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", "of", "the", "chosen", "colors", "it", "is"], None, Object(0)) # Tablet of Guilds
AddRule(T_FOR_EACH, ["for", "each", T_NUMBER, "life", "your", "opponents", "have", "lost", T_UNTIL_OPT], None, Object(0))
AddRule(T_FOR_EACH, ["for", "each", "coin", "that", "comes", "up", T_COIN_OUTCOME], None, Object(0))
AddRule(T_FOR_EACH_OPT, [T_FOR_EACH], Ident)
AddRule(T_FOR_EACH_OPT, [], None, Object(0))

AddRule(T_TAKE_CONTROL, ["take", "control"], None, Object(0))
AddRule(T_TAKE_CONTROL, [W_GAIN, "control"], None, Object(0))

AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, T_PLUS_X_PLUS_X], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, T_PLUS_X_PLUS_X, "or", T_PLUS_X_PLUS_X], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, ["loses", T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, ["loses", "all", "abilities"], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, [W_HAVE, T_ABILITIES], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, [W_IS, "indestructible"], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, [W_IS, "unblockable"], IdentSkip1)
AddRule(T_GET_EFFECT_INTERNAL, [W_HAVE, "DQ", T_STATEMENT, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_HAVE, "DQ", T_STATEMENTS, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, "DQ", T_STATEMENT, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, "DQ", T_STATEMENTS, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, "an", "emblem", "with", "DQ", T_STATEMENT, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_GETS, "an", "emblem", "with", "DQ", T_STATEMENTS, "DQ"], None, Object(0)) # TODO
AddRule(T_GET_EFFECT_INTERNAL, [W_IS, T_OBJECTS], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, [W_IS, T_OBJECTS, "type"], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, ["become", T_OBJECTS], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, ["becomes", T_OBJECTS], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, ["isn't", T_OBJECTS], None, Object(0))
AddRule(T_GET_EFFECT_INTERNAL, [W_IS, T_COLOR_OR_TYPE_TERM], None, Object(0))

AddRule(T_GET_EFFECT_QUALIFIER_AFTER, [T_UNTIL], None, Object(0))
AddRule(T_GET_EFFECT_QUALIFIER_AFTER, [T_FOR_EACH], None, Object(0))
AddRule(T_GET_EFFECT_QUALIFIER_AFTER, ["in", "addition", "to", T_WHOSE, T_COLOR_OR_TYPE_TERM], None, Object(0))
AddRule(T_GET_EFFECT_QUALIFIERS_AFTER, [T_GET_EFFECT_QUALIFIER_AFTER], None, Object(0))
AddRule(T_GET_EFFECT_QUALIFIERS_AFTER, [T_GET_EFFECT_QUALIFIER_AFTER, T_GET_EFFECT_QUALIFIERS_AFTER], None, Object(0))

AddRule(T_GET_EFFECT, [T_GET_EFFECT_INTERNAL], None, Object(0))
AddRule(T_GET_EFFECT, [T_GET_EFFECT_INTERNAL, T_GET_EFFECT_QUALIFIERS_AFTER], None, Object(0))

AddRule(T_GET_EFFECTS, [T_GET_EFFECT], Ident)
AddRule(T_GET_EFFECTS, [T_GET_EFFECT, T_AND_OR, T_GET_EFFECTS], AndOr)

AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["attack"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["block"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["attacks"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["blocks"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["attacks", T_OBJECTS], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["blocks", T_OBJECTS], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["be", "blocked"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["is", "blocked"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED_ONE, ["becomes", "blocked"], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED, [T_ATTACK_BLOCK_BE_BLOCKED_ONE], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED, ["must", T_ATTACK_BLOCK_BE_BLOCKED_ONE], None, Object(0))
AddRule(T_ATTACK_BLOCK_BE_BLOCKED, [T_ATTACK_BLOCK_BE_BLOCKED_ONE, T_AND_OR, T_ATTACK_BLOCK_BE_BLOCKED], AndOr)

AddRule(T_CANT_ATC_BLOCK_QUALIFIER, [T_UNTIL], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, [T_OBJECTS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["this", "combat"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["alone"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["by", T_OBJECTS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["except", T_CANT_ATC_BLOCK_QUALIFIER], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["only", T_OBJECTS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIER, ["during", "extra", "turns"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIERS, [T_CANT_ATC_BLOCK_QUALIFIER], None, Object(0))
AddRule(T_CANT_ATC_BLOCK_QUALIFIERS, [T_CANT_ATC_BLOCK_QUALIFIER, T_CANT_ATC_BLOCK_QUALIFIERS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, ["can", T_ATTACK_BLOCK_BE_BLOCKED], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, ["can", T_ATTACK_BLOCK_BE_BLOCKED, T_CANT_ATC_BLOCK_QUALIFIERS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, ["can", "only", T_ATTACK_BLOCK_BE_BLOCKED, T_CANT_ATC_BLOCK_QUALIFIERS], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, ["can't", T_ATTACK_BLOCK_BE_BLOCKED], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, ["can't", T_ATTACK_BLOCK_BE_BLOCKED, T_CANT_ATC_BLOCK_QUALIFIERS], None, Object(0))
# TODO: some of these might be reasonable to formalize later
AddRule(T_CANT_ATC_BLOCK, ["can", "block", T_OBJECTS, "each", "combat"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, [T_ATTACK_BLOCK_BE_BLOCKED, "each", "turn", "if", "able"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, [T_ATTACK_BLOCK_BE_BLOCKED, "this", "turn", "if", "able"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, [T_ATTACK_BLOCK_BE_BLOCKED, "each", "combat", "if", "able"], None, Object(0))
AddRule(T_CANT_ATC_BLOCK, [T_ATTACK_BLOCK_BE_BLOCKED, "this", "combat", "if", "able"], None, Object(0))

AddRule(T_COUNTER_TYPE, [T_PLUS_X_PLUS_X], Ident)
AddRule(T_COUNTER_TYPE, ["blaze"], Ident)
AddRule(T_COUNTER_TYPE, ["muster"], Ident)
AddRule(T_COUNTER_TYPE, ["loyalty"], Ident)
AddRule(T_COUNTER_TYPE, ["filibuster"], Ident)
AddRule(T_COUNTER_TYPE, ["charge"], Ident)
AddRule(T_COUNTER_TYPE, ["wish"], Ident)
AddRule(T_COUNTER_TYPE, ["fate"], Ident)

AddRule(T_COUNTERS, [T_NUMBER, T_COUNTER_TYPE, W_COUNTER], None, Object(0)) # TODO
AddRule(T_COUNTERS, [T_NUMBER, W_COUNTER], None, Object(0)) # TODO
AddRule(T_COUNTERS, [T_COUNTER_TYPE, W_COUNTER], None, Object(0)) # TODO
AddRule(T_COUNTERS, [W_COUNTER], None, Object(0)) # TODO
AddRule(T_COUNTERS, ["another", "of", "those", W_COUNTER], None, Object(0)) # TODO

AddRule(T_COUNTERS_ON, [T_COUNTERS, "on", T_OBJECTS], None, Object(0)) # TODO

AddRule(T_PUT_COUNTER, ["put", T_COUNTERS_ON, T_FOR_EACH_OPT], None, Object(0)) # TODO
AddRule(T_PUT_COUNTER, ["put", "a", "number", "of", T_COUNTERS_ON, T_EQUAL_TO], None, Object(0)) # TODO
AddRule(T_PUT_COUNTER, ["distribute", "a", "number", "of", T_COUNTERS, T_EQUAL_TO, "among", T_OBJECTS], None, Object(0)) # Vastwood Hydra
AddRule(T_PUT_COUNTER, ["double", "the", "number", "of", T_COUNTERS_ON, T_FOR_EACH_OPT], None, Object(0)) # TODO

AddRule(T_REMOVE_COUNTER, ["remove", T_COUNTERS, "from", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_REMOVE_COUNTER, ["remove", T_COUNTERS, "from", "among", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_REMOVE_COUNTER, ["remove", T_COUNTERS, "from", T_OBJECTS, T_FOR_EACH], None, Object(0)) # TODO

AddRule(T_UNTIL, ['until', 'end', 'of', 'turn'], None, Object(TEndOfTurn))
AddRule(T_UNTIL, ['until', T_WHOSE, "next", 'turn'], None, Object(0))
AddRule(T_UNTIL, ['until', T_OBJECTS, T_OBJECT_DOES], None, Object(0))
AddRule(T_UNTIL, ['this', 'turn'], None, Object(TEndOfTurn))
AddRule(T_UNTIL_OPT, [T_UNTIL], Ident)
AddRule(T_UNTIL_OPT, [], None, Object(0))

AddRule(T_MOVE_ACTION_TYPE, ["exile"], None, Object(MAExile))
AddRule(T_MOVE_ACTION_TYPE, ["exiles"], None, Object(MAExile))
AddRule(T_MOVE_ACTION_TYPE, ["destroy"], None, Object(MADestroy))
AddRule(T_MOVE_ACTION_TYPE, ["regenerate"], None, Object(MARegenerate))
AddRule(T_MOVE_ACTION_TYPE, ["tap"], None, Object(MATap))
AddRule(T_MOVE_ACTION_TYPE, ["untap"], None, Object(MAUntap))
AddRule(T_MOVE_ACTION_TYPE, ["return"], None, Object(MAReturn))
AddRule(T_MOVE_ACTION_TYPE, ["returns"], None, Object(MAReturn))
AddRule(T_MOVE_ACTION_TYPE, ["detain"], None, Object(MADetain))
AddRule(T_MOVE_ACTION_TYPE, ["sacrifice"], None, Object(MASacrifice))
AddRule(T_MOVE_ACTION_TYPE, ["sacrifices"], None, Object(MASacrifice))
AddRule(T_MOVE_ACTION_TYPE, ["put"], None, Object(MAPut))
AddRule(T_MOVE_ACTION_TYPE, ["puts"], None, Object(MAPut))
AddRule(T_MOVE_ACTION_TYPE, ["shuffle"], None, Object(MAShuffle))
AddRule(T_MOVE_ACTION_TYPE, [W_DRAW], None, Object(MADraw))
AddRule(T_MOVE_ACTION_TYPE, [W_DISCARD], None, Object(MADiscard))
AddRule(T_MOVE_ACTION_TYPES, [T_MOVE_ACTION_TYPE], Ident)
AddRule(T_MOVE_ACTION_TYPES, [T_MOVE_ACTION_TYPE, T_AND_OR, T_MOVE_ACTION_TYPES], AndOr)

AddRule(T_BATTALION, ['battalion', 'DASH', 'whenever', 'THIS', 'and', 'at', 'least', 'two', 'other', 'creatures', 'attack', 'COMMA'], None, Object(Dummy))
AddRule(T_BLOODRUSH, ['bloodrush', 'DASH'], None, Object(Dummy))
AddRule(T_HEROIC, ['heroic', 'DASH'], None, Object(Dummy))

AddRule(T_COST_PART, [T_PIC_COST], Ident)
AddRule(T_COST_PART, [T_MOVE_ACTION], Ident)
AddRule(T_COST_PART, ["pay", T_NUMBER, "life"], None, Object(0))
AddRule(T_COST_PART, [T_REMOVE_COUNTER], None, Object(0))
AddRule(T_COST, [T_COST_PART], Ident)
AddRule(T_COST, [T_COST_PART, T_COST], None, Object(0))
AddRule(T_COST, [T_COST_PART, "COMMA", T_COST], None, Object(0))

AddRule(T_MANA, [T_PIC_COST], Ident)
AddRule(T_MANA, [T_PIC_COST, T_MANA], None, Object(0))
AddRule(T_MANA, [T_PIC_COST, T_AND_OR, T_MANA], AndOr)
AddRule(T_MANA, [T_NUMBER, "mana"], None, Object(0)) # color is expected later (see Zhur-Taa Ancient from DGM)
AddRule(T_MANA, [T_NUMBER, T_PIC_COST], None, Object(0))
AddRule(T_MANA, [T_NUMBER, "mana", "of", "any", "color"], None, Object(0))
AddRule(T_MANA, [T_NUMBER, "mana", "of", "that", "color"], None, Object(0))
AddRule(T_MANA, [T_NUMBER, "mana", "in", "any", "combination", "of", "colors"], None, Object(0))
AddRule(T_MANA, [T_NUMBER, "mana", "in", "any", "combination", "of", T_MANA], None, Object(0))

AddRule(T_UNDER_WHOSE_CONTROL, ["under", T_WHOSE, "control"], None, Object(0))

AddRule(T_ENTERS_THE_BF_PREFIX, [W_ENTER, "the", "battlefield"], None, Object(0))
AddRule(T_ENTERS_THE_BF, [T_ENTERS_THE_BF_PREFIX], None, Object(0))
AddRule(T_ENTERS_THE_BF, [T_ENTERS_THE_BF_PREFIX, T_UNDER_WHOSE_CONTROL], None, Object(0))

AddRule(T_OBJECT_DOES, [T_ENTERS_THE_BF], Ident)
AddRule(T_OBJECT_DOES, ["leaves", "the", T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_OBJECT_DOES, ["would", "leave", "the", T_PART_OF_FIELD_INTERNAL], None, Object(0))
AddRule(T_OBJECT_DOES, ["would", "draw", T_NUMBER, W_CARD], None, Object(0))
AddRule(T_OBJECT_DOES, ["would", "draw", T_NUMBER, W_CARD, "while", T_OBJECTS, "have", T_NUMBER, "cards", "in", "hand"], None, Object(0)) # blood scrivener
AddRule(T_OBJECT_DOES, ["would", "draw", T_NUMBER, W_CARD, "except", "the", "first", "one", "he", "or", "she", "draws", "in", "each", "of", "his", "or", "her", "draw", "steps"], None, Object(0)) # notion thief
AddRule(T_OBJECT_DOES, ["would", "deal", T_DAMAGE, "to", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, ["evolves"], None, Object(0))
AddRule(T_OBJECT_DOES, [T_ATTACK_BLOCK_BE_BLOCKED], None, Object(0))
AddRule(T_OBJECT_DOES, [T_ATTACK_BLOCK_BE_BLOCKED, T_OBJECTS, "and", "isn't", "blocked"], None, Object(0)) # master of cruelties
AddRule(T_OBJECT_DOES, ['attacks', "for", "the", "first", "time", "each", "turn"], None, Object(0))
AddRule(T_OBJECT_DOES, ['becomes', 'the', 'target', 'of', T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, ['becomes', 'monstrous'], None, Object(0))
AddRule(T_OBJECT_DOES, ['dies'], None, Object(ODsAttacks))
AddRule(T_OBJECT_DOES, ['dies', 'this', "turn"], None, Object(0))
AddRule(T_OBJECT_DOES, ['deal', T_DAMAGE], None, Object(0))
AddRule(T_OBJECT_DOES, ['deals', T_DAMAGE], None, Object(0))
AddRule(T_OBJECT_DOES, ['deal', T_DAMAGE, "to", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_OBJECT_DOES, ['deals', T_DAMAGE, "to", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_OBJECT_DOES, ["is", "dealt", T_DAMAGE], None, Object(0))
AddRule(T_OBJECT_DOES, ["is", "dealt", T_DAMAGE, "by", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, ["is", "dealt", T_DAMAGE, "by", T_OBJECTS, "or", "by", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, ["is", "put", "into", T_PART_OF_FIELD, T_ENTER_THE_BATTLEFIELD_MOD_OPT, "from", T_PART_OF_FIELD], None, Object(0))
AddRule(T_OBJECT_DOES, ["becomes", "tapped"], None, Object(0))
AddRule(T_OBJECT_DOES, [T_MOVE_ACTION], None, Object(0))
AddRule(T_OBJECT_DOES, [W_TAP, T_OBJECTS, "for", "mana"], None, Object(0))
AddRule(T_OBJECT_DOES, ["is", "tapped", "for", "mana"], None, Object(0))
AddRule(T_OBJECT_DOES, ["is", T_COLORS], None, Object(0))
AddRule(T_OBJECT_DOES, [W_GAIN, "life"], None, Object(0))
AddRule(T_OBJECT_DOES, [W_HAVE, T_COUNTERS_ON], None, Object(0))
AddRule(T_OBJECT_DOES, [W_HAVE, T_NUMBER, "life"], None, Object(0))
AddRule(T_OBJECT_DOES, ["play", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, [W_CAST, T_OBJECTS], None, Object(0)) # TODO generalize this
AddRule(T_OBJECT_DOES, [W_CAST, T_OBJECTS, "that", "targets", T_OBJECTS], None, Object(0))
AddRule(T_OBJECT_DOES, [W_CAST, T_OBJECTS, T_AT], None, Object(0)) # TODO generalize this
AddRule(T_OBJECT_DOES, [W_CAST, "your", "second", "spell", "each", "turn"], None, Object(0)) # TODO generalize this
AddRule(T_OBJECT_DOES, [W_CAST, T_OBJECTS, "from", T_PART_OF_FIELD], None, Object(0)) # TODO generalize this
AddRule(T_OBJECT_DOES, ["scry"], None, Object(0))

AddRule(T_PT_EQUAL_TO, ["power", "is", T_EQUAL_TO], None, Object(0))
AddRule(T_PT_EQUAL_TO, ["toughness", "is", T_EQUAL_TO], None, Object(0))
AddRule(T_PT_EQUAL_TO, ["power", "and", "toughness", "are", "each", T_EQUAL_TO], None, Object(0))
AddRule(T_PT_EQUAL_TO, ["power", T_EQUAL_TO], None, Object(0))
AddRule(T_PT_EQUAL_TO, ["toughness", T_EQUAL_TO], None, Object(0))
AddRule(T_PT_EQUAL_TO, ["power", "and", "toughness", "each", T_EQUAL_TO], None, Object(0))

AddRule(T_WHERE_X_INTERNAL, [T_OBJECT_QUALIFIERS_BEFORE, "spell's", "converted", "mana", "cost"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_OBJECT_QUALIFIERS_BEFORE, "card's", "converted", "mana", "cost"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "converted", "mana", "cost", "of", "the", T_OBJECT_QUALIFIER_BEFORE, "card"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "converted", "mana", "cost", "of", "the", T_OBJECT_QUALIFIER_BEFORE, "spell"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["its", "converted", "mana", "cost"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "power", "of", "the", T_OBJECTS], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "power"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "toughness"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "power", "plus", "its", "toughness"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "number", "of", T_OBJECTS], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "number", "of", T_COUNTERS], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "number", "of", T_COUNTERS, "on", T_OBJECTS], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "number", "of", T_COUNTERS, "removed", "this", "way"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "damage", "dealt", "this", "way"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "greatest", "power", "among", T_OBJECTS, T_OBJECTS, W_CONTROL], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "greatest", "number", "of", T_OBJECTS, T_OBJECTS, "discarded", "this", "way"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "life", "lost", "this", "way"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "total", "life", "lost", "by", "your", "opponents", T_UNTIL], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, ["the", "amount", "of", "life", "you've", "gained", T_UNTIL], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "mana", "cost"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "life", "total"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "starting", "life", "total"], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_WHOSE, "devotion", "to", T_COLORS], None, Object(0))
AddRule(T_WHERE_X_INTERNAL, [T_NUMBER], None, Object(0))
AddRule(T_WHERE_X, ["where", "x", "is", T_WHERE_X_INTERNAL], None, Object(0))
AddRule(T_EQUAL_TO, [T_GREATER_LESS, T_WHERE_X_INTERNAL], None, Object(0))

AddRule(T_END_OF_STATEMENT, ["DOT"], None, Object(EndOfStatement))

AddRule(T_ROUNDED, ["rounded", "up"], IdentSkip1)
AddRule(T_ROUNDED, ["rounded", "down"], IdentSkip1)

AddRule(T_OBJECTS_OR_NUMBER, [T_OBJECTS], Ident)
AddRule(T_OBJECTS_OR_NUMBER, [T_NUMBER], Ident)
AddRule(T_OBJECTS_OR_NUMBER, ["the", "top", "half", "of", "his", "or", "her", "library", "COMMA", T_ROUNDED, "COMMA"], None, Object(0)) # traumatize

AddRule(T_MOVE_TO, [W_TO_INTO_ONTO, T_PART_OF_FIELD, T_ENTER_THE_BATTLEFIELD_MOD_OPT], None, Object(0))
AddRule(T_MOVE_TO, ["on", "top", "of", T_WHOSE, "library"], None, Object(0))
AddRule(T_MOVE_TO, ["on", "the", "bottom", "of", T_WHOSE, "library"], None, Object(0))
AddRule(T_MOVE_TO, ["back"], None, Object(0))
AddRule(T_MOVE_TO, ["there"], None, Object(0)) # see Grim Return
AddRule(T_MOVE_TO, ["anywhere", "else"], None, Object(0)) # see Whip of Erebos

AddRule(T_MOVE_FROM, ["from", T_PART_OF_FIELD], None, Object(0))
AddRule(T_MOVE_FROM, ["from", "it"], None, Object(0)) # for cases when part of field (e.g name) is implied, see Duress for example

AddRule(T_MOVE_TO_AFTER, [], None, Object(0))
AddRule(T_MOVE_TO_AFTER, ["in", "any", "order"], None, Object(0))
AddRule(T_MOVE_TO_AFTER, ["in", "a", "random", "order"], None, Object(0))
AddRule(T_MOVE_TO_AFTER, ["that's", "a", "copy", "of", T_OBJECTS], None, Object(0))
AddRule(T_MOVE_TO_AFTER, ["with", "DQ", T_STATEMENTS, "DQ"], None, Object(0))

AddRule(T_MOVE_TO_OPT, [], None, Object(0))
AddRule(T_MOVE_TO_OPT, [T_MOVE_TO, T_MOVE_TO_AFTER], None, Object(0))

AddRule(T_MOVE_FROM_OPT, [], None, Object(0))
AddRule(T_MOVE_FROM_OPT, [T_MOVE_FROM], Ident)

AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPES, T_MOVE_ACTION_INTERNAL], None, Object(0))
AddRule(T_MOVE_ACTION, [T_MOVE_ACTION_TYPES, T_MOVE_ACTION_INTERNAL, "face", "down"], None, Object(0))

AddRule(T_MOVE_FROM_OR_TO, [T_MOVE_FROM], Ident)
AddRule(T_MOVE_FROM_OR_TO, [T_MOVE_TO], Ident)
AddRule(T_MOVE_FROM_OR_TO, [T_MOVE_FROM, T_MOVE_TO], None, Object(0))

AddRule(T_MOVE_ACTION_INTERNAL, [T_OBJECTS_OR_NUMBER, T_MOVE_FROM_OPT, T_MOVE_TO_OPT, T_FOR_EACH_OPT, T_UNTIL_OPT], None, Object(0))
AddRule(T_MOVE_ACTION_INTERNAL, [T_OBJECTS_OR_NUMBER, T_MOVE_FROM_OR_TO, T_AND_OR, T_OBJECTS_OR_NUMBER, T_MOVE_FROM_OPT, T_MOVE_TO_OPT], None, Object(0))

AddRule(T_SEARCH_ACTION, ["search", T_PART_OF_FIELD, "for", T_OBJECTS, "and", T_MOVE_ACTION], None, Object(0))
AddRule(T_SEARCH_ACTION, ["search", T_PART_OF_FIELD, "for", T_OBJECTS, "COMMA", T_MOVE_ACTION], None, Object(0))
AddRule(T_SEARCH_ACTION, ["search", T_PART_OF_FIELD, "for", T_OBJECTS, "and", "reveal", "them"], None, Object(0))
AddRule(T_SEARCH_ACTION, ["search", T_PART_OF_FIELD, "for", T_OBJECTS, "COMMA", "reveal", T_OBJECTS, "COMMA", "put", T_OBJECTS, T_MOVE_TO], None, Object(0))
AddRule(T_SEARCH_ACTION, ["search", T_PART_OF_FIELD, "for", T_OBJECTS, "COMMA", "reveal", T_OBJECTS, "COMMA", "and", "put", T_OBJECTS, T_MOVE_TO], None, Object(0))

AddRule(T_DMG_NUM, ["the", "next", T_NUMBER], None, Object(0))
AddRule(T_DMG_NUM, ["all"], Ident)

AddRule(T_DMG_WHICH_BEGIN, [T_DMG_NUM, T_DAMAGE, "that", "would", "be", 'dealt'], None, Object(0))
AddRule(T_DMG_WHICH_BEGIN, [T_DMG_NUM, T_DAMAGE, T_OBJECTS, "would", 'deal'], None, Object(0))
AddRule(T_DMG_WHICH_QUALIFIER, ["to", T_OBJECTS], None, Object(0))
AddRule(T_DMG_WHICH_QUALIFIER, [T_UNTIL], None, Object(0))
AddRule(T_DMG_WHICH_QUALIFIER, ["by", T_OBJECTS], None, Object(0))
AddRule(T_DMG_WHICH_QUALIFIERS, [T_DMG_WHICH_QUALIFIER], None, Object(0))
AddRule(T_DMG_WHICH_QUALIFIERS, [T_DMG_WHICH_QUALIFIER, T_DMG_WHICH_QUALIFIERS], None, Object(0))
AddRule(T_DMG_WHICH, [T_DMG_WHICH_BEGIN, T_DMG_WHICH_QUALIFIERS], None, Object(0))

AddRule(T_PREVENT_DMG_ACTION, ["prevent", T_DMG_WHICH], None, Object(0))

AddRule(T_ACTIVATION_RESTRICTION, ["activate", "this", "ability", "only", "once", "each", "turn"], None, Object(0));
AddRule(T_ACTIVATION_RESTRICTION, ["activate", "this", "ability", "only", "if", T_OBJECTS, W_CONTROL, T_OBJECTS], None, Object(0));
AddRule(T_ACTIVATION_RESTRICTION, ["only", "an", "opponent", "may", "activate", "this", "ability"], None, Object(0));
AddRule(T_ACTIVATION_RESTRICTION, ["activate", "this", "ability", "only", "any", "time", "you", "could", W_CAST, "a", "sorcery"], None, Object(0));

AddRule(T_ACTION_INTERNAL, ["scry", T_NUMBER], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["play", "with", "the", "top", "card", "of", "your", "library", "revealed"], None, Object(0)) # Garruk's Horde
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_GET_EFFECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_CANT_ATC_BLOCK], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_GET_EFFECTS, "and", T_CANT_ATC_BLOCK], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_GET_EFFECTS, "and", "deals", T_NUMBER, T_DAMAGE, "to", T_OBJECTS], None, Object(0)) # TODO

AddRule(T_ACTION_INTERNAL, [T_PUT_COUNTER], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_REMOVE_COUNTER], None, Object(0))
# tokens
AddRule(T_ACTION_INTERNAL, [T_NUMBER, T_COUNTERS, "are", "placed"], None, Object(0)) # Corpsejack Menace
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, T_DAMAGE, "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, T_DAMAGE, T_PLUS_MINUS_NUMBER, "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, T_DAMAGE, "divided", "as", "you", "choose", "among", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_DAMAGE, "to", T_OBJECTS, T_EQUAL_TO], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_DAMAGE, T_EQUAL_TO, "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, T_DAMAGE, "to", T_OBJECTS, "and", "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "deals", T_NUMBER, T_DAMAGE, "to", T_OBJECTS, "and", T_NUMBER, T_DAMAGE, "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, W_LOSE, T_NUMBER, "life"], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, W_LOSE, "half", "his", "or", "her", "life", "COMMA", T_ROUNDED], None, Object(0)) # havoc
AddRule(T_ACTION_INTERNAL, [T_OBJECT, W_LOSE, T_NUMBER, "life", "COMMA", W_DISCARD, T_NUMBER, W_CARD], None, Object(0)) # undercity plague
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "lose", "life", T_EQUAL_TO], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECT, "loses", "life", T_EQUAL_TO], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, T_MOVE_ACTION], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, T_MOVE_ACTION, "and", W_LOSE, T_NUMBER, 'life'], None, Object(0)) # toil / trouble
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "choose", T_ABILITIES], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "choose", T_OBJECTS, T_COLOR_OR_TYPE_TERM], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "choose", T_OBJECTS, T_MOVE_FROM_OPT], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "chooses", T_OBJECTS, T_MOVE_FROM_OPT], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "choose", T_NUMBER, "color"], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "choose", T_NUMBER, "colors"], None, Object(0)) # TODO
# TODO: double check this rule with Soul Ransom
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_DISCARD, T_WHOSE, "hand"], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["populate"], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["counter", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, T_TAKE_CONTROL, "of", T_OBJECTS, T_UNTIL_OPT], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["exchange", "control", "of", T_OBJECTS, "and", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_ACTION_INTERNAL, ["move", T_COUNTERS, "from", T_OBJECTS, "onto", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_GAIN, T_NUMBER, "life", T_FOR_EACH_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_GAIN, "life", T_EQUAL_TO], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_PREVENT_DMG_ACTION], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_DMG_WHICH, "is", "dealt", "to", T_OBJECTS, 'instead'], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "separate", T_OBJECTS, "into", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "separates", T_OBJECTS, "into", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_ADD, T_MANA, "to", T_WHOSE, "mana", "pool", T_FOR_EACH_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_ADD, T_MANA, "to", T_WHOSE, "mana", "pool", T_EQUAL_TO], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_ADD, T_MANA, "to", T_WHOSE, "mana", "pool", "of", "any", "type", "that", "land", "produced", T_FOR_EACH_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_ADD, "to", T_WHOSE, "mana", "pool", T_MANA, T_EQUAL_TO], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "gain", "life", T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_DAMAGE, "can't", "be", "prevented", T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", W_CAST, T_OBJECTS, T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "be", "regenerated", T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "be", "countered", T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "be", "countered", "by", T_OBJECTS, T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["you", "win", "the", "game"], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "loses", "the", "game"], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_DONT, "untap", "during", T_WHOSE, "untap", "step"], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_DONT, "untap", "during", T_WHOSE, "untap", "steps"], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_DONT, "untap", "during", T_WHOSE, "next", "untap", "step"], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["look", "at", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_REVEAL, T_WHOSE, "hand"], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_REVEAL, T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_REVEAL, T_OBJECTS, "from", T_PART_OF_FIELD], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_REVEAL, T_OBJECTS, "COMMA", "may", T_MOVE_ACTION], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_REVEAL, T_OBJECTS, "COMMA", "loses", "life", T_EQUAL_TO], None, Object(0)); # duskmantle seer
AddRule(T_ACTION_INTERNAL, [T_ACTIVATION_RESTRICTION], Ident)
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_CONTROL, T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "reveals", W_CARD, "from", T_PART_OF_FIELD, "until", T_OBJECTS, "reveals", T_OBJECTS, "COMMA", "then", "puts", "those", W_CARD, "into", T_PART_OF_FIELD, T_ENTER_THE_BATTLEFIELD_MOD_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "reveals", W_CARD, "from", T_PART_OF_FIELD, "until", T_OBJECTS, "reveals", T_OBJECTS, "COMMA", "then", "puts", "all", T_OBJECTS, "into", T_PART_OF_FIELD, T_ENTER_THE_BATTLEFIELD_MOD_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["x", "can't", "be", T_NUMBER], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_WHOSE, T_PT_EQUAL_TO], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_WHOSE, "life", "total", "becomes", T_NUMBER], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "skips", "that", "draw"], None, Object(0)) # notion thief

# TODO: move all 'becomes' rules to T_GET_EFFECT
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "becomes", "a", T_PLUS_X_PLUS_X, T_OBJECTS, "with", "all", "creature", "types", T_UNTIL_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "becomes", "a", T_PLUS_X_PLUS_X, T_OBJECTS, "that's", "no", "longer", T_OBJECTS, T_UNTIL_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "becomes", "a", "copy", "of", T_OBJECTS, "and", T_GET_EFFECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "become", "a", "copy", "of", T_OBJECTS, "and", T_GET_EFFECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "become", T_PLUS_X_PLUS_X, T_UNTIL_OPT], None, Object(0));
#AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "becomes", "a", T_PLUS_X_PLUS_X, T_OBJECTS, T_UNTIL_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "becomes", T_NUMBER, T_OBJECTS, "with", T_PT_EQUAL_TO, T_UNTIL_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["it", "is", "still", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["he", "is", "still", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["they're", "still", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_SEARCH_ACTION], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, W_SHUFFLE, T_WHOSE, "library"], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "have", "no", "maximum", "hand", "size", T_UNTIL], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "may", W_CAST, T_OBJECTS, T_MOVE_FROM_OPT, "without", "paying", T_WHOSE, "mana", W_COST], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["there", "is", "an", "additional", T_PHASE_OR_STEP], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["as", "an", "additional", "cost", "to", W_CAST, T_OBJECTS, "COMMA", T_ACTIONS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "fights", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "fight", "each", "other"], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["have", T_OBJECTS, "become", "a", "copy", "of", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["have", T_OBJECTS, "enter", "the", "battlefield", "as", "a", "copy", "of", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_WHOSE, "name", "is", "still", T_NAME], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_WHOSE, "activated", "abilities", "can't", "be", "activated"], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["activated", "abilities", "of", T_OBJECTS, "can't", "be", "activated"], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, T_ENTERS_THE_BF, T_ENTER_THE_BATTLEFIELD_MOD], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can", "be", "the", "target", "of", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "be", "the", "target", "of", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can't", "be", "the", "targets", "of", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "can", "be", "cast"], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["name", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["copy", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["copy", T_OBJECTS, T_NUMBER, "times"], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "copies", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["choose", "new", "targets", "for", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["pay", T_NUMBER, "life"], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["repeat", "this", "process", "for", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS_OPT, "do", "the", "same", "COMMA", "with", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["flip", "a", "coin"], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["flip", T_NUMBER, "coins"], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["take", "an", "extra", "turn", "after", "this", "one", T_FOR_EACH_OPT], None, Object(0)) # Search the City
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "able", "to", T_ATTACK_BLOCK_BE_BLOCKED, T_OBJECTS, "do", "so"], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "able", "to", T_ATTACK_BLOCK_BE_BLOCKED, T_OBJECTS, "do", "so", T_UNTIL], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_COST, T_MANA, "less", "to", "cast", T_FOR_EACH_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_COST, T_MANA, "less", "to", "activate", T_FOR_EACH_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, W_COST, T_MANA, "less", "for", "you", "to", "cast", T_FOR_EACH_OPT], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["attach", T_OBJECTS, "to", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_INTERNAL, ["switch", T_WHOSE, "power", "and", "toughness", T_UNTIL_OPT], None, Object(0))
# TODO: you may is a qualifier, might as well remove it next three
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "may", "play", T_OBJECTS, T_UNTIL_OPT], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "may", "cast", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "may", "pay", T_COST], None, Object(0));
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "may", "spend", "mana", "as", "though", "it", "were", "mana", "of", "any", "color", "to", "cast", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["a", "deck", "can", "have", T_OBJECTS], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["x", W_IS, T_WHERE_X_INTERNAL], None, Object(0));
AddRule(T_ACTION_INTERNAL, ["the", "scavenge", "cost", "is", T_EQUAL_TO], None, Object(0)); # varolz
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "assigns", T_NUMBER, T_DAMAGE, "this", "combat"], None, Object(0)); # master of cruelties
AddRule(T_ACTION_INTERNAL, [T_OBJECTS, "turns", "face", "up", T_OBJECTS], None, Object(0)); # Pyxis of Pandemonium

AddRule(T_ACTION_QUALIFIER_AFTER, ["COMMA", T_WHERE_X], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", "you", "pay", T_COST], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", T_OBJECTS, W_CONTROL, T_OBJECTS], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["if", T_OBJECTS, W_CONTROL, T_OBJECTS], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["if", T_OBJECTS, W_IS, T_OBJECTS], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", T_OBJECTS, "pays", T_COST], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", T_OBJECTS, "pays", T_COST, T_FOR_EACH], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", T_OBJECTS, "lost", "life", T_UNTIL], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, [T_AT], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["instead", T_CONDITION], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["instead", "of", "putting", T_OBJECTS, T_MOVE_TO], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["as", "though", T_OBJECTS, "had", T_ABILITIES], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["as", "though", T_OBJECTS, "didn't", "have", T_ABILITIES], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["as", "long", "as", T_OBJECTS, "control", T_OBJECTS], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["as", "long", "as", T_OBJECTS, W_HAVE, T_COUNTERS_ON], None, Object(0))
AddRule(T_ACTION_QUALIFIER_AFTER, ["unless", "they're", "mana", "abilities"], None, Object(0)) # Putching Needle
AddRule(T_ACTION_QUALIFIER_AFTER, ["for", "as", "long", "as", "you", "control", T_OBJECTS], None, Object(0)) # Tidebinder Mage
AddRule(T_ACTION_QUALIFIER_AFTER, ["for", "as", "long", "as", T_OBJECTS, "remains", "exiled"], None, Object(0)) # Psychic Intrusion
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_FOR_EACH, "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_OBJECTS, "may"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_OBJECTS, "may", "have"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_CONDITION, "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_CONDITION, "COMMA", "or", T_CONDITION, "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, ["otherwise", "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, [T_UNTIL, "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, ["after", T_PHASE_OR_STEP, "COMMA"], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIER_BEFORE, ["instead"], None, Object(0))

AddRule(T_ACTION_QUALIFIERS_AFTER, ["instead"], None, Object(0))
AddRule(T_ACTION_QUALIFIERS_AFTER, [T_ACTION_QUALIFIER_AFTER], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIERS_AFTER, [T_ACTION_QUALIFIER_AFTER, T_ACTION_QUALIFIERS_AFTER], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIERS_BEFORE, [T_ACTION_QUALIFIER_BEFORE], None, Object(0)) # TODO
AddRule(T_ACTION_QUALIFIERS_BEFORE, [T_ACTION_QUALIFIER_BEFORE, T_ACTION_QUALIFIERS_BEFORE], None, Object(0)) # TODO

AddRule(T_ACTION, [T_ACTION_INTERNAL], None, Object(0))
AddRule(T_ACTION, [T_ACTION_INTERNAL, T_ACTION_QUALIFIERS_AFTER], None, Object(0))
AddRule(T_ACTION, [T_ACTION_QUALIFIERS_BEFORE, T_ACTION_INTERNAL], None, Object(0))
AddRule(T_ACTION, [T_ACTION_QUALIFIERS_BEFORE, T_ACTION_INTERNAL, T_ACTION_QUALIFIERS_AFTER], None, Object(0))

AddRule(T_ACTIONS, [T_ACTION], Ident)
AddRule(T_ACTIONS, [T_ACTION, "and", T_ACTIONS], None, Object(0))
AddRule(T_ACTIONS, [T_ACTION, "COMMA", "and", T_ACTIONS], None, Object(0))
AddRule(T_ACTIONS, [T_ACTION, "unless", "you", T_ACTION], None, Object(0)) # TODO
AddRule(T_ACTIONS, [T_ACTION, "except", T_ACTION], None, Object(0)) # TODO
AddRule(T_ACTIONS, [T_ACTION, "except", T_ACTION, "COMMA", T_ACTION], None, Object(0)) # TODO
AddRule(T_ACTIONS, [T_ACTION, "except", T_ACTION, "COMMA", T_ACTION, "COMMA", "and", T_ACTION], None, Object(0)) # TODO
#charm
AddRule(T_ACTIONS_TO_CHOOSE, [T_ACTIONS], None, Object(0))
AddRule(T_ACTIONS_TO_CHOOSE, [T_ACTIONS, "SEMICOLON", T_AND_OR, T_ACTIONS_TO_CHOOSE], None, Object(0))
AddRule(T_ACTIONS_TO_CHOOSE, [T_ACTIONS, "SEMICOLON", T_ACTIONS_TO_CHOOSE], None, Object(0))
AddRule(T_ACTIONS, ["choose", "one", "DASH", T_ACTIONS_TO_CHOOSE], None, Object(0))
AddRule(T_ACTIONS, ["choose", "one", "or", "more", "DASH", T_ACTIONS_TO_CHOOSE], None, Object(0))
AddRule(T_ACTIONS, ["choose", "one", "COLON", T_ACTIONS_TO_CHOOSE], None, Object(0))

AddRule(T_PHASE_OR_STEP, ["this", "phase"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["end", "step"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["precombat", "main", "phase"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["combat", "phase"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["main", "phase"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["end", "of", "combat"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["upkeep"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["untap", "step"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["draw", "step"], None, Object(0))
AddRule(T_PHASE_OR_STEP, ["turn"], None, Object(0))

AddRule(T_AT, ['at', 'the', 'beginning', 'of', 'each', 'combat'], None, Object(TBeginningOfEachCombat))
AddRule(T_AT, ['at', 'the', 'beginning', 'of', 'the', "next", 'combat'], None, Object(0))
AddRule(T_AT, ['at', 'the', 'beginning', 'of', "each", T_PHASE_OR_STEP], None, Object(0)) # TODO generalize this
AddRule(T_AT, ['at', 'the', 'beginning', 'of', T_WHOSE, T_PHASE_OR_STEP], None, Object(0)) # TODO generalize this
AddRule(T_AT, ['at', 'the', 'beginning', 'of', T_WHOSE, T_PHASE_OR_STEP, "of", T_OBJECTS], None, Object(0)) # TODO generalize this
AddRule(T_AT, ['at', 'the', 'beginning', 'of', T_WHOSE, 'next', T_PHASE_OR_STEP], None, Object(0)) # TODO generalize this
AddRule(T_AT, ['at', 'this', "turn's", "next", T_PHASE_OR_STEP], None, Object(0)) # TODO generalize this
AddRule(T_AT, ['during', T_WHOSE, T_PHASE_OR_STEP], None, Object(0)) # TODO generalize this

AddRule(T_CONDITION, ["whenever", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["whenever", T_OBJECTS, T_OBJECT_DOES, T_AND_OR, T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["whenever", T_OBJECTS, T_OBJECT_DOES, T_UNTIL], None, Object(0)) # TODO
AddRule(T_CONDITION, ["whenever", T_COUNTERS, W_IS, "placed", "on", "THIS"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['whenever', "an", "ability", "of", T_OBJECTS, "is", "activated"], None, Object(0))
AddRule(T_CONDITION, ["when", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["when", T_OBJECTS, T_OBJECT_DOES, T_AND_OR, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["as", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ["if", T_OBJECTS, T_OBJECT_DOES], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "control", T_OBJECTS], None, Object(0)) # TODO generalize this
AddRule(T_CONDITION, ['if', T_OBJECTS, "do"], None, Object(0)) # TODO generalize this
AddRule(T_CONDITION, ['if', T_OBJECTS, W_DONT], None, Object(0)) # TODO generalize this
AddRule(T_CONDITION, ['if', T_OBJECTS, "does"], None, Object(0)) # TODO generalize this
AddRule(T_CONDITION, ['if', T_OBJECTS, W_REVEAL, T_OBJECTS], None, Object(0)) # Signal the clans
AddRule(T_CONDITION, ['if', T_OBJECTS, "would", "die", T_UNTIL], None, Object(0)) # TODO generalize this
AddRule(T_CONDITION, ['if', T_OBJECTS, "are", "put", T_MOVE_TO, "this", "way"], None, Object(0)) # guild feud
AddRule(T_CONDITION, ['if', T_OBJECTS, "would", "be", "put", T_MOVE_TO], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "would", "be", "put", T_MOVE_TO, "from", T_PART_OF_FIELD], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "would", "be", "put", T_MOVE_TO, "this", "turn"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "has", T_NUMBER, W_CARD, "in", "hand"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "gained", T_NUMBER, "life", "this", "turn"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "win", "the", "flip"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "lose", "the", "flip"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "causes", "you", "to", T_ACTIONS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, W_IS, "countered", "this", "way"], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, W_IS, T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "isn't", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "was", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, "is", "attached", "to", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_OBJECTS, W_HAVE, T_ABILITIES], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', T_NUMBER, T_COUNTERS, "would", "be", "placed", "on", T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ['if', "it", "isn't", "a", "mana", "ability"], None, Object(0)) # TODO
AddRule(T_CONDITION, ["if", "there", "are", T_NUMBER, T_OBJECTS], None, Object(0)) # TODO
AddRule(T_CONDITION, ["if", T_WHOSE, "power", "is", T_NUMBER], None, Object(0)) # TODO
AddRule(T_CONDITION, ["if", T_WHOSE, "toughness", "is", T_NUMBER], None, Object(0)) # TODO
AddRule(T_CONDITION, ["as", "long", "as", "it", "is", "not", T_WHOSE, "turn"], None, Object(0)) # TODO
AddRule(T_CONDITION, ["as", "long", "as", T_OBJECTS, W_IS, "monstrous"], None, Object(0))
AddRule(T_CONDITION, ["if", T_OBJECTS, W_IS, "monstrous"], None, Object(0))
AddRule(T_CONDITION, ["if", T_OBJECTS, W_IS, "in", T_PART_OF_FIELD], None, Object(0))
AddRule(T_CONDITION, ["as", "long", "as", T_OBJECTS, "control", T_OBJECTS], None, Object(0))
AddRule(T_CONDITION, ["as", "long", "as", T_OBJECTS, T_OBJECT_DOES], None, Object(0))
AddRule(T_CONDITION, ["as", "long", "as", T_OBJECTS, T_OBJECT_DOES, T_AND_OR, T_OBJECTS, T_OBJECT_DOES], None, Object(0))
AddRule(T_CONDITION, ["as", "long", "as", T_WHERE_X_INTERNAL, "is", T_GREATER_LESS, T_WHERE_X_INTERNAL], None, Object(0))
AddRule(T_CONDITION, [T_AT], Ident) # TODO generalize this

AddRule(T_STATEMENT, [T_ACTIONS], None, Object(0))
AddRule(T_STATEMENT, [T_COST, "COLON", T_ACTIONS], None, Object(0))
AddRule(T_STATEMENT, [T_ABILITIES], None, Object(0))
AddRule(T_STATEMENT, [T_COST, "COLON", T_ABILITIES], None, Object(0))
AddRule(T_STATEMENT, ["enchant", T_OBJECT], None, Object(0))
AddRule(T_STATEMENT, ["equip", T_COST], None, Object(0)) # TODO

AddRule(T_STATEMENT, [T_BATTALION, T_ACTIONS], None, Object(0))
AddRule(T_STATEMENT, [T_BLOODRUSH, T_STATEMENT], IdentSkip1)
AddRule(T_STATEMENT, [T_HEROIC, T_STATEMENT], IdentSkip1)
AddRule(T_STATEMENT, ["overload", T_COST], None, Object(0))
AddRule(T_STATEMENT, ["fuse"], None, Object(0))
AddRule(T_STATEMENT, ["//"], None, Object(0))

AddRule(T_STATEMENTS, [T_END_OF_STATEMENT], Ident)
AddRule(T_STATEMENTS, [T_END_OF_STATEMENT, T_STATEMENTS], IdentSkip1)
AddRule(T_STATEMENTS, [T_STATEMENT, T_END_OF_STATEMENT], IdentSkip2nd)
AddRule(T_STATEMENTS, [T_STATEMENT, T_END_OF_STATEMENT, T_STATEMENTS], MergeStatementsSkip1)
AddRule(T_STATEMENTS, [T_STATEMENT, "COMMA", "then", T_STATEMENTS], MergeStatementsSkip2)
AddRule(T_STATEMENTS, [T_STATEMENT, T_END_OF_STATEMENT, "then", T_STATEMENTS], MergeStatementsSkip2)

AddRule(T_PLANESWALKER_STATEMENT, [T_LOYALTY_COST, "COLON", T_STATEMENTS], None, Object(0))
AddRule(T_PLANESWALKER_STATEMENTS, [T_PLANESWALKER_STATEMENT], Ident)
AddRule(T_PLANESWALKER_STATEMENTS, [T_PLANESWALKER_STATEMENT, T_PLANESWALKER_STATEMENTS], None, Object(0))

AddRule(T_CARD, [T_STATEMENTS], Ident)
AddRule(T_CARD, [T_PLANESWALKER_STATEMENTS], Ident)

