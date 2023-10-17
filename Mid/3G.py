a = int(input())
for i in range(1,a+1):
    for j in range(i+1,a+1):
        for k in range(j+1,a+1):
            print((i,j,k),end="")