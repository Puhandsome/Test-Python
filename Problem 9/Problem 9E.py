from copy import deepcopy

height = int(input())
width = int(input())
grid = []

for _ in range(height):
    row = input()
    grid.append(row)

answer = []
for row in grid:
    answer.append(list(row))

for i in range(height):
    for j in range(width):
        if grid[i][j] == "*":
            continue
        
        mines = 0
        
        for di in (-1,0,1):
            for dj in (-1,0,1):
                if di == 0 and dj == 0:
                    continue

                adj_i = i + di
                adj_j = j + dj

                if 0 <= adj_i < height and 0 <= adj_j < width:
                    if grid[adj_i][adj_j] == "*":
                        mines += 1
        
        answer[i][j] = str(mines)

for row in answer:
    print(''.join(row))
    