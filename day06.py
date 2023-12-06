import aoc
from tqdm import tqdm

if False:
    data = [[51, 222], [92, 2031], [68, 1126],[90, 1225]]
    data = [[7, 9], [15, 40], [30, 200]]
if True:
    data = [51926890, 222203111261225]
    # data = [71530, 940200]

over_max = 0
for i in tqdm(range((data[0]))):
    if i*(data[0]-i) > data[1]:
        over_max += 1
print(over_max)


def p1(data):
    cnt = 1
    for time, distance in data:
        over_max = 0
        for i in range(time):
            if i*(time-i) > distance:
                over_max += 1
        cnt *= over_max

    print(cnt)
