file_path = 'inputs/10.in'
with open(file_path, 'r') as file:
    inpt = file.readlines()
inpt = [[int(x) for x in line.strip()] for line in inpt]

R = len(inpt)
C = len(inpt[0])
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

S = []
for r in range(len(inpt)):
    for c in range(len(inpt[0])):
        if inpt[r][c] == 0:
            S.append((r,c))

def search(Q, part1):
    SEEN = []
    ans = 0
    while Q:
        r,c = Q.pop()
        if inpt[r][c] == 9 and (r,c) not in SEEN:
            ans += 1
            SEEN.append((r,c))
        elif not part1 and inpt[r][c] == 9:
            ans += 1
        else:
            for dr,dc in dirs:
                rr = r+dr
                cc = c+dc
                if 0<=rr<R and 0<=cc<C and inpt[rr][cc] == inpt[r][c]+1:
                    Q.append((rr,cc))
    return ans

p1, p2 = 0, 0
for s in S:
    p1 += search([s], True)
p2 = search(S, False)

print(p1)
print(p2)