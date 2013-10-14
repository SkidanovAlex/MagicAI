#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file contains an algorithm that, given card text and set of rules,
#   produces a parse tree. Rules should be crafted in such a way that every
#   card has at most one parse tree.
# It also contains routines to build Statement objects out of parse trees
#   (which is just traversing the tree and calling the function embedded)
#

# MTG uses very simple english. I highly suspect that one can use
#    bison to parse it, but to be safe I use some kind of CFG here
#
import rules

debug = False
limitsMax = {}
limitsMin = {}

# mins could be innacurate, but never larger than the actual min
def ComputeLimitsForResult(stack, result):
    if result in stack:
        limitsMax[result] = 2000000
        limitsMin[result] = 0
    if result in limitsMax:
        return

    stack[result] = True
    limitsMax[result] = 0
    limitsMin[result] = 2000000

    for rule in rules.rules[result]:
        curMax = 0
        curMin = 0
        for token in rule.body:
            if isinstance(token, basestring) or token == rules.T_LOYALTY_COST or token == rules.T_PLUS_X_PLUS_X or token == rules.T_PIC_COST:
                curMax += 1
                curMin += 1
            else:
                ComputeLimitsForResult(stack, token)
                curMax += limitsMax[token]
                curMin += limitsMin[token]
        limitsMax[result] = max(limitsMax[result], curMax)
        limitsMin[result] = min(limitsMin[result], curMin)
        rule.maxL = curMax
        rule.minL = curMin

    del stack[result]

def ComputeLimits():
    stack = {}
    for result in rules.rules.keys():
        ComputeLimitsForResult(stack, result)

# it should match all +a/+a, -a/-a, -a/+a, and also just a/a
def IsPlusXPlusX(word):
    # should be good enough
    return "/" in word

def IsLoyaltyCost(word):
    return "0" == word or word[0] == '+' or word[0] == '-'

def IsPicCost(word):
    return word.startswith("[") and word.endswith("]")

# computes if text[l:r] can be represented as `result`
# if yes, dp[l][r][result] will contain backlinks to restore the tree
def DP(dp, text, l, r, result, depth=0):
    if result in dp[l][r]:
        if dp[l][r][result] != False:
            return True
        else:
            return False

    if isinstance(result, basestring):
        if r == l + 1 and text[l] == result:
            return True
        return False

    if result == rules.T_PLUS_X_PLUS_X:
        # +x/+x is a special case
        return r == l + 1 and IsPlusXPlusX(text[l])

    if result == rules.T_LOYALTY_COST:
        # +x/+x is a special case
        return r == l + 1 and IsLoyaltyCost(text[l])

    if result == rules.T_PIC_COST:
        # +x/+x is a special case
        return r == l + 1 and IsPicCost(text[l])

    if r - l > limitsMax[result]:
        return False

    if r - l < limitsMin[result]:
        return False

    ways = 0
    for rule in rules.rules[result]:
        if (len(rule.body) == 0):
            if r == l:
                ways += 1
                dp[l][r][result] = { 'rule': rule , 'split': [] }
            continue
        elif r == l:
            continue

        if r - l > rule.maxL: continue
        if r - l < rule.minL: continue
        ok = True
        for state in rule.body:
            if isinstance(state, basestring) and state not in text[l:r]:
                ok = False
                break
        if not ok: continue
        idp = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp_back = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp[0][0] = 1
        maxWid = 0
        for wid in range(r - l + 1):
            for rid, state in enumerate(rule.body):
                if idp[wid][rid] > 0:
                    for nwid in range(wid, r - l + 1):
                        if rid == len(rule.body) - 1 and nwid != r - l:
                            continue
                        if rid < len(rule.body) - 1 and nwid != r - l and isinstance(rule.body[rid + 1], basestring) and text[l + nwid] != rule.body[rid + 1]:
                            continue
                        try:
                            if DP(dp, text, l + wid, l + nwid, state, depth+1):
                                idp[nwid][rid + 1] += idp[wid][rid]
                                idp_back[nwid][rid + 1] = wid
                        except:
                            print l + wid, l + nwid, state
                            raise
        wid = r - l
        rid = len(rule.body)
        if idp[wid][rid]:
            ways += idp[wid][rid]
            desc = [0 for x in range(len(rule.body))]
            while rid != 0:
                assert idp[wid][rid] > 0
                desc[rid - 1] = l + idp_back[wid][rid]
                wid = idp_back[wid][rid]
                rid -= 1
            assert wid == 0
            desc.append(r)
            dp[l][r][result] = { 'rule': rule , 'split': desc }
    if ways > 1:
        print ' '.join(text)
        print "WARNING: [%d:%d, %d] -- %d ways to achieve" % (l, r, result, ways)
        assert False
    elif ways == 1:
        if debug:
            print "YAY: [%d:%d, %d]" % (l, r, result)
        return True
    dp[l][r][result] = False
    return False

