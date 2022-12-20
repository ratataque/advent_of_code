import copy

data = open("day_17/data.txt", "r").read()

shape_data = open("day_17/shape.txt", "r").read().split("\n\n")
shape_data = [[list(j) for j in i.split("\n")] for i in shape_data]

def affiche_grid(grid):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    # print(string, "\n")
    return string

def can_moove(cave, dx, dy, sha_rd):
    for coord in sha_rd:
        x = coord[0]
        y = coord[1]
        if (0 > y+dy or y+dy >= len(cave)) or (0 > x+dx or x+dx >= len(cave[y])):
            return False
        if cave[y+dy][x+dx] == "#":
            return False
    return True


# print(data)
print(1000000000000//50455*78749+20777)
print(1000000000000-1000000000000//50455*50455)

sh_co = []
for index, shape in enumerate(shape_data):
    sh = []
    for i, line in enumerate(shape):
        for j, char in enumerate(line):
            if char == "@":
                sh.append([j, i])
    sh_co.append(sh)


cave = []
rocks_fallen = 0
gas_jet = 0
while rocks_fallen > 10091:
    for index, shape in enumerate(shape_data):
        cave = copy.deepcopy(shape) + copy.deepcopy(cave)
        
        shape_coord = copy.deepcopy(sh_co[index])
        
        # print(affiche_grid(cave))
        
        while len(cave) > len(shape)-3 :
            
            can_slide_left = False
            can_slide_right = False
            if data[gas_jet%len(data)] == "<":
                can_slide_left = can_moove(cave, -1, 0, shape_coord)
            else:
                can_slide_right = can_moove(cave, 1, 0, shape_coord)
                
            if can_slide_left:
                for coord in shape_coord:
                    x = coord[0]
                    y = coord[1]
                    
                    cave[y][x] = "."
                    coord[0] -= 1
                    cave[y][coord[0]] = "@"
                                    
                # print(affiche_grid(cave))
            if can_slide_right:
                for coord in shape_coord[::-1]:
                    x = coord[0]
                    y = coord[1]
                    
                    cave[y][x] = "."
                    coord[0] += 1                    
                    cave[y][coord[0]] = "@"
                                    
                # print(affiche_grid(cave))
            
            gas_jet += 1
                


            can_fall = can_moove(cave, 0, 1, shape_coord)
            
            if can_fall:
                for coord in shape_coord[::-1]:
                    x = coord[0]
                    y = coord[1]
                    
                    cave[y][x] = "."                   
                    cave[y+1][x] = "@"
                                    
                # print(affiche_grid(cave))
                if "#" not in cave[0]:
                    cave.pop(0)
                else:
                    for coord in shape_coord[::-1]:
                        x = coord[0]
                        y = coord[1]
                        
                        coord[1] += 1
             
            else:
                break
            
        if len(cave) == 1:
            can_slide_left = False
            can_slide_right = False
            if data[gas_jet%len(data)] == "<":
                can_slide_left = can_moove(cave, -1, 0, shape_coord)
            else:
                can_slide_right = can_moove(cave, 1, 0, shape_coord)
                
            if can_slide_left:
                for coord in shape_coord:
                    x = coord[0]
                    y = coord[1]
                    
                    cave[y][x] = "."
                    coord[0] -= 1
                    cave[y][coord[0]] = "@"
                                    
                # print(affiche_grid(cave))
            if can_slide_right:
                for coord in shape_coord[::-1]:
                    x = coord[0]
                    y = coord[1]
                    
                    cave[y][x] = "."
                    coord[0] += 1                    
                    cave[y][coord[0]] = "@"
                                    
                # print(affiche_grid(cave))
            
            gas_jet += 1
            
            
        for coord in shape_coord:
                x = coord[0]
                y = coord[1]
                cave[y][x] = "#"
          
        rocks_fallen += 1
        
        if rocks_fallen >= 10091:
            break
        # print(affiche_grid(cave))
        
        # j'ai besoin des coordonnée pour trouver de chaque shape dans le tableau et de les faire bouger en bas ou en 
        # fonction des inputs, et chaque fois si la ligne au top est  empy je l'a suprime
        

 
# print(affiche_grid(cave))

print(len(data))
print("Part1: ", len(cave))


