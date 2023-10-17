y = int(input())
for x in range(y,-1,-1):
    if ((x*x)+x)<=y:
        break
print(x)
