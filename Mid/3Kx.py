h = int(input())
m = int(input())
d = int(input())
day = 0
new_m = (m+d)%60
new_h = h + (m+d)//60
day = new_h//24

def zero_num(x):
    if x>10:
        return str(x)
    else:
        return "0"+str(x)

print(zero_num(new_h)+":"+zero_num(new_m))