file_path = "inputs/16.in"
M = []
with open(file_path, 'r') as file:
    for line in file.readlines():
        M.append(line.strip())
R = len(M)
C = len(M[0])
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

Q = [(R-2,1,1,0)]
SEEN = []
COST = {}
while Q:
    r,c,d,q = Q.pop()
    if (r,c,d) in SEEN:
        continue
    if (r,c) not in COST or COST[(r,c)] > q:
        COST[(r,c)] = q
    SEEN.append((r,c,d))
    dr,dc = DIRS[d]
    rr = r+dr
    cc = c+dc
    if M[rr][cc] != "#":
        Q.append((rr,cc,d,q+1))
    Q.append((r,c,(d+1)%4,q+1000))
    Q.append((r,c,(d+3)%4,q+1000))
print(COST[(1,C-2)])