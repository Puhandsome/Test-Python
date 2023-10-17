n = int(input())
s = 0
result = 0
if -2**40>n>2**40:
    print("Invalid input")
else:
    while n>0:
        s = (n%10)
        n = n//10
        result = result + (s)
    print(result)