f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]

double = 0
triple = 0
correct = ''

for line in lines:
    counts = {}
    for c in line:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    double += 1 if 2 in counts.values() else 0
    triple += 1 if 3 in counts.values() else 0

    for i in range(len(line)):
        diff = line[:i] + line[i + 1:]
        if [l[:i] + l[i + 1:] for l in lines].count(diff) > 1:
            correct = diff


part1 = double * triple
part2 = correct

print(f'part 1: {part1}')
print(f'part 2: {part2}')
