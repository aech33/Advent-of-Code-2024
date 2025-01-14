import copy

file_path = 'inputs/6.in'
with open(file_path, 'r') as file:
    matrix = [list(line.strip()) for line in file.readlines()]

R, C = 0, 0
P1 = set()
P2 = set()
height = len(matrix)
width = len(matrix[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r in range(height):
    for c in range(width):
        if matrix[r][c] == "^":
            sr,sc = r,c

def check_path(M):
    r,c,d = sr,sc,0
    SEEN = set()
    while True:
        if (r, c, d) in SEEN:
            return True 
        SEEN.add((r, c, d))
        rr = r + dirs[d][0]
        cc = c + dirs[d][1]
        if not(0<=rr<height and 0<=cc<width):
            return False
        if M[rr][cc] == "#":
            d = (d+1)%4
        else:
            r = rr
            c = cc

r = sr
c = sc
d = 0

while True:
    rr = r + dirs[d][0]
    cc = c + dirs[d][1]
    if not(0<=rr<height and 0<=cc<width):
        break
    if matrix[rr][cc] == "#":
        d = (d+1)%4
    else:
        r = rr
        c = cc
        P1.add((r, c, d))
    
for r,c,d in P1:
    matrix_2 = copy.deepcopy(matrix)
    if matrix[r][c] == "." and (r,c) not in P2 and matrix[r][c] != "^":
        matrix_2[r][c] = "#"
        if check_path(matrix_2):
            P2.add((r,c))

print(len(set([(r,c) for (r,c,d) in P1])))
print(len(P2))
