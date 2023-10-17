list = []
while True:
    n = input()
    if n == '$':
        break
    else:
        list.append(int(n))

list2 = []
ans = 0
if len(list)>1:
    if list[0]>0:
        a=list[0]+list[1]
        list2.append(a)
        for i in range(len(list)-2):
            a = a + list[i+2]
            list2.append(a)
    if list[0]<0:
        a = list[0]
        list2.append(a)
        for j in range(len(list)-1):
            a = a + list[j+1]
            list2.append(a)
elif len(list)==1:
    a = list[0]
    list2.append(a)

ans = min(list2)
if ans>=0:
    print(0)
else:
    ans = -ans
    print(ans)







    
    



