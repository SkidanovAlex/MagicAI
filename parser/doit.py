import urllib2
import re

from parser import ParseCard

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

def removeImages(text):
    text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/tap.gif" alt="{T}" />', '[TAP]')
    for mana1 in "brguwx":
        MANA1 = mana1.upper()
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s.gif" alt="{%s}" />' % (mana1, MANA1), '[%s]' % MANA1)
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s.gif" alt="%s" class="inlineimg" style="border: none;" />' % (mana1, mana1), '[%s]' % MANA1)
        for mana2 in "brguw":
            MANA2 = mana2.upper()
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="{%s%s}" />' % (MANA1, MANA2, MANA1, MANA2), '[%s%s]' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="{%s%s}" />' % (mana1, mana2, mana1, mana2), '[%s%s]' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="%s%s" class="inlineimg" style="border: none;" />' % (mana1, mana2, mana1, mana2), '[%s%s]' % (MANA1, MANA2))
            text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%s%s.gif" alt="%s%s" class="inlineimg" style="border: none;" />' % (mana1, mana2, mana2, mana1), '[%s%s]' % (MANA1, MANA2))
    for i in range(100):
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%d.gif" alt="%d" class="inlineimg" style="border: none;" />' % (i, i), '[%d]' % i)
        text = text.replace('<img src="http://forums.mtgsalvation.com/images/smilies/mana%d.gif" alt="%d" />' % (i, i), '[%d]' % i)
    return text

def doit(url, fname, name):
    if url != None:
        website = urllib2.urlopen(url).read()
    elif fname != None:
        website = open(fname, 'r').read()
    else:
        assert False
    lastPos = 0
    count = 0
    good = 0
    while True:
        res = parseBetween(website, '<table border="0" cellspacing="0" cellpadding="5" width="290" align="center" style="border: 1px solid black;background-color:white;color: black;">', '</table>', lastPos + 1);
        if res == None: break
        content, lastPos = res
        name = stripTags(parseBetween(content, '<h3 style="margin: 0;">', '</h3>'))
        if name[0] == '*': name = name[1:]
        cost, nextPos = parseBetween(content, '<td align="right" width="80px">', '</td>', 0)
        cost = removeImages(cost)
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
        """
        print "NAME: '%s', COST: '%s' TYPE: '%s', SUBTYPES: '%s'\n%s" % (name, cost, ':'.join(types), ':'.join(subtypes), cardText)
        if 'Creature' in types:
            print "%s/%s" % (pwr, tgh);
        print "\n"
        """
        if ParseCard(cardText) != None:
            print "%s: OK" % name
            good += 1

        count += 1
    print "Total cards: %d. Parsed: %d" % (count, good)

if __name__ == '__main__':
    #doit('http://www.mtgsalvation.com/gatecrash-spoiler.html', None, 'gatecrash');
    doit(None, 'spoilers/rtr.txt', 'gatecrash')

    
