list = []
while True:
    n = input()
    if n == '$':
        break
    else:
        list.append(int(n))
average = sum(list)/len(list)
stdev = 0
for x in range(len(list)):
    stdev = stdev + ((list[x] - average)**2)
result = ((stdev/len(list))**(1/2))
print(round(result,2))
    