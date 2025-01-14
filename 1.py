from collections import Counter

file_path = 'inputs/1.in'

a = []
b = []

with open(file_path, 'r') as file:
    for line in file:
        nums = line.split("   ")
        a.append(int(nums[0]))
        b.append(int(nums[1]))

def part1(a,b):
    ans = 0
    a = sorted(a)
    b = sorted(b)
    for i in range(len(a)):
        ans += abs(a[i] - b[i])  
    print(ans)

def part2(a,b):
    ans = 0
    C = Counter(b)
    for i in range(len(a)):
        ans += C[a[i]] * a[i]
    print(ans)

part1(a,b)
part2(a,b)