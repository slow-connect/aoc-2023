import aoc
import re

data = aoc.get_lst(1)
num = []
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# test = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
# test = data.split('\n')

def two_digit_1(str):
    num = ''
    for i in range(len(str)):
        if str[i] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            num += str[i]
            break
    for i in range(len(str)-1, -1, -1):
        if str[i] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            num += str[i]
            break
    if len(num) == 0:
        return 0
    else:
        return int(num)

def two_digit_2(str):
    for k in range(len(numbers)):
        p = re.compile(numbers[k])
        str = str.replace(numbers[k], numbers[k] + k.__str__() + numbers[k])
    return two_digit_1(str)

res = 0
if False:
    for i in range(len(data)):
        res += two_digit_1(data[i])
if True:
    for i in range(len(data)):
        res += two_digit_2(data[i])
print(res)
