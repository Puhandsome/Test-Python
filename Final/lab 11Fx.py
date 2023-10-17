a = int(input())
b = int(input())
c = int(input())
max_p = 0
max_r = 0
for r in range(0,2001):
    r = r/100
    p = a*(r**3)+b*(r**2)+(c*r)
    if p>max_p:
        max_p = p
        max_r = r
print(float(round(max_r,2)))
    
