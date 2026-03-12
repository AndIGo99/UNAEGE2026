def to2(X):
    alf = "0123456789ABCDEF"
    s = ""
    while X > 0:
        s = alf[X%2] +s
        X //= 2
    return s


for N in range(1,1000):
    r  = to2(N)
    if N%6 == 0:
        r += r[-3:]
    else:
        r += to2(N%6*3)
    R = int(r,2)
    if R < 500:
        print(N)
