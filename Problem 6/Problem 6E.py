a = int(input())
def bin(x, b =""):
    if x ==0:
        return b
    else:
        b = str(x%2)+b
        x//=2
        return bin(x,b)

if a == 0:
    print(a)
else:
    print(bin(a))