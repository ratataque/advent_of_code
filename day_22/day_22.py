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
                return (x, y)
        else:
            x -= dx
            y -= dy
            orix = x
            oriy = y
            while (0 <= y < len(grid)) and (0 <= x < len(grid[y])) and grid[y][x] != " ":
                x -= dx
                y -= dy
            x += dx
            y += dy
            if grid[y][x] == "#":
                return (orix, oriy)
            
    return (x, y)

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
            start = go_forward(start, grid, dir, int(q))
            if count < 5000000000:
                print(start)
            dir = rotate(dir, l)
            q = ""
            count += 1
    start = go_forward(start, grid, dir, int(q))
    print(start)
    print(1000*(start[1]+1) + 4*(start[0]+1) + directions[dir])
    

    
if __name__ == "__main__":
    # print(grid)
    
    start = start_pos(grid)
    
    part_1(grid, start)
    
    # affiche_grid(grid)
    # print(data)