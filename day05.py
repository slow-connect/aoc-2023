import aoc

data = aoc.get_str(5)[:-1]
data = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
data = data.split('\n\n')
seeds = data[0]
if False:
    seeds = [int(k) for k in seeds.split(' ') if k.isdigit()]
if True:
    seed = [int(k) for k in seeds.split(' ') if k.isdigit()]
    actualseeds = []
    for k in range(0, len(seed), 2):
        actualseeds.append([seed[k], seed[k] + seed[k+1] - 1])
        # do again if some more time with intervals, and go over evolution of seeds, not maps
    seeds = actualseeds
print(seeds)
moves = []
for k in range(1, len(data)):
    moves.append(data[k].split('\n'))
    tmp = []
    for j in range(1, len(moves[k-1])):
        tmp.append([int(x) for x in moves[k-1][j].split(' ') if x.isdigit()])
    for j in range(len(tmp)):
        tmp[j][2] = tmp[j][1] + tmp[j][2] - 1
    moves[k-1] = tmp
print(moves)
min = 100000000000
for seed in seeds:
    for k in range(len(moves)):
        for j in range(len(moves[k])):
            if moves[k][j][1] <= seed[0] <= seed[1] <= moves[k][j][2]:
                seed[0] -= moves[k][j][1] - moves[k][j][0]
            if
    # pass through the different maps
    pass



def p1(seeds):
    for k in range(1, len(data)):
        tmp = data[k].split('\n')
        print(tmp[0])
        copy = seeds.copy()
        for i in range(1, len(tmp)):
            ttmp = [int(j) for j in tmp[i].split(' ') if j.isdigit()]
            for kk in range(len(seeds)):
                if seeds[kk] in range(ttmp[1], ttmp[1] + ttmp[2]):
                    copy[kk] -= ttmp[1] - ttmp[0]
        seeds = copy.copy()
        return min(seeds)


# print(p2(seeds))
