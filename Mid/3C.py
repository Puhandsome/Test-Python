w = int(input())
h = int(input())
c = 0
for i in range(h):
    for j in range(w):
        print((c+1)%3,end="")
    print()

    
