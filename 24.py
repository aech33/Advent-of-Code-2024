import operator,time

file_path = "inputs/24.in"
with open(file_path, "r") as file:
    init, gates = file.read().split("\n\n")

def calc_bin(x):
    Z = []
    for wire in D:
        if wire[0] == x:
            Z.append(wire)
    ans = 0
    for i,z in enumerate(sorted(Z, key=lambda x : int(x[1:]))):
        ans += 2**(i)*D[z]
    return ans

D = {}
for i in init.split("\n"):
    wire, value = i.strip().split(" ")
    D[wire[:-1]] = int(value)


GATES = {"AND":operator.and_, 
         "OR":operator.or_, 
         "XOR":operator.xor}

LINKS = {}
OPS = gates.split("\n")
while OPS:
    line = OPS.pop()
    a,gate,b,_,c = line.split(" ")
    if c not in LINKS:
        LINKS[c] = [a,b]
    else:
        LINKS[c] += [a,b]
    if a in D and b in D:
        D[c] = GATES[gate](D[a],D[b])
    else:
        OPS.insert(0,line)

print(calc_bin("z"))

# Part 2 Beginnings:

def trace(wire,S):
    if wire in LINKS:
        S = []
        for w in LINKS[wire]:
            if w[0] not in "xyz" and w not in S:
                S += trace(w,S+[w])
        return S
    return []

# to_change = set()
# for i in range(46):
#     to_change.update(trace("z" + str(i).zfill(2),[]))


