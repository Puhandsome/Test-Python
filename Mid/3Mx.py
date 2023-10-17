n = int(input())
m = int(input())
c = 0
for i in range(m):
    for j in range(n):
        print((j+i)%3,end="")