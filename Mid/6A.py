def recursive(a):
    if a == 1:
        print(a)
    else:
        recursive(a-1)
        print(a)

b = int(input())
recursive(b)