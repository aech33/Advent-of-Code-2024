file_path = 'inputs/16.in'
M = []
with open(file_path, 'r') as file:
    for line in file.readlines():
        M.append(line.strip())
R = len(M)
C = len(M[0])

def print_it(X):
    outfile = "16.out"
    with open(outfile, 'w') as file:
        for r in range(R):
            for c in range(C):
                if (r,c) not in X:
                    file.write(M[r][c]*4+"  ")
                else:
                    file.write(str(X[(r,c)]).ljust(6))
            file.write("\n")
            file.write("\n")

def get_dirs(d):
    if d == (-1,1):
        return [0,3]
    elif d == (1,1):
        return [0,1]
    elif d == (1,-1):
        return [1,2]
    elif d == (-1,-1):
        return [2,3]

def add_dist(r,c,rr,cc,DIST,add):
    if (rr,cc) not in DIST:
        DIST[(rr,cc)] = []
    for d in DIST[(r,c)]:
        DIST[(rr,cc)] += [d+add]
    return DIST


sr,sc = R-2,0
er,ec = 1,C-2
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
DIAS = [(-1,1),(1,1),(1,-1),(-1,-1)] # diagonal dirs

SEEN = []
DIST = {(sr,sc):[-1]}
Q = [(sr,sc,0)]
while Q:
    #print(Q)
    r,c,d = Q.pop()

    dr,dc = DIRS[d]
    rr = r+dr
    cc = c+dc

    # keep going the same direction
    if 0<=rr<R and 0<=cc<C and M[rr][cc] != "#":
        if (rr,cc) not in DIST or DIST[(rr,cc)] > DIST[(r,c)] + 1:
            DIST = add_dist(r,c,rr,cc,DIST,1)
            Q.append((rr,cc,d))

    # try the other directions
    if d == 3:
        TURNS = [DIAS[3]] + [DIAS[0]]
    else:
        TURNS = DIAS[d:d+2]
    if (r,c) == (7,8):
        print(r,c,d,TURNS)
    for i,(dr,dc) in enumerate(TURNS):
        rr = r+dr
        cc = c+dc
        #print(M[rr][cc],M[rr][c],M[r][cc])
        if 0<=rr<R and 0<=cc<C and M[rr][cc] != "#" and (M[rr][c] != "#" or M[r][cc] != "#"):
            if (rr,cc) not in DIST or DIST[(rr,cc)] > DIST[(r,c)] + 1002:
                DIST = add_dist(r,c,rr,cc,DIST,1002)
                if i == 0:
                    new_d = (d+3)%4
                elif i == 1:
                    new_d = (d+1)%4
                Q.append((rr,cc,get_dirs((dr,dc))[0]))
                Q.append((rr,cc,get_dirs((dr,dc))[1]))

SEEN = []
def search(r,c):
    if (r,c) not in SEEN:
        for dr,dc in DIRS:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and M[rr][cc] != "#":
                if 





