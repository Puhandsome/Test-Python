n = int(input())
k = int(input())
s = ""
hex_digits = "0123456789ABCDEF"
if n < 0 or n > 1000000000 or k < 1 or k > 10:
    print("Invalid input")
else:
    while n > 0:
        remainder = n % 16
        s = hex_digits[remainder] + s
        n = n // 16

    if k > len(s):
        print(0)
    else:
        print(s[-k])
