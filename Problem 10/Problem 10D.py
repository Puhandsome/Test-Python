i=0
max=0
count=0
while 0<1:
    a=input()
    if a=='$':
        break
    else:
        a=int(a)
        if i==0:
            same=a
            count=1
        else:
            if a==same:
                count+=1
            else:
                if count>max:
                    max=count
                same=a
                count=1
    i+=1       
if count>max:
        max=count 
print(max)