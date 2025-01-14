import re

file_path = 'inputs/3.in'
with open(file_path, 'r') as file:
    data = file.readline()
valid_zones = re.findall(r"do\(\)(.*?)don't\(\)", "do()"+data+"don't()")
pattern = r"mul\([0-9][0-9]*[0-9]*,[0-9][0-9]*[0-9]*\)"

p1 = 0
for ins in re.findall(pattern, data):
    s = ins.split(',')
    a = int(s[0][4:])
    b = int(s[1][:-1])
    p1 += a*b

p2 = 0
valids = [re.findall(pattern, zone) for zone in valid_zones]
valids = [item for sublist in valids for item in sublist]
for ins in valids:
    s = ins.split(',')
    a = int(s[0][4:])
    b = int(s[1][:-1])
    p2 += a*b

print(p1)
print(p2)