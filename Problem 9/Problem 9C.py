p = input()
q = input()
count = 0
lis_p = [int(i) for i in p.split()]
lis_q = [int(j) for j in q.split()]
ans = []

for num1 in range(len(lis_q)):
    count = 0
    for num2 in range(len(lis_p)):
        if num1 == 0:
            ans.append(lis_q[num1] * lis_p[num2])
        elif count + num1 == len(ans):
            ans.append( lis_q[num1] * lis_p[num2])
        else:
            ans[count + num1] += lis_q[num1] * lis_p[num2]
            count += 1

for i in ans:
    print(i,end = " ")