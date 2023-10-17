import math

n = int(input())

min_x = math.inf
max_x = -math.inf
min_y = math.inf
max_y = -math.inf

for i in range(n):
    input_ = input()
    x, y = input_.split()
    x = int(x)
    y = int(y)

    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

width = max_x - min_x
height = max_y - min_y
side = max(width, height)
print(side ** 2)