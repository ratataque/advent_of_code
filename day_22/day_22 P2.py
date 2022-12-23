data = open("day_22/data.txt", "r").read().split("\n\n")
grid = [list(i) for i in data[0].split("\n")]
data = data[1]

def affiche_grid(grid: list):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string


def start_pos(grid: list):
    for x, case in enumerate(grid[0]):
        if case == ".":
            return (x, 0)

def go_forward(start: tuple, grid: list, direction: tuple, step: int):
    x, y  = start
    dx, dy = direction
    for i in range(step):
        x += dx
        y += dy
        if ((0 <= y < len(grid)) and (0 <= x < len(grid[y]))) and grid[y][x] != " ":
            if grid[y][x] == "#":
                x -= dx
                y -= dy
                return ((x, y), (dx, dy))
        else:
            x -= dx
            y -= dy
            orix = x
            oriy = y
            if 50 <= x <= 99 and y == 0:
                y = x + 100
                x = 0
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "R")
            
            elif 100 <= x <= 149 and y == 0:
                x -= 100
                y = 199
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                
            elif x == 149 and 0 <= y <= 49:
                x -= 50
                y = 149 - y
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(rotate(direction, "R"), "R")
                
            elif 100 <= x <= 149 and y == 49:
                y = x - 50
                x = 99
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "R")

            elif 50 <= y <= 99 and x == 99:
                x = y + 50
                y = 49
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "L")
                
            elif x == 99 and 100 <= y <= 149:
                x += 50
                y = 149 - y
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(rotate(direction, "R"), "R")
                
            elif 50 <= x <= 99 and y == 149:
                y = x + 100
                x = 49
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "R")
                
            elif 150 <= y <= 199 and x == 49:
                x = y - 100
                y = 149
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "L")
                
            elif 0 <= x <= 49 and y == 199:
                x += 100
                y = 0
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                
            elif 150 <= y <= 199 and x == 0:
                x = y - 100
                y = 0
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "L")
                
            elif 100 <= y <= 149 and x == 0:
                x = 50
                y = 149 - y
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(rotate(direction, "R"), "R")
                
            elif 0 <= x <= 49 and y == 100:
                y = x + 50
                x = 50
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "R")
                
            elif 50 <= y <= 99 and x == 50:
                x = y - 50
                y = 100
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(direction, "L")
                
            elif 0 <= y <= 49 and x == 50:
                x = 0
                y = 149 - y
                if grid[y][x] == "#":                
                    return ((orix, oriy), (dx, dy))
                dx, dy = rotate(rotate(direction, "R"), "R")
                
    return ((x, y), (dx, dy))

def rotate(prev_direction: tuple, turn: str):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    dir = directions.index(prev_direction)
    if turn == "R":
        return directions[(dir+1)%4]
    else:
        return directions[(dir-1)%4]
    

def part_1(grid: list, start: tuple):
    directions = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
    
    
    q = ""
    dir = (1, 0)
    count = 0
    for l in data:
        if l.isnumeric():
            q += l
        else:
            a = go_forward(start, grid, dir, int(q))
            print(a)
            start, dir = a[0], a[1]
            if count < 200:
                print(start)
            dir = rotate(dir, l)
            q = ""
            count += 1
    start = go_forward(start, grid, dir, int(q))[0]
    print(start)
    print(1000*(start[1]+1) + 4*(start[0]+1) + directions[dir])
    

    
if __name__ == "__main__":
    # print(grid)
    
    start = start_pos(grid)
    
    part_1(grid, start)
    
    # affiche_grid(grid)
    # print(data)