a = int(input())
s = 0
result = 0
if a>-2**40 and a<2**40:
    while a>0:
        s = a%10
        a = a//10
        result = result +s
    print(result)
else:
    print('Invalid input')
