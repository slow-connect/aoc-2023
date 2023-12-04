import aoc
import re
from math import pow
import numpy as np

data = aoc.get_lst(4)
# data = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n".split('\n')
points = 0
counts = [1 for _ in range(len(data) - 1)]
for k in range(len(data)-1):
    data[k] = re.sub(" +", " ", data[k])
    tmp = data[k].split(': ')
    tmp = tmp[1].split(' | ')
    winning = tmp[0].split(' ')
    have = tmp[1].split(' ')
    win_set = set()
    have_set = set()
    for j in range(len(winning)):
        win_set.add(int(winning[j]))
    for j in range(len(have)):
        have_set.add(int(have[j]))
    if False:
        tmp = 0 if len(have_set.intersection(win_set)) == 0 else pow(2, len(have_set.intersection(win_set)) - 1)
        points += int(tmp)

    if True:
        for kk in range(k+1, k + len(have_set.intersection(win_set)) + 1):
            counts[kk] += counts[k]

if False:
    print(points)
if True:
    print(sum(counts))
