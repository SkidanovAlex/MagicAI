#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file contains a simple HTML parser for mtgsalvation.com spoilers.
# For each card it extracts its name, card text, CMC etc, and then passes it
#    further to the card text parser and code generator
#

import urllib2
import re

from parser import ParseCard, ParseTreeToStatement, ComputeLimits

PARSE_NEW = 1
PARSE_ALL = 2
REPORT = 3

# if pos is not given, returns a string
# if pos is given, returns (string, newPos)
def parseBetween(s, op, cl, pos = -1):
    opPos = s.find(op, pos + 1)
    if opPos == -1: return None
    clPos = s.find(cl, opPos + 1)
    if clPos == -1: return None
    ret = s[opPos + len(op):clPos]
    if pos != -1: return (ret, opPos)
    else: return ret

def stripTags(value):
    """Returns the given HTML with all tags stripped."""
    return re.sub(r'<[^>]*?>', '', value)

# fixes some mispellings in spoiler texts
def randomFixes(text):
    text = text.replace("Ordruum", "Ordruun")
    text = text.replace("until end a turn", "until end of turn");
    text = text.replace("it's controller", "its controller");
    text = text.replace("it's owner", "its owner");
    text = text.replace("except it's name is", "except its name is");
    text = text.replace("addition to it's other types", "addition to its other types");
    text = text.replace(", deal 1 damage", ", Bomber Corps deals 1 damage");
    text = text.replace("manapool", "mana pool");
    text = text.replace("its or her library", "his or her library");
    text = text.replace("end of turn; permanents", "end of turn; or permanents");
    text = text.replace("gets lifelink", "gains lifelink");
    text = text.replace("cretaures", "creatures");
    text = text.replace("Squad attacks you", "Squad attacks, you");
    text = text.replace("your opponent controls", "your opponents control");
    text = text.replace("2/2 Knight", "2/2 white Knight");
    text = text.replace("unless it's controller", "unless its controller");
    text = text.replace("during the untap step", "during its controller's untap step");
    text = text.replace("its controller pay ", "its controller pays ");
    text = text.replace("Whenever enchanted land become tapped", "Whenever enchanted land becomes tapped");
    text = text.replace("reveals the top card of his or her library until", "reveals cards from the top of his or her library until");
    text = text.replace("0: Until end of turn, Gideon becomes", "0: Until end of turn, Gideon, Champion of Justice  becomes");
    text = text.replace("becomes a 2/2  blue and black Horror until end", "becomes a 2/2 blue and black Horror artifact creature until end");
    text = text.replace("token onto the battlefield that is a copy", "token onto the battlefield that's a copy");
    text = text.replace("spell’s", "spell's");
    text = text.replace("Borborygmous", "Borborygmos");
    text = text.replace("exile Obzedat. If", "exile Obzedat, Ghost Council. If")
    text = text.replace("At the beginning of your end step you may", "At the beginning of your end step, you may ")
    text = text.replace("libary", "library")
    text = text.replace("without paying it's mana cost", "without paying its mana cost")
    return text

def removeImages(text):
    text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/tap.gif" alt="{T}" />', '[TAP]')
    for mana1 in "brguwx":
        MANA1 = mana1.upper()
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s.gif" alt="{%s}" />' % (mana1, MANA1), ' [%s] ' % MANA1)
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s.gif" alt="%s" class="inlineimg" style="border: none;" />' % (mana1, mana1), ' [%s] ' % MANA1)
        for mana2 in "brguw":
            MANA2 = mana2.upper()
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="{%s%s}" />' % (MANA1, MANA2, MANA1, MANA2), ' [%s%s] ' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="{%s%s}" />' % (mana1, mana2, mana1, mana2), ' [%s%s] ' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="%s%s" class="inlineimg" style="border: none;" />' % (mana1, mana2, mana1, mana2), ' [%s%s] ' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="%s%s" class="inlineimg" style="border: none;" />' % (mana1, mana2, mana2, mana1), ' [%s%s] ' % (MANA1, MANA2))
    for i in range(100):
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%d.gif" alt="%d" class="inlineimg" style="border: none;" />' % (i, i), ' [%d] ' % i)
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%d.gif" alt="%d" />' % (i, i), ' [%d] ' % i)
    return text

