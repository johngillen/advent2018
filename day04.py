f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

lines = sorted(lines)

guards = {}

for line in lines:
    if 'Guard' in line:
        guard = int(line.split()[3][1:])
        if guard not in guards:
            guards[guard] = [0 for i in range(60)]
    elif 'falls' in line:
        start = int(line.split()[1][3:5])
    elif 'wakes' in line:
        end = int(line.split()[1][3:5])
        for i in range(start, end):
            guards[guard][i] += 1

part1 = max(guards, key=lambda x: sum(guards[x])) * \
            guards[max(guards, key=lambda x: sum(guards[x]))].index\
                (max(guards[max(guards, key=lambda x: sum(guards[x]))]))
part2 = max(guards, key=lambda x: max(guards[x])) * \
            guards[max(guards, key=lambda x: max(guards[x]))].index\
                (max(guards[max(guards, key=lambda x: max(guards[x]))]))

print(f'part 1: {part1}')
print(f'part 2: {part2}')
