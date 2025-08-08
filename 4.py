with open('inputs/4.in', 'r') as file:
    grid = [line.strip() for line in file]

R = len(grid)
C = len(grid[0])

DIRS = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

def part1(r, c):
    if grid[r][c] != "X": return 0
    return sum(
        all(0 <= r+i*dr < R and 0 <= c+i*dc < C and grid[r+i*dr][c+i*dc] == ch
            for i, ch in enumerate("XMAS"))
        for dr, dc in DIRS
    )

def part2(r,c):
    if not (grid[r][c] == "A" and 1<=r<R-1 and 1<=c<C-1):
        return 0
    l_diag = set([grid[r-1][c-1],grid[r+1][c+1]])
    r_diag = set([grid[r-1][c+1],grid[r+1][c-1]])
    return l_diag == r_diag == set(["S","M"])

p1 = sum(part1(r, c) for r in range(R) for c in range(C))
p2 = sum(part2(r, c) for r in range(R) for c in range(C))

print(p1)
print(p2)

