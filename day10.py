import aoc

data = aoc.get_lst(10)
# data = "7-F7-\n.FJ|7\nSJLL7\n|F--J\nLJ.LJ".split('\n')
data = ".F----7F7F7F7F-7....\n .|F--7||||||||FJ....\n.||.FJ||||||||L7....\nFJL7L7LJLJ||LJ.L-7..\nL--J.L7...LJS7F-7L7.\n....F-J..F7FJ|L7L7L7\n....L7.F7||L7|.L7L7|\n.....|FJLJ|FJ|F7|.LJ\n....FJL-7.||.||||...\n....L---J.LJ.LJLJ...\n"

data.insert(0, '.'*(len(data[0])+2))
data.append('.'*(len(data[0]) + 1))
for i in range(1, len(data)-1):
    data[i] = '.' + data[i] + '.'

for k in range(len(data)):
    for i in range(len(data[k])):
        if data[k][i] == 'S':
            start = (k, i)
            break


def next_pos(prev_pos, current_pos):
    if data[current_pos[0]][current_pos[1]] == '.':
        return current_pos
    elif data[current_pos[0]][current_pos[1]] == '-':
        return (current_pos[0], current_pos[1]+1) if prev_pos[1] < current_pos[1] else (current_pos[0], current_pos[1]-1)
    elif data[current_pos[0]][current_pos[1]] == '|':
        return (current_pos[0]+1, current_pos[1]) if prev_pos[0] < current_pos[0] else (current_pos[0]-1, current_pos[1])
    else:
        in_y = prev_pos[0] != current_pos[0]
        if data[current_pos[0]][current_pos[1]] == 'F':
            if in_y:
                return (current_pos[0], current_pos[1]+1)
            else:
                return (current_pos[0]+1, current_pos[1])
        elif data[current_pos[0]][current_pos[1]] == '7':
            if in_y:
                return (current_pos[0], current_pos[1]-1)
            else:
                return (current_pos[0]+1, current_pos[1])
        elif data[current_pos[0]][current_pos[1]] == 'J':
            if in_y:
                return (current_pos[0], current_pos[1]-1)
            else:
                return (current_pos[0]-1, current_pos[1])
        elif data[current_pos[0]][current_pos[1]] == 'L':
            if in_y:
                return (current_pos[0], current_pos[1]+1)
            else:
                return (current_pos[0]-1, current_pos[1])

paths  = [[start, (start[0]+1 , start[1])], [start, (start[0]-1, start[1])], [start, (start[0], start[1]-1)], [start, (start[0], start[1]+1)]]
k=1

for k in range(4):
    while True:
        paths[k].append(next_pos(paths[k][-2], paths[k][-1]))
        if paths[k][-1][0] == start[0] and paths[k][-1][1] == start[1]:
            break
        if paths[k][-1][0] == paths[k][-2][0] and paths[k][-1][1] == paths[k][-2][1]:
            break

for k in range(4):
    if paths[k][-1] == start:
        print((len(paths[k])-1)//2)
