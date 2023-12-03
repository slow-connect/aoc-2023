import aoc
import re
import pandas as pd
import numpy as np

data = aoc.get_str(day=3)
# data = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.." #\n..........\n..........\n...11*11.."
width = data.index('\n')
max = (len(data)) // (width + 1)

def neibours(x, y, max=max, width=width):
    if x == 0 and y == 0:
        return [[x+1, y], [x, y+1], [x+1, y+1]]
    elif x == 0 and y == width:
        return [[x+1, y], [x, y-1], [x+1, y-1]]
    elif x == max and y == 0:
        return [[x-1, y], [x, y+1], [x-1, y+1]]
    elif x == max and y == width:
        return [[x-1, y], [x, y-1], [x-1, y-1]]
    elif x == 0:
        return [[x+1, y], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y+1]]
    elif x == max:
        return [[x-1, y], [x, y-1], [x, y+1], [x-1, y-1], [x-1, y+1]]
    elif y == 0:
        return [[x-1, y], [x+1, y], [x, y+1], [x-1, y+1], [x+1, y+1]]
    elif y == width:
        return [[x-1, y], [x+1, y], [x, y-1], [x-1, y-1], [x+1, y-1]]
    else:
        return [[x-1, y], [x+1, y], [x, y-1], [x, y+1], [x-1, y-1], [x+1, y+1], [x-1, y+1], [x+1, y-1]]


def part2():
    regex = r"[*]"
    matches = re.finditer(regex, data, re.MULTILINE)
    characters = []
    mine = data.split('\n')
    for matchNum, match in enumerate(matches, start=1):
        characters.append([match.start() // (width + 1), match.start() % (width + 1) ])
    regex = r"\d+"
    matches = re.finditer(regex, data, re.MULTILINE)
    num = pd.DataFrame(columns=['id', 'line', 'col_start', 'col_end', 'number', 'length'])
    for matchNum, match in enumerate(matches, start=1):
        thisdict = dict(id = (match.start() // (width + 1))*width + match.start() % (width + 1),  line = match.start() // (width + 1), col_start = match.start() % (width + 1), col_end = match.end() % (width + 1), number = int(data[match.start():match.end()]), length = match.end() - match.start())
        df_dict = pd.DataFrame([thisdict])
        num = pd.concat([num, df_dict], ignore_index=True)
    num.set_index('id', inplace=True)
    id_count = pd.DataFrame(columns=['id', 'number', 'char_id'])
    for char in characters:
        nei = neibours(char[0], char[1])
        char_id = char[0]*width + char[1]
        for n in nei:
            nei_id = n[0]*width + n[1]
            if mine[n[0]][n[1]].isdigit():
                if nei_id in num.index:
                    id_count = pd.concat([id_count, pd.DataFrame([dict(id = nei_id, number = num.loc[nei_id]['number'], char_id = char_id)])], ignore_index=True)
                elif nei_id - 1 in num.index:
                    id_count = pd.concat([id_count, pd.DataFrame([dict(id = nei_id - 1, number = num.loc[nei_id - 1]['number'], char_id = char_id)])], ignore_index=True)
                elif nei_id - 2 in num.index:
                    id_count = pd.concat([id_count, pd.DataFrame([dict(id = nei_id - 2, number = num.loc[nei_id - 2]['number'], char_id = char_id)])], ignore_index=True)
    id_count.drop_duplicates(inplace=True)
    id_count.set_index('id', inplace=True)
    print(id_count)
    res = int(id_count.groupby('char_id').filter(lambda x: len(x) > 1).groupby('char_id').prod().groupby('char_id').sum().sum().iloc[0])
    print(res)

def part1():
    regex = r"[^a-zA-z0-9_.\n]"
    regex = r"[*]"
    matches = re.finditer(regex, data, re.MULTILINE)
    characters = []
    mine = data.split('\n')
    for matchNum, match in enumerate(matches, start=1):
        characters.append([match.start() // (width + 1), match.start() % (width + 1) ])
    # print(characters)
    regex = r"\d+"
    matches = re.finditer(regex, data, re.MULTILINE)
    num = pd.DataFrame(columns=['id', 'line', 'col_start', 'col_end', 'number', 'length'])
    for matchNum, match in enumerate(matches, start=1):
        thisdict = dict(id = (match.start() // (width + 1))*width + match.start() % (width + 1),  line = match.start() // (width + 1), col_start = match.start() % (width + 1), col_end = match.end() % (width + 1), number = int(data[match.start():match.end()]), length = match.end() - match.start())
        df_dict = pd.DataFrame([thisdict])
        num = pd.concat([num, df_dict], ignore_index=True)
    num.set_index('id', inplace=True)
    # print(num)
    id_count = set()
    for char in characters:
        nei = neibours(char[0], char[1])
        for n in nei:
            nei_id = n[0]*width + n[1]
            if mine[n[0]][n[1]].isdigit():
                if nei_id in num.index:
                    id_count.add(nei_id)
                if nei_id - 1 in num.index:
                    id_count.add(nei_id - 1)
                if nei_id - 2 in num.index:
                    id_count.add(nei_id - 2)
    cnt = 0
    # print(id_count)
    for id in id_count:
        cnt += num.loc[id]['number']
    print(cnt)
    print(len(id_count))
# part1()
part2()
