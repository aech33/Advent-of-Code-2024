from itertools import product

A = 41644071
B = 0
C = 0
i = 0
output = []
PROG = [int(x) for x in "2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0".split(",")]

def combo_op(op):
    if 0 <= op <= 3:
        return op
    elif op == 7:
        print("ERR")
    else:
        return [A,B,C][op-4]

def adv(op):
    global A
    A = A//(2**combo_op(op))

def bxl(op):
    global B
    B = B^op

def bst(op):
    global B
    B = combo_op(op) % 8

def jnz(op):
    global A,i
    if A != 0:
        i = op - 2

def bxc(op):
    global B,C
    B = B^C

def out(op):
    global output
    output.append(combo_op(op)%8)
    if output != PROG[:len(output)]:
        return False
    return True

def bdv(op):
    global A,B
    B = A//(2**combo_op(op))

def cdv(op):
    global A,C
    C = A//(2**combo_op(op))

OPS = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

while i < len(PROG):
    OPS[PROG[i]](PROG[i+1])
    i += 2
print(output)




