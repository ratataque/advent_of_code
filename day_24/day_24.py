import copy

data = open("day_24/data.txt", "r").read().split("\n")

empty_grid = [list(data[0])]
for j in range(len(data)-2):
    line = []
    for i in range(len(data[0])):
        if i == 0 or i == len(data[0])-1:
            line.append("#")
        else:
            line.append(".")
    empty_grid.append(line)
empty_grid.append(list(data[len(data)-1]))

grid = [list(i) for i in data]


def affiche_grid(grid: list):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string
    
    
def get_bliz_coord(grid: list):
    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    
    blizz_coord = []
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell in direction:
                blizz_coord.append([x, y, cell])
    
    return blizz_coord
    

def move_blizard(empty_grid: list, blizz_coord: list):
    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    
    new_grid = copy.deepcopy(empty_grid)
    
    for i, bliz in enumerate(blizz_coord):
        x, y, d = bliz
        dx, dy = direction[d]
        mx ,my = (x+dx), (y+dy)

        mx = mx if mx != 0 else len(new_grid[y])-2
        mx = mx if mx != len(new_grid[y])-1 else 1
        
        my = my if my != 0 else len(new_grid)-2
        my = my if my != len(new_grid)-1 else 1

        new_grid[my][mx] = d
        blizz_coord[i] = [mx, my, d]
    
    affiche_grid(new_grid)
    
    return blizz_coord

def bfs(start: tuple, end: tuple, grid: list, blizz_coord: list):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    pre_queue = []
    pre_queue.append(start)
    
    queue = []
    queue.extend(pre_queue)
    
    visited = []
    
    minute = 0
    while pre_queue:
        while queue:
            
            x, y = queue.pop(0)
            
            if (x, y) == end:
                return minute
            
            visited.append((x, y))
                        
            for dir in directions:
                dx, dy = dir
                mx ,my = x+dx, y+dy
                
                if ((1 <= mx < len(grid[y])-1) and 
                    (1 <= my < len(grid)-1) and
                    (mx, my) not in visited and
                    (mx, my) not in blizz_coord):
                    
                    grid[y][x] = "E"
                    pre_queue.append((x, y))
        
        
        
        
    return grid
        




    
if __name__ == "__main__":
    affiche_grid(grid)
 
    
    blizz_coord = get_bliz_coord(grid)
    
    for i in range(18):
        blizz_coord = move_blizard(empty_grid, blizz_coord)