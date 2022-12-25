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
empty_grid.append(list(data[0]))

grid = [list(i) for i in data]


def affiche_grid(grid: list):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string
    
    
def get_bliz_coord(grid: list):
    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    new_grid = copy.deepcopy(grid) 
    
    blizz_coord = []
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell in direction:
                blizz_coord.append([x, y])
    
    return blizz_coord
    

def move_blizard(empty_grid: list, blizz_coord: list):
    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    for bliz in blizz_coord:
        x, y = bliz
        dx, dy = 
    
if __name__ == "__main__":
    affiche_grid(grid)
 
    
    blizz_coord = get_bliz_coord(grid)
    
    move_blizard(empty_grid, blizz_coord)