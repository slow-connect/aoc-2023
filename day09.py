import aoc
import numpy as np

data = aoc.get_lst(9)[:-1]
# data = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45".split('\n')
# print(data)


ans = 0
for line in data:
    val = line.split()
    mat = np.zeros((len(val), len(val)))
    for k in range(len(val)):
        mat[0][k] = int(val[k])
    for i in range(1, len(val)):
        for j in range(len(val)-i):
            mat[i][j] = mat[i-1][j+1] - mat[i-1][j]
        if sum(mat[i]) == 0:
            ans += int(sum(mat[_][0]*(-1)**_ for _ in range(len(val))))
            break

print(ans)




def part1():
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
                ans += int(sum(mat[_][-1] for _ in range(len(val))))
                break

    print(ans)
