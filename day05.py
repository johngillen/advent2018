f = open('input/day05.txt')
lines = [line.rstrip() for line in f.readlines()]

def react(polymer):
    i = 0
    while i < len(polymer) - 1:
        if polymer[i].lower() == polymer[i + 1].lower() and polymer[i] != polymer[i + 1]:
            polymer = polymer[:i] + polymer[i + 2:]
            i = max(0, i - 1)
        else:
            i += 1
    return polymer

units = {}

for i in range(26):
    polymer = lines[0]
    polymer = polymer.replace(chr(ord('a') + i), '')
    polymer = polymer.replace(chr(ord('A') + i), '')
    units[chr(ord('a') + i)] = react(polymer)

polymer = lines[0]

part1 = len(react(polymer))
part2 = min([len(units[i]) for i in units])

print(f'part 1: {part1}')
print(f'part 2: {part2}')
