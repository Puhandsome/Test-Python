def recursive(n):
    if n<=0:
        return
    else:
        recursive(n-1)
        print(n)
a = int(input())
recursive(a)