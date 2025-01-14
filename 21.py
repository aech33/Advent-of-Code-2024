from itertools import permutations

file_path = "inputs/21.in"
with open(file_path,"r") as file:
    INPUTS = file.read().replace("\n","")

INPUTS = "029A"

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
ARROWS = "^>v<"
NUMPAD = ["789","456","123","#0A"]
ARROW_PAD = ["#^A","<v>"]
PATHS = []

def find_loc(button,pad):
    R = len(pad)
    C = len(pad[0])

    for r in range(R):
        for c in range(C):
            if pad[r][c] == button:
                return (r,c)

# find all paths from (r,c) to (er,ec)
def find_paths(r,c,er,ec,pad):
    R = len(pad)
    C = len(pad[0])

    # config = (r,c,er,ec,pad)
    # if config in PATHS:
    #     return PATHS[config]

    if (r,c) == (er,ec):
        return ["A"]

    P = []
    for i,(dr,dc) in enumerate(DIRS):
        rr = r+dr
        cc = c+dc
        if not(0<=rr<R and 0<=cc<C) or pad[rr][cc] == "#":
            continue

        if abs(er-rr) < abs(er-r) or abs(ec-cc) < abs(ec-c):
            next_paths = find_paths(rr,cc,er,ec,pad)
            for path in next_paths:
                P.append(ARROWS[i]+path)
    return P

def foo(paths,a, pad):
    ans = ""
    R = []
    for path in paths:
        tent_ans = ""
        for next2 in path:
            cr2,cc2 = find_loc(a,pad)
            nr2,nc2 = find_loc(next2,pad)
            paths2 = find_paths(cr2,cc2,nr2,nc2,pad)
            #tent_ans+=min(paths2,key=len)
            R.append(paths2)
            a = next2
        #R.append(tent_ans)
    #ans += min(R,key=len)
    return (a,R)

num_loc = "A"
arr3 = "A"
ans = ""
for next in INPUTS:
    num_loc,step1 = foo(next, num_loc, NUMPAD)
    print(1, step1)
    for a in step1:
        arr1 = "A"
        for b in a:
            arr1, step2 = foo(b, arr1, ARROW_PAD)
            print(2, step2)
            for c in step2:
                arr2 = "A"
                for d in c:
                    arr2, step3 = foo(d,arr2,ARROW_PAD)
                    print(3, step3)
            print()
    print()
    
print(ans)


#v<<A>^>A<A>A<AA>vA^Av<AAA^>A
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#v<A<AA>^>AvA^<A>vA^Av<<A>^>AvA^Av<A^>A<Av<A>^>AAvA^Av<A<A>^>AAA<A>vA^A
#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A