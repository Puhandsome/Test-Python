n = int(input())
dict = {}
for i in range(n):
    f = input()
    if f in dict:
        dict[f]+=1
    else:
        dict[f]=1

list = [(dict[f],f) for f in dict]
list.sort()
for v,k in list:
    print(k,v)


