import numpy as np

file_path = 'inputs/13.in'
with open(file_path, 'r') as file:
    data = file.readlines()

D = []
for i in range(0,len(data),4):
    ax,ay = data[i][10:].split(", ")
    bx,by = data[i+1][10:].split(", ")
    X,Y = data[i+2 ][7:].split(", ")
    D.append([int(x[2:]) for x in [ax,ay,bx,by,X,Y]])

def solve(ax,ay,bx,by,X,Y):
    A = np.array([[ax,bx],[ay,by]])
    B = np.array([X,Y])
    intersection = np.linalg.solve(A,B)

    m = intersection[0].item() # num of A presses
    n = intersection[1].item() # num of B presses
    t = 1e-4

    if m-t < round(m) < m+t and n-t < round(n) < n+t:
        return 3*round(m)+round(n)
    return 0

p1, p2 = 0, 0
for i in range(len(D)):
    ax,ay,bx,by,X,Y = D[i]
    offset = 10000000000000
    p1 += solve(ax,ay,bx,by,X,Y)
    p2 += solve(ax,ay,bx,by,X+offset,Y+offset)

print(p1)
print(p2)