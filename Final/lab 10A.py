n = int(input())
lis = []
ans = []
for i in range(n):
    food = input().split()
    lis.append(food)

set1 = set(lis[0])
for i in lis:
    set1 = set1.intersection(set(i))

ans = list(set1)
ans.sort()
if ans == []:
    print("Nothing")
else:
    for i in ans:
        print(i,end=' ')

