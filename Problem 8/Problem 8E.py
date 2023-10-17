word = (input())
temp = word[0]
count = 0

for letter in word :
    if temp == letter :
        count += 1
    else :
        if count == 1 :
            print(temp,end='')
        else :
            print(str(count)+temp,end='')
        count = 1
        temp = letter

if count == 1 :
    print(temp,end='')
else :
    print(str(count)+temp,end='')
