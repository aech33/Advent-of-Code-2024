import re

file_path = 'inputs/5.in'
with open(file_path, 'r') as file:
    rules, updates = file.read().split("\n\n")

rules = rules.split("\n")
updates = updates.split("\n")

def solve(nums):
    sol = [nums[0]]
    for i in range(1,len(nums)):
        for j in range(len(sol)):
            if nums[i] + "|" + sol[j] in rules:
                sol.insert(j, nums[i])
                break
        else:
            sol.append(nums[i])
        
    return sol

part1,part2 = 0,0
for line in updates:
    updts = line.split(",")
    valid = True
    for i in range(len(updts)): 
        for j in updts[i+1:]:
            if updts[i] + "|" + j in rules:
                continue
            else:
                valid = False
    if valid:
        part1 += int(updts[len(updts)//2])
    else:
        part2 += int(solve(updts)[len(updts)//2])

print(part1)
print(part2)