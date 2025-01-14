from math import prod

file_path = "inputs/19.in"
with open(file_path, "r") as file:
    patterns, designs = file.read().split("\n\n")

patterns = patterns.strip().split(", ")
designs = designs.split("\n")

DP = {}

def check_design(d):
    if d in DP:
        return DP[d]
    S = []
    for i in range(len(d)):
        if d[:i] in patterns:
            S.append(check_design(d[i:]))
    DP[d] = sum(S)
    return sum(S)

def check_pattern(p):
    S=0
    if p == "":
        return 1
    for i in range(1,len(p)+1):
        if p[:i] in patterns:
            S += check_pattern(p[i:])
    return S

for p in patterns:
    DP[p] = check_pattern(p)

p1 = 0
p2 = 0
for d in designs:
    if check_design(d):
        p1 += 1
    p2 += check_design(d)
print(p1)
print(p2)
