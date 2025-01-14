import re
from collections import deque

def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

file_path = 'inputs/15.in'
with open(file_path, 'r') as file:
    D, moves = file.read().split("\n\n")

G = [list(x) for x in D.split("\n")]
moves = moves.replace("\n","")

R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]
dirs = {">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}

BIG_G = []
for r in range(R):
    row = []
    for c in range(C):
        if G[r][c]=="@":
            row += ["@","."]
        elif G[r][c]=="O":
            row += ["[","]"]
        else:
            row += [G[r][c], G[r][c]]
    #print("".join(row))
    BIG_G.append(row)

G = BIG_G
C *= 2

for r in range(R):
    for c in range(C):
        if G[r][c] == '@':
            sr,sc = r,c
            G[r][c] = '.'

r,c = sr,sc
for m in moves:
    if m == '\n':
        continue
    dr,dc = dirs[m]
    rr,cc = r+dr,c+dc
    if G[rr][cc]=='#':
        continue
    elif G[rr][cc]=='.':
        r,c = rr,cc
    elif G[rr][cc] in ['[', ']']:
        Q = deque([(r,c)])
        SEEN = set()
        ok = True
        while Q:
            rr,cc = Q.popleft()
            if (rr,cc) in SEEN:
                continue
            SEEN.add((rr,cc))
            rrr,ccc = rr+dr, cc+dc
            if G[rrr][ccc]=='#':
                ok = False
                break
            if G[rrr][ccc]=='[':
                Q.append((rrr,ccc))
                assert G[rrr][ccc+1]==']'
                Q.append((rrr,ccc+1))
            if G[rrr][ccc]==']':
                Q.append((rrr,ccc))
                assert G[rrr][ccc-1]=='['
                Q.append((rrr,ccc-1))
        if not ok:
            continue
        while len(SEEN) > 0:
            for rr,cc in sorted(SEEN):
                rrr,ccc = rr+dr,cc+dc
                if (rrr,ccc) not in SEEN:
                    assert G[rrr][ccc] == '.'
                    G[rrr][ccc] = G[rr][cc]
                    G[rr][cc] = '.'
                    SEEN.remove((rr,cc))
        r = r+dr
        c = c+dc

ans = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == "[":
            ans += 100*r+c
print(ans)