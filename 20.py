file_path = "inputs/20.in"
with open(file_path, "r") as file:
    G = [list(line.strip()) for line in file.readlines()]

R = len(G)
C = len(G[0])
DIRS = [(0,1),(1,0),(-1,0),(0,-1)]

#s=start, e=end
sr,sr,er,et = 0,0,0,0
for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr,sc = r,c
        elif G[r][c] == "E":
            er,ec = r,c

# dijkstra's with no cheats

def dijkstra(start_r, start_c):
    Q = [(start_r,start_c)]
    SEEN = []
    DIST = {(start_r,start_c):0}
    while Q:
        r,c = Q.pop()
        if (r,c) in SEEN:
            continue
        SEEN.append((r,c))

        for dr,dc in DIRS:
            rr = r+dr
            cc = c+dc
            if G[rr][cc] != "#":
                if (rr,cc) not in DIST or DIST[(rr,cc)] > DIST[(r,c)]+1:
                    DIST[(rr,cc)] = DIST[(r,c)]+1
                Q.append((rr,cc))
    return DIST

def get_cheats(length):
    C = []
    for dr in range(-length,length+1):
        for dc in range(-length,length+1):
            if abs(dr)+abs(dc) <= length:
                C.append((dr,dc))
    return C

DIST_TO = dijkstra(sr,sc)
DIST_FROM = dijkstra(er,ec)
CHEAT_DIRS = get_cheats(20)

p1,p2 = 0,0
for r in range(R):
    for c in range(C):
        if G[r][c] == "#":
            continue
        for dr,dc in CHEAT_DIRS:
            rr = r+dr
            cc = c+dc
            if not(0<=rr<R and 0<=cc<C) or G[rr][cc] == "#":
                continue
            if (r,c) == (sr,sc) and (rr,cc) == (7,3):
                print(DIST_TO[(r,c)], dr,dc, DIST_FROM[(rr,cc)])
            if DIST_TO[(r,c)] + abs(dr)+abs(dc) + DIST_FROM[(rr,cc)] + 100 <= DIST_FROM[(sr,sc)]:
                if abs(dr)+abs(dc)==2:
                    p1 += 1
                p2 += 1
print(p1)
print(p2)