def RestoreDP(dp, l, r, result):
    if rules.IsTerminal(result):
        return { 'terminal': 1, 'state': result }
    
    assert result in dp[l][r], "%d:%d, %s" % (l, r, result)
    ret = []
    data = dp[l][r][result]
    assert len(data['rule'].body) + 1 == len(data['split']) or (len(data['rule'].body) == 0 and len(data['split']) == 0)
    for id, state in enumerate(data['rule'].body):
        ret.append(RestoreDP(dp, data['split'][id], data['split'][id + 1], state))
    return { 'terminal': 0, 'children': ret, 'rule': data['rule'] }

def Tokenize(text, name):
    text = text.replace("—", '-')
    text = text.replace("\x92", '\'')
    text = text.replace("\x93", '"')
    text = text.replace("\x94", '"')
    text = text.replace("\xe2\x80\x99", '\'')
    text = text.replace("\xe2\x80\x9c", '"')
    text = text.replace("\xe2\x80\x9d", '"')
    if '//' in name:
        print name
        pos = name.find('//')
        text = text.lower()
        if name[:pos].lower().strip() != 'turn': # HACK: turn//burn has "until end of turn" in its description
            text = text.replace(name[:pos].lower().strip(), "THIS")
        text = text.replace(name[pos + 2:].lower().strip(), "THIS")
    else:
        text = text.lower().replace(name.lower(), "THIS")
    if ',' in name:
        text = text.replace(name.lower()[:name.find(',')], "THIS")
    text = text.replace("it's", "it is").replace("he's", "he is")
    text = text.replace(".", " DOT ").replace("<br />", " DOT ").replace(",", " COMMA ").replace(" - ", " DASH ").replace(":", " COLON ").replace(";", " SEMICOLON ").replace("\"", " DQ ")
    # I screw the encoding somewhere...
    while True:
        p1, p2 = text.find('('), -1
        if p1 != -1:
            p2 = text.find(')', p1)
        q1, q2 = text.find('<'), -1
        if q1 != -1:
            q2 = text.find('>', q1)
        if p2 != -1:
            text = text[:p1] + text[p2 + 1:]
        elif q2 != -1:
            text = text[:q1] + text[q2 + 1:]
        else: break
    tokens = text.split()
    if len(tokens) == 0 or tokens[-1] != "DOT":
        tokens.append("DOT");
    if debug:
        print tokens
        print list(enumerate(tokens))
    return tokens

def ParseCard(text, name):
    dp = []
    tokens = Tokenize(text, name)
    for i in range(len(tokens) + 1):
        dp.append([])
        for j in range(len(tokens) + 1):
            dp[i].append({})
    success = DP(dp, tokens, 0, len(tokens), rules.T_CARD)
    if not success:
        return None
    tree = RestoreDP(dp, 0, len(tokens), rules.T_CARD)
    return tree

# This is for debugging only
def PrettyPrintTree(tree, ident = ""):
    if tree['terminal']:
        print "%s%s" % (ident, tree['state'])
    else:
        if len(tree['children']) == 1:
            PrettyPrintTree(tree['children'][0], ident)
        else:
            print "%s{" % ident
            for elem in tree['children']:
                PrettyPrintTree(elem, ident + " ")
            print "%s}" % ident

if __name__ == "__main__":
    debug = True
    ComputeLimits()
    tree = ParseCard("When Trostani's Summoner enters the battlefield, put a 2/2 white Knight creature token with vigilance, a 3/3 green Centaur creature token, and a 4/4 green Rhino creature token with trample onto the battlefield.", "Trostani's Summoner")

    PrettyPrintTree(tree)

