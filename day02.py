import aoc
import re

data = aoc.get_lst(2)
# data = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\n".split('\n')
re_str = r"Game \d*: "
re_pattern = r"[0-9]* (green|blue|red)"

def p2(re_str, re_pattern):
    cnt = 0
    for k in range(len(data)-1):
        l_red, l_green, l_blue = [], [], []
        matches = re.finditer(re_pattern, data[k])
        for matchNum, match in enumerate(matches, start=1):
            tmp = data[k][match.start():match.end()]
            tmp = tmp.split()
            if tmp[1] == 'red':
                l_red.append(int(tmp[0]))
            if tmp[1] == 'green':
                l_green.append(int(tmp[0]))
            if tmp[1] == 'blue':
                l_blue.append(int(tmp[0]))

        thisdict = dict(id = k+1, red=max(l_red), green=max(l_green), blue=max(l_blue))
        cnt +=  thisdict['blue']*thisdict['green']*thisdict['red']
    return cnt
def p1(re_str, re_pattern):
    cnt = 0
    constraits = dict(id=0, red=12, green=13, blue=14)
    for k in range(len(data)-1):
        l_red, l_green, l_blue = [], [], []
        matches = re.finditer(re_pattern, data[k])
        for matchNum, match in enumerate(matches, start=1):
            tmp = data[k][match.start():match.end()]
            tmp = tmp.split()
            if tmp[1] == 'red':
                l_red.append(int(tmp[0]))
            if tmp[1] == 'green':
                l_green.append(int(tmp[0]))
            if tmp[1] == 'blue':
                l_blue.append(int(tmp[0]))

        thisdict = dict(id = k+1, red=max(l_red), green=max(l_green), blue=max(l_blue))
        if thisdict['blue'] <= constraits['blue'] and thisdict['green'] <= constraits['green'] and thisdict['red'] <= constraits['red']:
            cnt += thisdict['id']

    return cnt
print(p2(re_str, re_pattern))
