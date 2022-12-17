data = open("day_17/data.txt", "r").read()

shape_data = open("day_17/shape.txt", "r").read().split("\n\n")
shape_data = [[[j] for j in i.split("\n")] for i in shape_data]

def affiche_grid(grid):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    # print(string, "\n")
    return string



print(data)

cave = []
for shape in shape_data:
    cave = cave + shape
    
    
    
    # j'ai besoin des coordonnée pour trouver de chaque shape dans le tableau et de les faire bouger en bas ou en 
    # fonction des inputs, et chaque fois si la ligne au top est  empy je l'a suprime
    
    
    
    
    
    
    print(len(cave)-3)
    print(cave[len(cave)-3])
    # for
    while "@" in cave[len(cave)-3]:

        if ["......."] in shape:
            del cave[len(cave)-3]

    print(affiche_grid(shape))
print(affiche_grid(cave))


