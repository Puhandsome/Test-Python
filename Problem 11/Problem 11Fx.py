a = float(input())
b = float(input())
c = float(input())
p_max = 0
r_max = 0
for r in range(0,2001):
    r = r/100
    p = (a*r**3)+(b*r**2)+ c*r
    if p>p_max:
        p_max = p
        r_max = r

print(round(float(r_max),2))