import copy

data = open("day_23/data.txt", "r").read().split("\n")
empty_grid_ = [["." for __ in range(300)] for _ in range(200)]

def affiche_grid(grid: list):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string
    

def get_pos(grid: list):
    pos_lutin = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                pos_lutin.append([x, y])
    return pos_lutin


def move_lutin(grid: list, new_lutin_pos: list):
    empty_grid = copy.deepcopy(grid)
    for lutin in new_lutin_pos:
        x, y = lutin
        empty_grid[y][x] = "#"  
    
    return empty_grid

def separate(pos_lutin: list, grid: list, round: int):
    direction = ["N", "S", "W", "E"]
    dir = {"N": (0, -1), "NE": (1, -1), "NW": (-1, -1), "S": (0, 1), "SE": (1, 1), "SW": (-1, 1), "W": (-1, 0), "E": (1, 0)}
    
    for round in range(round):
        new_lutin_pos = []
        for pos, lutin in enumerate(pos_lutin):
            x, y = lutin
            
            no_need_move = True
            for j, po in enumerate(grid[y-1:y+2]):
                for i,p in enumerate(po[x-1:x+2]):
                    if (i!=1 or j!=1) and p == "#" and no_need_move:
                        for i_d, di in enumerate(direction):
                            x_base , y_base = x+dir[di][0], y+dir[di][1]        
                            can_move = True
                            if grid[y_base][x_base] == "#":
                                can_move = False
                            a = ["N", "S"]
                            b = ["W", "E"]
                            if di in a:
                                z = b
                            else:
                                z = a
                            for d in z:
                                if z == b:
                                    nx , ny = x+dir[di+d][0], y+dir[di+d][1]
                                else:
                                    nx , ny = x+dir[d+di][0], y+dir[d+di][1]

                                if grid[ny][nx] == "#":
                                    can_move = False
                            if can_move:
                                no_need_move = False
                                if [x_base, y_base] not in new_lutin_pos:
                                    new_lutin_pos.append([x_base, y_base])
                                else:
                                    index = new_lutin_pos.index([x_base, y_base])
                                    new_lutin_pos.remove([x_base, y_base])
                                    new_lutin_pos.insert(index, pos_lutin[index])
                                    new_lutin_pos.append(lutin)
                                break
                        break
                    else:
                        continue
                    
            if no_need_move:
                new_lutin_pos.append(lutin)
                
                
        grid = move_lutin(empty_grid_, new_lutin_pos)
            
        if new_lutin_pos == pos_lutin:
            return (grid, pos_lutin, round+1)
        
        pos_lutin = new_lutin_pos
        # affiche_grid(grid)
        zob = direction.pop(0)
        direction.append(zob)
        
    return (grid, pos_lutin, round+1)                      

def part_1(data: list):
    
    #Part1 grid, pos_lutin, round = separate(get_pos(data), data, 10)
    grid, pos_lutin, round = separate(get_pos(data), data, 100000000000) # Part 2
    affiche_grid(grid)
    
    
    x = []
    y = []
    for lutin in pos_lutin:
        x.append(lutin[0])
        y.append(lutin[1])
        
    min_x = min(x)
    min_y = min(y)
    max_x = max(x)
    max_y = max(y)
    
    empty_tile = 0
    rect = []
    count = 0
    for i in range(min_y, max_y+1, 1):
        rect.append([])
        for j in range(min_x, max_x+1, 1):
            rect[count].append(grid[i][j])
            if grid[i][j] == ".":
                empty_tile += 1
        count+=1
    # print(rect)
    affiche_grid(rect)
    print(min_x,min_y, max_x, max_y)
    print("Resulta: ", empty_tile, "round: ", round)    
    


if __name__ == '__main__':
    affiche_grid(data)
    # affiche_grid(empty_grid)
    # separate(get_pos(data), data)
    
    part_1(data)
    
    
    