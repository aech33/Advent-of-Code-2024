file_path = "inputs/22.in"
with open(file_path, "r") as file:
    S = file.read().split("\n")

def evolve(s):
    s ^= s*64
    s = s%16777216
    s ^= s//32
    s = s%16777216
    s ^= s*2048
    s = s%16777216
    return s

p1 = 0

P = {}
for secret in S:
    cur = int(secret)
    last = -1
    SEEN = set()
    pattern = []

    for i in range(2001):
        if len(pattern) == 4:
            pat = tuple(pattern)
            if pat not in SEEN:
                SEEN.add(pat)
                if pat not in P:
                    P[pat] = last%10
                else:
                    P[pat] += last%10
            pattern = pattern[1:]

        if last != -1:
            pattern.append(cur%10-last%10)

        last = cur
        cur = evolve(cur)

    p1 += last

p2 = 0
for pat in P:
    p2 = max(p2,P[pat])

print(p1)
print(p2)