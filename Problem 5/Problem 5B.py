def progress(step =1,num = 10):
    for i in range(num):
        print(i*step)
input()
d = input()
n = input()
input()
if (d!='') and (n!=''):
    d = int(d)
    n = int(n)
    progress(d,n)
elif (d!=''):
    d = int(d)
    progress(d)
elif (n!=''):
    n = int(n)
    progress(num=n)
else:
    progress()