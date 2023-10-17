a = int(input())
s = ""
if a<0:
    print("Invalid input")
elif a ==0:
    print("0")
else:
    while a>0:
        s = str(a%2) +s
        a = a//2
    print(s)