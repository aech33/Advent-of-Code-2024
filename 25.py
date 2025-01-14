from itertools import product

def convert(K):
    R = len(K)
    C = len(K[0])
    heights = [0]*C
    for r in range(R):
        for c in range(C):
            if K[r][c] == "#":
                heights[c] += 1
    return (K[0] == ".....",heights)

def check_pair(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 7:
            return False
    return True

file_path = "inputs/25.in"
with open(file_path, "r") as file:
    tumblers = file.read().split("\n\n")

keys = []
locks = []

for t in tumblers:
    is_lock, heights = convert(t.split("\n"))
    if is_lock:
        locks.append(heights)
    else:
        keys.append(heights)

ans = 0
for (k,l) in product(keys, locks):
    if check_pair(k,l):
        ans += 1

print(ans)

