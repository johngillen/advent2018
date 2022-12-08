f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

frequencies = [0]

while frequencies[-1] not in frequencies[:-1]:
    for line in lines:
        frequencies.append(frequencies[-1] + int(line))
        if frequencies[-1] in frequencies[:-1]:
            break

part1 = frequencies[len(lines)]
part2 = frequencies[-1]

print(f'part 1: {part1}')
print(f'part 2: {part2}')
