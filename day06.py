f = open('input/day06.txt')
lines = [line.rstrip() for line in f.readlines()]

plane = [[0 for i in range(1000)] for j in range(1000)]

for line in lines:
    x, y = line.split(', ')
    x = int(x)
    y = int(y)

    plane[x][y] = line


    

part1 = 0
part2 = 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
