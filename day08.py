import aoc
import re
from functools import reduce
import math

data = aoc.get_lst(8)
# data = "RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)".split('\n')
# data = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)".split('\n')
# data = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)".split('\n')
instructions = data[0]

lst = []
for i in range(2, len(data)):
    line = re.findall(r'[A-Z0-9][A-Z0-9][A-Z]', data[i])
    lst.append(line)

starts = []
lst = lst[:-1]
for i in range(len(lst)):
    # print(lst[i])
    if len(re.findall(r'[A-Z0-9][A-Z0-9]A', lst[i][0])) == 1:
        starts.append(lst[i][0])

cnts = []
# print(starts)
for node in starts:
    cnt = 0
    # print(node)
    while len(re.findall(r'[A-Z0-9][A-Z0-9]Z', node)) == 0:
        for i in range(len(instructions)):
            for k in range(len(lst)):
                if node == lst[k][0]:
                    if instructions[i] == 'L':
                        node = lst[k][1]
                    elif instructions[i] == 'R':
                        node = lst[k][2]
                    cnt += 1
                    if len(re.findall(r'[A-Z0-9][A-Z0-9]Z', node)) == 1:
                        cnts.append(cnt)
                        print(cnt)
                        break
                    break
            if len(re.findall(r'[A-Z0-9][A-Z0-9]Z', node)) ==1:
                break
        if len(re.findall(r'[A-Z0-9][A-Z0-9]Z', node)) == 1:
            break



def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)
print(lcm(cnts))

def p1():
    node = 'AAA'
    cnt = 0
    while node !=  'ZZZ':
        for i in range(len(instructions)):
            for k in range(len(lst)):
                if node == lst[k][0]:
                    if instructions[i] == 'L':
                        node = lst[k][1]
                    elif instructions[i] == 'R':
                        node = lst[k][2]
                    cnt += 1
                    if node == 'ZZZ':
                        print(cnt)
                        break
                    break
            if node == 'ZZZ':
                break
        if node == 'ZZZ':
            break
