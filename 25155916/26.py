f = [s for s in open("26_3.txt")]
count = int(f[0])
f.remove(f[0])
arr1 = []
arr2 = []
arr3 = []
arr4_1 = []
arr4_2 = []

for s in f:
    a,b = [int(x) for x in s.split()]
    arr1.append(a)
    arr2.append(b)
    arr3.append(a)
    arr3.append(b)

arr3 =  sorted(arr3)
arr5 = []
for x in arr3:
    if x in arr1 and arr1.index(x)+1 not in arr4_2:
        arr4_1.append(arr1.index(x)+1)
        arr5.append(arr1.index(x)+1)
    elif x in arr2 and arr2.index(x)+1 not in arr4_1:
        arr4_2.append(arr2.index(x)+1)
        arr5.append(arr2.index(x)+1)
print(arr5[-1])
arr4 = arr4_1+arr4_2[::-1]
print(966-arr4.index(arr5[-1])-1)
