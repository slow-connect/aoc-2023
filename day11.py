import aoc

data = aoc.get_lst(11)[:-1]
# data = "...#......\n.......#..\n#.........\n..........\n......#...\n.#........\n.........#\n..........\n.......#..\n#...#.....".split('\n')
length, width = len(data), len(data[0])

zero_rows = []
for i in range(length):
    if data[i] == '.'*width:
        zero_rows.append(i)

zero_cols = []
for j in range(width):
    maxi = 0
    for i in range(length):
        if data[i][j] == '.':
            maxi += 1
    if maxi == length:
        zero_cols.append(j)

galaxies = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            galaxies.append((i, j))


distance = []
for i in range(len(data)):
    if i in set(zero_rows):
        distance.append([1000000 for _ in range(len(data[i]))])
    else:
        distance.append([])
    for j in range(len(data[i])):
        if j in set(zero_cols):
            distance[i].append(1000000)
        else:
            distance[i].append(1)

def distances(a, b, distances):
    dist = 0
    for j in range(min(a[1], b[1]), max(a[1], b[1])):
        dist += distances[a[0]][j]
    for i in range(min(a[0], b[0]), max(a[0], b[0])):
        dist += distances[i][a[1]]
    return dist

ans = 0
print(len(data) == len(distance))
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        ans += distances(galaxies[i], galaxies[j], distance)


print(ans)

def p1():
    expanded = data.copy()
    ins = 0
    for i in range(length):
        if data[i] == '.'*width:
            expanded.insert(i+ins, "."*width)
            ins += 1


    ins = 0
    for j in range(width):
        max = 0
        for i in range(length):
            if j == width:
                print("WTF")
            if data[i][j] == '.':
                max += 1
        if max == length:
            for i in range(len(expanded)):
                expanded[i] = expanded[i][:j+ins] + '.' + expanded[i][j+ins:]
            ins += 1

    def distance (a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    galaxies = []

    for i in range(len(expanded)):
        for j in range(len(expanded[i])):
            if expanded[i][j] == '#':
                galaxies.append((i, j))


    ans = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            ans += distance(galaxies[i], galaxies[j])

    print(ans)
