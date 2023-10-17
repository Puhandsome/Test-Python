import os
os.chdir('D:\Python\Problem 12')


try:
    x = input()
    with open(x,"r") as rf:
        print(rf.read())

except FileNotFoundError:
    print("ERROR: File not found ")