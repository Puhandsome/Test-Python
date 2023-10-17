list = []
while True:
    n = input()
    if n == '$':
        break
    else:
        list.append(int(n))

ans = []
if len(list) == 1:
    ans.append(list[0])
elif len(list)>1:
    s = list[0] + list[1]
    ans.append(list[0])
    ans.append(s)
    for i in range(2,len(list)):
        s = s + list[i]
        ans.append(s)
if min(ans)<0:
    print(abs(min(ans)))
else:
    print(0)



        
    
            
            
    
        
    

