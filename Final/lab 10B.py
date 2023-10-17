n = int(input())
dict = {}
for i in range(n):
    x = input()
    if x not in dict:
        dict[x] = 1
    else:
        dict[x]+=1

ans = [(dict[x],x) for x in dict]
ans.sort()

for (v,k) in ans:
    print(k,v)


