import os
os.chdir('D:\Python\Problem 12')

x = input('Enter a file name:')
count = 1
try:
    with open(x,'r') as rf_check:
        with open("dict.txt","r") as dic_file:
            list_of_word_check = [w.split() for w in rf_check]
            dic = [d.split() for d in dic_file]
            for i in range(len(list_of_word_check)):
                for j in range(len(list_of_word_check[i])):
                    if list_of_word_check[i][j].upper().strip(",").replace(".","") not in dic[0]:
                        print(f'Line {i+1}: {list_of_word_check[i][j].replace(".","")}')
except FileNotFoundError:
    print("Error: Cannot open the file")