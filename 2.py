def check_line(levels):
    asc = int(levels[0]) < int(levels[1])
    for i in range(len(levels) - 1):
        if asc and not (-3 <= (int(levels[i]) - int(levels[i+1])) < 0):
            return False
        if not asc and not (0 < (int(levels[i]) - int(levels[i+1])) <=3):
            return False
    else:
        return True

def solve(part1):
    count = 0
    file_path = 'inputs/2.in'
    with open(file_path, 'r') as file:
        for line in file:
            valid = False
            levels = line.split(' ')
            for i in range(len(levels)):
                if part1:
                    valid = check_line(levels)
                    break
                if check_line(levels[:i] + levels[i+1:]):
                    valid = True
                    break
            if valid:
                count += 1
    print(count)
    
solve(True)
solve(False)