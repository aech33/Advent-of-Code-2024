file_path = 'inputs/15.in'
with open(file_path, 'r') as file:
    W, moves = file.read().split("\n\n")

W = [list(x) for x in W.split("\n")]
moves = moves.replace("\n","")

R = len(W)
C = len(W[0])
dirs = {">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}

def print_it(D):
    for r2 in range(R):
        for c2 in range(C):
            print(D[r2][c2],end="")
        print()

def check_move(r,c,dr,dc):
    print(r,c)
    rr = r+dr
    cc = c+dc
    if W[rr][cc] == "#":
        return False
    elif W[rr][cc] == "O":
        return check_move(rr,cc,dr,dc)
    elif W[rr][cc] == ".":
        return True
    else:
        print("ERR")
        return False

def move(D,r,c,dr,dc):
    rr = r+dr
    cc = c+dc
    if D[rr][cc] == ".":
        D[rr][cc] = D[r][c]
    elif D[rr][cc] == "O":
        D = move(D,rr,cc,dr,dc)
        D[rr][cc] = D[r][c]
    D[r][c] = "."
    return D


sr,sc = 0,0
for r in range(R):
    for c in range(C):
        if W[r][c] == "@":
            sr,sc = r,c

r,c = sr, sc

for char in moves:
    dr, dc = dirs[char]
    if check_move(r,c,dr,dc):
        W = move(W,r,c,dr,dc)
        r,c = r+dr, c+dc

ans = 0
for r in range(R):
    for c in range(C):
        if W[r][c] == "O":
            ans += 100*r+c
print(ans)





