n = int(input())
dict = {}
for i in range(n):
    k = input()
    if k in dict:
        dict[k] +=1
    else:
        dict[k] = 1
key=list(dict.keys())
value=list(dict.values())
key.sort()
value.sort()
for i in value:
    for j in key:
        if dict[j]==i:
            print(j,i)
            key.remove(j)
            break