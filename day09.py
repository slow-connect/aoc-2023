import aoc
import numpy as np

data = aoc.get_lst(9)[:-1]
# data = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45".split('\n')
# print(data)


part1 = True
ans = 0
for line in data:
    val = line.split()
    mat = np.zeros((len(val), len(val)))
    for k in range(len(val)):
        mat[0][k] = int(val[k])
    for i in range(1, len(val)):
        for j in range(i, len(val)):
            mat[i][j] = mat[i-1][j] - mat[i-1][j-1]
        if sum(mat[i]) == 0:
            if part1 == False:
                ans += int(sum(mat[_][_]*(-1)**_ for _ in range(len(val))))
            else:
                ans += int(sum(mat[_][-1] for _ in range(len(val))))
            break

print(ans)
