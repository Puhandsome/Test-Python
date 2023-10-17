a = float(int(input()))
b = float(int(input()))
c = float(int(input()))
def avg(a=None,b=None,c=None):
    if b == None and c == None:
        return a
    elif c == None:
        return round((a+b)/2,2)
    else:
        return round((a+b+c)/3,2)
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))