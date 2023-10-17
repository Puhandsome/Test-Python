s = 0
while True:
    n = input()
    if n == '$':
        break
    else:
        n = int(n)
        s = s + n
print(s)
