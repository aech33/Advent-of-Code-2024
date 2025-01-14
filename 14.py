import time

file_path = 'inputs/14.in'
with open(file_path, 'r') as file:
    data = file.readlines()

R = 103
C = 101

D = []
DC = []

for line in data:
  c = int(line.split("=")[1].split(",")[0])
  r = int(line.split("=")[1].split(",")[1][:-2])
  dc, dr = [int(x) for x in line.split("=")[2].split(",")]
  D.append([r,c])
  DC.append((dr,dc))

def print_grid(D):
  for r in range(R):
    for c in range(C):
      if [r,c] in D:
        print("#",end="")
      else:
        print(".",end="")
    print()

def part1(D):
  q1,q2,q3,q4=0,0,0,0
  for r,c in D:
    if c < C//2:
      if r < R//2:
        q1+=1
      elif r>R//2:
        q2+=1
    elif c > C//2:
      if r < R//2:
        q3+=1
      elif r>R//2:
        q4+=1
  return q1*q2*q3*q4

# With some messing around I noticed that the grid would look like some
# super warped christmas tree every 86 iterations, so then I looked exclusively
# at every 86th, until I found the intact tree at 7502.

x = 86
for i in range(1,7503): 
  for j,(r,c) in enumerate(D):
    dr,dc = DC[j]
    r += dr
    c += dc
    if r < 0:
      r += R
    elif r >= R:
      r -= R
    if c < 0:
      c += C
    elif c >= C:
      c -= C
    D[j] = [r,c]
  if i == 100:
    p1 = part1(D)
  if i == x:
    print_grid(D)
    print(i)
    time.sleep(0.1)
    x += 412

print(p1)