import math
n = int(input())
list = []
for i in range(n):
    a = input()
    list.append(int(a))

b = len(list)
avg = sum(list)/b
result = 0
for j in range(b):
    sd = ((list[j]-avg)**2)
    result = result + sd
ans = math.sqrt(result/b)
less = avg - ans
greater = avg + ans
list2 = []
for i in range(b):
    if list[i] <less or list[i] >greater:
        continue
    else:
        list2.append(list[i])

c = len(list2)
avg2 = sum(list2)/c
print(round(avg2,2))

