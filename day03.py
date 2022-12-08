f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

fabric = [[0 for i in range(1000)] for j in range(1000)]
clear = 0

for line in lines:
    id, x, y, w, h = [int(i) for i in re.findall(r'\d+', line)]

    for i in range(x, x + w):
        for j in range(y, y + h):
            fabric[i][j] += 1
    
for line in lines:
    id, x, y, w, h = [int(i) for i in re.findall(r'\d+', line)]

    for i in range(x, x + w):
        for j in range(y, y + h):
            if fabric[i][j] > 1:
                break
        else:
            continue
        break
    else:
        clear = id
                

part1 = sum([1 for i in range(1000) for j in range(1000) if fabric[i][j] > 1])
part2 = clear

print(f'part 1: {part1}')
print(f'part 2: {part2}')
