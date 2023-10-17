x = float((input()))
y = x
result = ""
result2 = ""
result2_count = 0

if x<0 or x>2**20:
    print("Invalid input")
else:
    while x > 0:
        x = int(x)
        a = x%2
        x = x//2
        result = str(a) + result
    if result == "":
        result = "0"

    x = y
    x = x - int(x)
    while x >= 0 and result2_count < 30:
        x = x * 2
        if x >= 1:
            result2 =result2 + "1"
            x = x - 1
            result2_count += 1
            continue
        else:
            result2 = result2 + "0"
        result2_count += 1

    z = (result+"."+result2)
    print(z)