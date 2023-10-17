n = int(input())
m = int(input())
for i in range(1,n+1):
    if i>m:
        break
    else:
        for j in range(i,n+1,m):
            print(j,end=' ')
        print()


    