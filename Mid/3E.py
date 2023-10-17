max = 0
min = 0
while True:
    n = input()
    if n == '$':
        break
    n = int(n)
    if n>=max:
        max = n
    elif n<=min:
        min = n
if min == 0:
    print(max)
    print(max)
elif max ==0:
    print(min)
    print(min)
else:
    print(min)
    print(max)