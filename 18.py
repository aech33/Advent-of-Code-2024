file_path = "inputs/18.in"
with open(file_path, "r") as file:
    D = [line.strip() for line in file.readlines()]

R = 70
C = 70
DIRS = [(0,1),(1,0),(-1,0),(0,-1)]

def search(D):
    Q = [(0,0)]
    DIST = {(0,0):0}
    SEEN = []
    while Q:
        Q = sorted(Q,key=lambda x: DIST[(x[0],x[1])], reverse=True)
        r,c = Q.pop()
        if (r,c) == (R,C):
            break
        if (r,c) in SEEN:
            continue
        SEEN.append((r,c))
        for dr,dc in DIRS:
            rr,cc = r+dr,c+dc
            if 0<=rr<=R and 0<=cc<=C and f"{rr},{cc}" not in D and (rr,cc) not in SEEN:
                if (rr,cc) not in DIST or DIST[(rr,cc)] > DIST[(r,c)]+1:
                    DIST[(rr,cc)] = DIST[(r,c)]+1
                Q.append((rr,cc)) 
    return DIST

low = 1024
high = len(D)

while low <= high:

    mid = low + (high - low) // 2

    DIST = search(D[:mid])

    # If x is greater, ignore left half
    if (R,C) in DIST:
        low = mid + 1

    # If x is smaller, ignore right half
    elif (R,C) not in DIST:
        high = mid - 1

print(search(D[:1024])[(R,C)])
print(D[mid])

