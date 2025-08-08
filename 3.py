import re

pattern = re.compile(r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)")

def part1(data):
    return sum(
    int(a) * int(b)
    for match in pattern.finditer(data)
    for a, b in [match.groups()]
    )


def part2(data):
    valid_zones = re.findall(r"do\(\)(.*?)don't\(\)", "do()"+data+"don't()")
    return sum(part1(vz) for vz in valid_zones)

with open('inputs/3.in', 'r') as f:
    data = f.readline()

print(part1(data))
print(part2(data))