read = open("D:\Python\Problem 12\input.txt","r")
write = open("D:\Python\Problem 12\output.txt","w")
for line in read:
    line = line.capitalize()
    write.write(line)
read.close()
write.close()