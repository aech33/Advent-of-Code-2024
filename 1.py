from collections import Counter

def part1(a,b):
    return sum(abs(f[0]-f[1]) for f in zip(sorted(a),sorted(b)))

def part2(a,b):
    C = Counter(b)
    return sum(C[x] * x for x in a)

with open('inputs/1.in') as f:
    a, b = zip(*(map(int, line.split("   ")) for line in f))
a, b = list(a), list(b)

print(part1(a,b))
print(part2(a,b))