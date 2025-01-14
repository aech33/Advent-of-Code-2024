data = "28591 78 0 3159881 4254 524155 598 1"

M = {}
def blink(x, n):
    if (x,n) in M:
        return M[(x,n)]
    if n == 0:
        res = 1
    elif x == 0:
        res = blink(1, n-1)
    elif len(str(x))%2 == 0:
        strx = str(x)
        mid = len(strx)//2
        l = int(strx[:mid])
        r = int(strx[mid:])
        res = blink(l, n-1) + blink(r, n-1)
    else:
        res = blink(x*2024, n-1)
    M[(x,n)] = res
    return res


data = [int(d) for d in data.split()]
p1, p2 = 0, 0

for stone in data:
    p1 += blink(stone, 25)
    p2 += blink(stone, 75)

print(p1)
print(p2)