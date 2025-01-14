from itertools import combinations

file_path = 'inputs/8.in'
with open(file_path, 'r') as file:
    lines = file.readlines()


locs = {}
antennas = set()
for r, line in enumerate(lines):
    for c, freq in enumerate(line.strip()):
        if freq == ".":
            continue
        antennas.add((r,c))
        if freq not in locs.keys():
            locs[freq] = [(r,c)]
        else:
            locs[freq].append((r,c))


P1 = set()
P2 = set()
R = len(lines)
C = len(lines[0].strip())
for k,v in locs.items():
    for r1,c1 in v:
        for r2,c2 in v:   
            if (r1,c1) == (r2,c2):
                continue
            dr = abs(r2-r1)
            dc = abs(c2-c1)
            i = 1
            while True:
                rr1,cc1 = r1-i*dr if r1<=r2 else r1+i*dr, c1+i*dc if c1>=c2 else c1-i*dc
                rr2,cc2 = r2-i*dr if r2<=r1 else r2+i*dr, c2-i*dc if c1>=c2 else c2+i*dc
                if 0<=rr1<R and 0<=cc1<C:
                    if i == 1:
                        P1.add((rr1,cc1))
                    P2.add((rr1,cc1))
                if 0<=rr2<R and 0<=cc2<C:
                    if i == 1:
                        P1.add((rr2,cc2))
                    P2.add((rr2,cc2))
                if not(0<=rr1<R and 0<=cc1<C) and not(0<=rr2<R and 0<=cc2<C):
                    break
                i+=1

print(len(P1))
print(len(P2.union(antennas)))

