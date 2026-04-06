f = [x for x in open("9.txt")]

count = 0
for s in f:
    arr = [int(x) for x  in s.split()]
    arr_n = [x for x in arr if arr.count(x) == 1]
    arr_2 = [x for x in arr if arr.count(x) == 2]
    if len(arr_n) == 3 and len(arr_2) == 4 and min(arr_2) > min(arr_n):
        count += 1
print(count)



