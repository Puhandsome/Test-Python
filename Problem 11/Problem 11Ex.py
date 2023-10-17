dict = {}
while True:
    a = input()
    if a == '$':
        break
    else:
        [x,y] = a.split()
        if x in dict:
           dict[x] += int(y)
        else:
            dict[x] = int(y)
max = max(dict.values())
list = []
for key,value in dict.items():
    if value == max:
        list.append(key)
    else:
        continue
list.sort()
for i in list:
    print(i)
    


       

        


