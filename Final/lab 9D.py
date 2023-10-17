import math
list = []
while True:
    n = input()
    if n == '$':
        break
    else:
        list.append(int(n))
list.sort()
a = len(list)
if a%2 == 0:
    ans = (list[a//2]+list[((a-1)//2)])/2
elif a%2 == 1:
    ans = list[a//2]
print(ans)
