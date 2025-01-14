import re

file_path = 'inputs/4.in'
with open(file_path, 'r') as file:
    horz = [line.strip() for line in file]

pattern = r"(?=(XMAS|SAMX))"
pattern2 = r"(?=(MAS|SAM))"

vert = "O".join(["".join(list(row)) for row in zip(*horz)][::-1])

def rotate_45(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_dim = rows + cols - 1  # Total number of diagonals
    diagonals = ["" for _ in range(max_dim)]
    
    # Group elements into diagonals
    for i in range(rows):
        for j in range(cols):
            diagonals[i + j] += (matrix[i][j])
    
    # Pad diagonals to form the rotated matrix
    rotated = []
    for i, diagonal in enumerate(diagonals):
        padding = max_dim - len(diagonal) if i < len(diagonals) // 2 else i - len(diagonals) // 2
        rotated.append("O" * padding + diagonal)
    
    return rotated

def rotate_45_counterclockwise(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_dim = rows + cols - 1  # Total number of diagonals
    diagonals = ["" for _ in range(max_dim)]
    
    # Group elements into diagonals (counterclockwise logic)
    for i in range(rows):
        for j in range(cols):
            diagonals[j - i + (rows - 1)]+=matrix[i][j]
    
    # Align diagonals to form the rotated matrix
    rotated = []
    for i, diagonal in enumerate(diagonals):
        padding = (len(diagonals) - 1 - i) if i < len(diagonals) // 2 else i - (len(diagonals) // 2)
        rotated.append("O" * padding + diagonal)
    
    return rotated

def get_matches(patt, text):
    return len([match.group(1) for match in re.finditer(patt, text)])

angle = "O".join(rotate_45(horz)[3:-3])
angle2 = "O".join(rotate_45_counterclockwise(horz)[3:-3])

print(get_matches(pattern, "O".join(horz)) + get_matches(pattern, angle) + get_matches(pattern, vert) + get_matches(pattern, angle2))

def part2(data):
    count = 0
    for r in range(1, len(data)-1):
        for c in range(1,len(data)-1):
            if data[r][c] == "A":
                l_diag = set([data[r-1][c-1],data[r+1][c+1]])
                r_diag = set([data[r-1][c+1],data[r+1][c-1]])
                if l_diag == set(["S","M"]) and r_diag == set(["S","M"]):
                    count += 1
    return count

print(part2(horz))

