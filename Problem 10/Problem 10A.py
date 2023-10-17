n = int(input())
lis = []
answer = []
for i in range(n):
    food = input().split()
    lis.append(food)

compare = set(lis[0])

for i in lis:
    compare = compare.intersection(set(i))

answer = list(compare)
answer.sort()

if answer == []:
    print("Nothing")
else:
    for i in answer:
        print(i,end=' ')
