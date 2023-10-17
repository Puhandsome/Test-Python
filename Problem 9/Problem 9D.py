list = []
while True:
    n = input()
    if n == '$':
        break
    else:
        list.append(int(n))

list.sort()
a = len(list)
if a%2==0:
    median = (((list[a//2])+list[a//3])/2)
elif a%2==1:
    median = (list[a//2])

print(float(median))





