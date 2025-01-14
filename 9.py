from copy import deepcopy
import sys

file_path = 'inputs/9.in'
with open(file_path, 'r') as file:
    inpt = file.readline().strip()

inpt = [int(x) for x in inpt]

def part1(data):
    ans = 0
    pos = 0
    for i,c in enumerate(data):
        if i % 2 == 0:
            for j in range(c):
                ans += (pos+j)*(i//2)
        else:
            for j in range(c):
                if data[-1] == 0:
                    data.pop()
                    data.pop()
                ans += (pos+j)*(len(data)-1)//2
                data[-1] -= 1
        pos += int(c)
    return ans

#Fuck part 2

def clean(data):
    for i in range(len(data)-1):
        if data[i][0] == data[i+1][0]:
            data[i][1] += data[i+1][1]
            del data[i+1]
            return clean(data)
    else:
        if data[-1][0] == ".":
            return data[:-1]
        else:
            return data
    

def compress(data, point):
    moved = True
    for i,x in enumerate(data):
        if x == point:
            j = i
    for i in range(j):  
        if data[i][0] == "." and data[i][1] >= data[j][1]:
            data[j-1][1] += data[j][1] + (data[j+1][1] if j+1 < len(data) else 0)
            data[i][1] -= data[j][1]
            to_move = data[j]
            del data[j]
            if j+1 < len(data):
                del data[j]
            data.insert(i, to_move)  
            data.insert(i, [".",0])
            break
    else:
        moved = False
    return [clean(data), moved]

def clear_last_line():
    sys.stdout.write('\033[F\033[K')
    sys.stdout.flush()

def part2(data):
    new_data = []
    for i,c in enumerate(data):
        if i % 2 == 0:
            new_data.append([str(i//2), c])
        else:
            new_data.append([".", c])
    
    original_data = deepcopy(new_data)

    for i in range(len(new_data)//2):
        if i % 200 == 0:
            clear_last_line()
            print((len(data)-i+1)//200 - 50)
        new_data, moved = compress(new_data, original_data[-2*i-1])

    clear_last_line()
    ans = 0
    pos = 0
    for x in new_data:
        if x[0] != ".":
            for j in range(x[1]):
                ans += (pos+j)*int(x[0])
        pos += x[1]
    return ans

print(part1(inpt.copy()))
print()
print(part2(inpt.copy()))


