dict = {}
while True:
    n = input()
    if n == '$':
        break
    else:
        [x,y] = n.split()
        if x in dict:
            dict[x] += int(y)
        else:
            dict[x] = int(y)
max = max(dict.values())
list = []
for key,value in dict.items():
    if value == max:
        list.append(key)
list.sort()
for i in list:
    print(i)


