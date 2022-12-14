import json

data = open("day_14/data.txt", "r").read().split("\n") 
data = [i.split("->") for i in data]
# coord = [[(int(j.split(",")[0]), int(j.split(",")[1])) for j in i] for i in data]

def affiche_grid(grid):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    # print(string, "\n")
    return string

def create_grid(data):
    min = [0, 0]
    max = [1000, 0]
    for line in data:
        for i, pair in enumerate(line):
            pair = (int(pair.split(",")[0]), int(pair.split(",")[1]))
            
            min[0] = pair[0] if pair[0] < min[0] else min[0]
            max[0] = pair[0] if pair[0] > max[0] else max[0]
            max[1] = pair[1] if pair[1] > max[1] else max[1]

            line[i] = pair

    grid = [["."for i in range(0, max[0]-min[0]+1)] for j in range(0, max[1]-min[1]+1)]
    grid.append(["." for i in range(0, max[0]-min[0]+1)])
    grid.append(["#" for i in range(0, max[0]-min[0]+1)])
    grid[0][500 - min[0]] = "+"

    return [grid, min, max]

def create_cave(data, grid, min, max):
    for i, row in enumerate(data):
        line = []
        for j, column in enumerate(row):
            if j == 0:
                continue
            
            # print(column)
            prevx = row[j-1][0] - min[0]
            prevy = row[j-1][1] - min[1]
            
            x = column[0] - min[0]
            y = column[1] - min[1]

            diffx = x-prevx
            diffy = y-prevy

            pacex = 1 if diffx > 0 else -1 
            pacey = 1 if diffy > 0 else -1 
            
            for v in range(0, diffx+pacex, pacex):
                # print(v)
                grid[y][prevx+v] = "#"
                
                # affiche_grid(grid)
                
            for w in range(0, diffy+pacey, pacey):
                grid[prevy+w][x] = "#"
                
                # affiche_grid(grid)
    return grid
        
def breadth_first_search(grid, start):
    directions = [(0, 1), (-1, 1), (1, 1)]
    
    sand = 0

    queue = []
    queue.append(start)

    while queue:

        vertex = queue.pop(0)

        x, y = vertex[0],vertex[1]
        origin = grid[y][x]

        for index, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            dessous = (x+directions[0][0], y+directions[0][1])
            neighbor = (nx, ny)
            # check = grid[ny][nx]
            if (0 <= nx < len(grid[y]) and
                0 <= ny < len(grid)):
                
                check = grid[ny][nx]
                
                if grid[dessous[1]][dessous[0]] == ".":
                    queue.append(dessous)
                    break
                else:
                    if check in ["#", "O"]:                        
                        if index == 2:
                            grid[y][x] = "O"
                            # affiche_grid(grid)
                            queue.append(start)
                            sand += 1
                            
                            if vertex == start:
                                return sand
                            
                    else:
                        queue.append(neighbor)
                        break
                        
            else:
                break

    return sand


# print(data)

l = create_grid(data)
grid = l[0]
min = l[1]
max = l[2]

print(min, max)

grid = create_cave(data, grid, min, max)

print(breadth_first_search(grid, (500- min[0], 0)))

open("day_14/demo.txt", "w").write(affiche_grid(grid))
