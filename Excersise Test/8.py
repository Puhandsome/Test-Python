def down(n):
    if n<0:
        return
    else:
        while n>=0:
            print(n)
            down(n-1)
a = int(input())
down(a)


