Q = {}
G = {}
F = {}

for n in range(0,100001):
    if n<21:
        Q[n] = n+4
    else:
        Q[n] = Q[n-4]+2

for n in range(100000,0,-1):
    if n>= 11240:
        G[n] = Q[n]
    else:
        G[n] = G[n+3]+2

for n in range(120000):
    if n< 43:
        F[n] = G[n+4]
    else:
        F[n] = 2*F[n-2]-F[n-4]+2
print(F[2026])
