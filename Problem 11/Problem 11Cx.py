import math
list = []
n = int(input())
for i in range(n):
    x = input()
    list.append(int(x))

avg = sum(list)/n
stdev = 0
for j in range(len(list)):
    stdev = stdev + (((list[j]-avg)**2)/n)
    result = math.sqrt(stdev)
a = round((avg - result),2)
b = round((avg + result),2)
list2 = []
for k in range(len(list)):
    if list[k]<a or list[k]>b:
        continue
    else:
        list2.append(list[k])
avg2 = sum(list2)/len(list2)
print(round(avg2,2))





