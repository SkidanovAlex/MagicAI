# MTG uses very simple english. I highly suspect that one can use
#    bison to parse it, but to be safe I use some kind of CFG here
#
import parser_rules as rules

def IsPlusXPlusX(word):
    # should be good enough
    return "+" in word and "/" in word

# computes if text[l:r] can be represented as `result`
# if yes, dp[l][r][result] will contain backlinks to restore the tree
def DP(dp, text, l, r, result):
    if result in dp[l][r]:
        return True

    if isinstance(result, basestring):
        if r == l + 1 and text[l] == result:
            return True
        return False

    if result == rules.T_PLUS_X_PLUS_X:
        # +x/+x is a special case
        return r == l + 1 and IsPlusXPlusX(text[l])

    ways = 0
    for rule in rules.rules[result]:
        idp = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp_back = [[0 for i in range(len(rule.body) + 1)] for j in range(r - l + 1)]
        idp[0][0] = 1
        for wid in range(r - l):
            for rid, state in enumerate(rule.body):
                if idp[wid][rid] > 0:
                    for nwid in range(wid + 1, r - l + 1):
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
        print "WARNING: [%d:%d, %d] -- %d ways to achieve" % (l, r, result, ways)
        assert False
    elif ways == 1:
        print "YAY! [%d:%d, %d]" % (l, r, result);
        return True
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

def ParseCard(text):
    dp = []
    for i in range(len(text)):
        dp.append([])
        for j in range(len(text)):
            dp[i].append({})
    text = text.lower().replace(".", " DOT ").split()
    success = DP(dp, text, 0, len(text), rules.T_CARD)
    if not success:
        return None
    tree = RestoreDP(dp, 0, len(text), rules.T_CARD)
    return tree

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
    tree = ParseCard("Target creature gets +1/+1 and gains flying and first strike until end of turn.");
    PrettyPrintTree(tree)
