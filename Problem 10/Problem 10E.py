def backward(b):
    k=[b[0]]
    for i in range(-1,-len(b),-1):
        k.append(b[i])
    return k
def find_same(a,b):
    count=0
    while 0<1:
        back=backward(b)
        if count==len(a):
            return 'different'
        if a==b or a==back:
            return 'same'
        g=b[0]
        b.remove(g)
        b.append(g)    
        count+=1
         
a=input().split()
b=input().split()
print(find_same(a,b))