n = int(input())
n = abs(n)
digits_found = []
result = 0
if 2**40<n<-2**40:
    print("Invalid input")
else:
    while n>0:
        digit = n%10
        if digit not in digits_found:
            digits_found.append(digit)
        n//=10
    result = sum(digits_found)
    print(result)