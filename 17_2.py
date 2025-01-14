inp = "2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0"
PROG = [int(x) for x in inp.split(",")]

def bin_to_int(X):
    return int("".join(map(str, X)),2)

def pad(X):
    while len(X) < 3:
        X.insert(0,0)
    return X

def search(INIT):
    if (len(INIT)-8)//3 == len(PROG):
        print(bin_to_int(INIT[8:]))
        quit()

    for B in range(8):
        bits = pad([int(x) for x in bin(B)[2:]])
        POSS_INIT = INIT+bits
        L = len(POSS_INIT)

        B = B^2
        C = bin_to_int(POSS_INIT[L-B-3:L-B])
        B = B^7
        B = B^C

        i = (len(INIT)-8)//3
        if PROG[-i-1] == B:
            search(POSS_INIT)

search([0,0,0,0,0,0,0,0])