n = int(input())
s = ""
if n<0 or n>2**20:
    print ("Invalid input")
else:
    if n == 0:
        print ("0")
    else:
        while n>=1:
            s = str(n%2) + s
            n = n//2
        print(s)