file_path = 'inputs/12.in'
with open(file_path, 'r') as file:
    data = [[x for x in line.strip()] for line in file.readlines()]

R = len(data)
C = len(data[0])
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

GARDENS = []
SEEN = set()
for r in range(R):
    for c in range(C):
        if (r,c) in SEEN:
            continue
        G = []
        Q = [(r,c)]
        while Q:
            r2,c2 = Q.pop()
            if (r2,c2) in SEEN:
                continue
            G.append((r2,c2))
            SEEN.add((r2,c2))
            for dr, dc in DIRS:
                rr = r2+dr
                cc = c2+dc
                if 0<=rr<R and 0<=cc<C and data[r2][c2] == data[rr][cc]:
                    Q.append((rr,cc))
            
        GARDENS.append(G)

p1,p2 = 0,0

for G in GARDENS:
    area = len(G)

    E = set()
    for r,c in G:
        for d, (dr, dc) in enumerate(DIRS):
            if (r+dr,c+dc) not in G:
                E.add((d,r+dr,c+dc))

    sides = 0
    SEEN = []
    for d,r,c in E:
        if (d,r,c) not in SEEN:
            Q = [(d,r,c)]
            while Q:
                cd, cr, cc = Q.pop()  
                for dr, dc in DIRS:
                    if (cd,cr+dr,cc+dc) in E and (cd,cr+dr,cc+dc) not in SEEN:
                        Q.append((cd,cr+dr,cc+dc))
                SEEN.append((cd, cr, cc))
            sides += 1
    perimeter = len(E)
    p1 += area*perimeter
    p2 += area*sides

print(p1)
print(p2)


