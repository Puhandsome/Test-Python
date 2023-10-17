count = 0
i = 0
max_l = 0
while True:
    n = input()
    if n == '$':
        break
    
    else:
        n = int(n)
        if i == 0:
            same = n
            count = 1
            i = 1
        else:
            if n == same:
                count += 1
            else:
                count = 1
            if count > max_l:
                max_l = count
            same = n

print(max_l)