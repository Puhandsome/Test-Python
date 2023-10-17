s = 0
x = input()
if x == '$':
    print("None")
else:
    s = x
while True:
    n = input()
    if n == '$':
        break
    else:
        n = int(n)
        s = int(s)
        if n <= s:
            s = n
        else:
            continue
if s<0:
    print("None")
else:
    print(s)
            