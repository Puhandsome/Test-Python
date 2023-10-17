sum = 0
while True:
    n = input()
    if n =='$':
        break
    else:
        n = int(n)
        if n%2==0 and n<=10:
            sum+=n
print(sum)      
