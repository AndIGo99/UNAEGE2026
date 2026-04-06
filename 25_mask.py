from fnmatch import *
for N in range(171,10**8,171):
    if fnmatch(str(N),"1*23??56"):
        print(N)

