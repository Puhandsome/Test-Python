import turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
import os
os.chdir('D:\Python\Problem 12')

with open('picture.txt','r') as rf:
    for line in rf:
        line = line.strip()
        if len(line) != 0:
            x,y = (line.split(','))
            t.goto(int(x),int(y))
            t.pendown()
        else:
            t.penup()
            