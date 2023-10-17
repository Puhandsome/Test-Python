p = [float(x)for x in input().split()]
q = [int(x) for x in input().split()]
result = 0
for i in range (len(p)):
    result += p[i]*q[i]

print(round(result,2))