import aoc
import numpy as np

data = aoc.get_str(13)[:-1].split('\n\n')
# data = "#.##..##.\n..#.##.#.\n##......#\n##......#\n..#.##.#.\n..##..##.\n#.#.##.#.\n\n#...##..#\n#....#..#\n..##..###\n#####.##.\n#####.##.\n..##..###\n#....#..#".split('\n\n')
data = [data[_].split('\n') for _ in range(len(data))]

for k in range(len(data)):
    for line in data[k]:
        print(line)
    print()


ans = 0
for group in data:
    matrix = np.array([[1 if group[i][j] == '#' else 0 for j in range(len(group[i]))] for i in range(len(group))])
    for k in range(len(matrix)):
        tmp = []
        for i in range(min(k+1, len(matrix) - k-1)):
            tmp.append(matrix[k-i] == matrix[k+i+1])
        tmp = [all(tmp[i]) for i in range(len(tmp))]
        if all(tmp) and len(tmp) > 1:
            ans += 100*(k+1)
    matrix = np.transpose(matrix)
    for k in range(len(matrix)):
        tmp = []
        for i in range(min(k+1, len(matrix) - k-1)):
            tmp.append(matrix[k-i] == matrix[k+i+1])
        tmp = [all(tmp[i]) for i in range(len(tmp))]
        if all(tmp) and len(tmp) > 1:
            ans += (k+1)
print(ans)
