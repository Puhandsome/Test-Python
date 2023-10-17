x = int(input())
y = int(input())
z = int(input())
print(min(x,y,z))
def min(x,y,z):
    if x>y or x>z:
        result = x
    elif y>x or y>z:
        result = y
    elif z>x or z>y:
        result = z
    return result