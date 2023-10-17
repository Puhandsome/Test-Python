import math
list = []
while True:
    a = input()
    if a == '$':
        break
    else:
        list.append(int(a))

n = len(list)
avg = sum(list)/n
result = 0
for i in range(n):
    sd = ((list[i]-avg)**2)
    result = result + sd

ans = math.sqrt(result/n)
print(round(ans,2))


   