def doit(fname, setName, mode):
    website = open('spoilers/' + fname + '.txt', 'r').read()
    known = set()
    try:
        known = set([x.strip() for x in open('parsed/' + fname + '.list', 'r').readlines()])
    except IOError as e:
        print "Failed to open known cards file. Assuming nothing is known."
        pass
    new = []
    website = randomFixes(website)
    lastPos = 0
    count = 0

    report = {}

    while True:
        res = parseBetween(website, '<table border="0" cellspacing="0" cellpadding="5" width="290" align="center" style="border: 1px solid black;background-color:white;color: black;">', '</table>', lastPos + 1);
        if res == None: break
        content, lastPos = res
        name = stripTags(parseBetween(content, '<h3 style="margin: 0;">', '</h3>')).strip()
        if name[0] == '*': name = name[1:]
        cost, nextPos = parseBetween(content, '<td align="right" width="80px">', '</td>', 0)
        cost = removeImages(cost).strip()
        typeStr, nextPos = parseBetween(content, '<td width="220px">', '</td>', nextPos)
        typeArr1 = typeStr.split('-')
        types = typeArr1[0].strip().split()
        subtypes = []
        if len(typeArr1) > 1:
            assert len(typeArr1) == 2, str(typeArr1)
            subtypes = typeArr1[1].split()
        cardText, nextPos = parseBetween(content, '<td colspan="2">', '</td>', nextPos)
        cardText = removeImages(cardText)
        pwr, tgh = -1, -1
        if "Creature" in types:
            pt, nextPos = parseBetween(content, '<td align="right">', '</td>', nextPos)
            assert '/' in pt, pt
            pwr, tgh = pt.split('/')
        if "Basic" in types and "Land" in types:
            continue
        """
        print "NAME: '%s', COST: '%s' TYPE: '%s', SUBTYPES: '%s'\n%s" % (name, cost, ':'.join(types), ':'.join(subtypes), cardText)
        if 'Creature' in types:
            print "%s/%s" % (pwr, tgh);
        print "\n"
        """
        ok = False
        if mode == PARSE_ALL or (mode == PARSE_NEW and name not in known):
            tree = ParseCard(cardText, name)
            if tree != None:
                ok = True
                ParseTreeToStatement(tree)
                new.append(name)
        elif name in known:
            ok = True

        colorSet = set()
        colors = []
        clr = ''
        inside = False
        for color in cost:
            clr += color
            if color == '[':
                inside = True
            elif color == ']':
                inside = False
            if not inside:
                if not clr[1:-1].isdigit() and clr[1:-1] != 'X':
                    clr = clr.strip()
                    if clr not in colorSet:
                        colors.append(clr)
                        colorSet.add(clr)
                clr = ''
        colors = ''.join(colors)

        if ok or name in known:
            print "[%s] %s: OK%s" % (colors, name, " (new)" if name not in known else " (gone)" if not ok else "")
            if colors not in report:
                report[colors] = 1
            else:
                report[colors] += 1
        else:
            print "[%s] %s: FAIL" % (colors, name)

        count += 1
    print "[%s] Total cards: %d. Known: %d. New: %d" % (setName, count, len(known), len(new))
    for key, value in report.items():
        print "%s: %s" % (key, value)

    known |= set(new)
    with open('parsed/' + fname + '.list', 'w') as fout:
        print >> fout, "\n".join(known)

if __name__ == '__main__':
    mode = PARSE_ALL
    ComputeLimits()
#    doit('gatecrash', 'gatecrash', mode)
    doit('rtr', 'return to ravnica', mode)
#    doit('dgm', 'dragon\'s maze', mode)

    
