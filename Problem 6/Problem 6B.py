def recursive(n):
    if n<=0:
        return
    else:
        print(n)
        recursive(n-1)
a = int(input())
recursive(a)