def recursive(n,a = 0):
    if n<=0:
        return
    else:
        print(" "*a+'*'*n)
        recursive(n-1,a+1)
def recursive_rows(n,a = 0):
    if n<2:
        return
    else:
        recursive(n,a)
        recursive_rows(n-1,a+1)
a = int(input())
recursive_rows(a)