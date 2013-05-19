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

# it should match all +a/+a, -a/-a, -a/+a, and also just a/a
def IsPlusXPlusX(word):
    # should be good enough
    return "/" in word

def IsPicCost(word):
    return word.startswith("[") and word.endswith("]")

# computes if text[l:r] can be represented as `result`
# if yes, dp[l][r][result] will contain backlinks to restore the tree
def DP(dp, text, l, r, result):
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

    if result == rules.T_PIC_COST:
        # +x/+x is a special case
        return r == l + 1 and IsPicCost(text[l])

    ways = 0
    for rule in rules.rules[result]:
        idp = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp_back = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp[0][0] = 1
        for wid in range(r - l):
            for rid, state in enumerate(rule.body):
                if idp[wid][rid] > 0:
                    for nwid in range(wid + 1, r - l + 1):
                        if rid == len(rule.body) and nwid != r - l:
                            continue
                        if DP(dp, text, l + wid, l + nwid, state):
                            idp[nwid][rid + 1] += idp[wid][rid]
                            idp_back[nwid][rid + 1] = wid
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
    assert len(data['rule'].body) + 1 == len(data['split'])
    for id, state in enumerate(data['rule'].body):
        ret.append(RestoreDP(dp, data['split'][id], data['split'][id + 1], state))
    return { 'terminal': 0, 'children': ret, 'rule': data['rule'] }

def Tokenize(text, name):
    text = text.replace("—", '-')
    text = text.lower().replace(name.lower(), "THIS").replace(".", " DOT ").replace("<br />", " DOT ").replace(",", " COMMA ").replace(" - ", " DASH ").replace(":", " COLON ").replace("\"", " DQ ")
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

def ParseTreeToStatement(tree):
    if tree['terminal']:
        return tree['state']
    children = []
    for elem in tree['children']:
        children.append(ParseTreeToStatement(elem))
    return tree['rule'].apply(children)

if __name__ == "__main__":
    debug = True
    tree = ParseCard("Counter target spell. Its controller puts the top two cards of his or her library into his or her graveyard.", "Mindeye Drake");
    PrettyPrintTree(tree)
