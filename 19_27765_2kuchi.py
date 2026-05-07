def f(s1,s2,i):
    if i == 0:
        if s1+s2<69 and (s1*2+s2 >= 69 or s1+s2*3>=69):
            return True
        else:
            return False
    else:
        if f(s1+1,s2,i-1) or  f(s1,s2+1,i-1) or f(s1*2,s2,i-1) or f(s1,s2*3,i-1):
            return True
        else:
            return False

for s2 in range(1,68):
    if f(10,s2,1):
        print(s2)
