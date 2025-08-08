def check(level):
    up = level[0] < level[1]
    for l in range(len(level) - 1):
        if not (1 <= abs(level[l]-level[l+1]) <= 3 and up == (level[l] < level[l+1])):
            return False
    else:
        return True

def part1(levels):
    return sum(map(check, levels))

def part2(levels):
    return sum(
        check(l) or any(check(l[:i] + l[i+1:]) for i in range(len(l)))
        for l in levels
    )

with open('inputs/2.in') as f:
    levels = [list(map(int, line.split())) for line in f]

print(part1(levels))
print(part2(levels))