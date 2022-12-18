data = open("day_17/data.txt", "r").read()

shape_data = open("day_17/shape.txt", "r").read().split("\n\n")
shape_data = [[list(j) for j in i.split("\n")] for i in shape_data]

def affiche_grid(grid):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    # print(string, "\n")
    return string



print(data)

cave = []
for shape in shape_data:
    cave = shape + cave
    
    shape_coord = []
    for i, line in enumerate(shape):
        for j, char in enumerate(line):
            if char == "@":
                shape_coord.append((j, i))

    test = True
    for x, y in shape_coord:
        if shape[y+1][x] == "#":
            test = False
    
    print(shape_coord)
    while len(cave) > len(shape)-3 and not cave[len(shape)-3].__contains__("#"):
        for coord in shape_coord:
            x = coord[0]
            y = coord[1]
            cave[y][x] = "."
        for coord in shape_coord:
            x = coord[0]
            y = coord[1]
            cave[y+1][x] = "@"
        
        print(affiche_grid(cave))
        cave.pop(0)
    
    for coord in shape_coord:
            x = coord[0]
            y = coord[1]
            cave[y][x] = "#"
        
    print(affiche_grid(cave))
    
    # j'ai besoin des coordonnée pour trouver de chaque shape dans le tableau et de les faire bouger en bas ou en 
    # fonction des inputs, et chaque fois si la ligne au top est  empy je l'a suprime
    
    
    
    
    
    
    # print(len(cave)-3)
    # print(cave[len(cave)-3])
    # # for
    # while "@" in cave[len(cave)-3]:

    #     if ["......."] in shape:
    #         del cave[len(cave)-3]

    # print(affiche_grid(shape))
print(affiche_grid(cave))


