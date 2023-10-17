p = [float(x) for x in input().split()]
q = [int(x) for x in input().split()]
ans = 0
for i in range(len(p)):
    ans += p[i]*q[i]
print(round(ans,2))
