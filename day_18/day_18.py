import json

data = open("day_18/data.txt", "r").read().split("\n")
data = [i.split(",") for i in data]
data = [tuple([json.loads(l) for l in line]) for line in data]
# print(data)

def face_exposed(data, test_cube):
    neighbor = 0
    for cube in data:
        diff = 0
        for a, b in zip(test_cube,cube):
            diff += abs(a-b)
                
        if diff == 1:
            neighbor += 1
    
    return 6-neighbor
    
def exterior_cube(data, coord_min_max):
    directions = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (-1, 0, 0),
            (0, -1, 0),
            (0, 0, -1),
        )

    exte_cubes = []
    
    queue = []

    queue.append((0,0,0))

    while queue:

        vertex = queue.pop(0)

        x, y, z = vertex[0],vertex[1],vertex[2]

        for dx, dy, dz in directions:
            nx, ny , nz= x + dx, y + dy, z + dz
            neighbor = (nx, ny , nz)
            if (coord_min_max["x"]["min"]-1 <= nx <= coord_min_max["x"]["max"]+1 and
                coord_min_max["y"]["min"]-1 <= ny <= coord_min_max["y"]["max"]+1 and
                coord_min_max["z"]["min"]-1 <= nz <= coord_min_max["z"]["max"]+1 ):

                if neighbor not in exte_cubes and neighbor not in data:
                                        
                    queue.append(neighbor)
                    exte_cubes.append(neighbor)

    return exte_cubes


def min_max(data):
    coord_min_max = {"x": {"min": 100, "max": 0},"y": {"min": 100, "max": 0},"z": {"min": 100, "max": 0}}
    for i in data:
        if i[0] < coord_min_max["x"]['min']:
            coord_min_max["x"]['min'] = i[0]
        if i[0] > coord_min_max["x"]['max']:
            coord_min_max["x"]['max'] = i[0]
        if i[1] < coord_min_max["y"]['min']:
            coord_min_max["y"]['min'] = i[1]
        if i[1] > coord_min_max["y"]['max']:
            coord_min_max["y"]['max'] = i[1]
        if i[2] < coord_min_max["z"]['min']:
            coord_min_max["z"]['min'] = i[2]
        if i[2] > coord_min_max["z"]['max']:
            coord_min_max["z"]['max'] = i[2]
            
    return coord_min_max
            
def part1(cubes):
        
    total = 0
    for cube in cubes:
        surface = face_exposed(data, cube)
        # print(surface)
        if surface > 0:
            total += surface

    return total    

def part2(cubes):
    total = 0
    for cube in cubes:
        surface = face_exposed(data, cube)
        # print(surface)
        if surface > 0:
            total += (6-surface)

    return total 

coord_min_max = min_max(data)

# print(exterior_cube(data, coord_min_max))
print("part1: ", part1(data))
print("part2: ", part2(exterior_cube(data, coord_min_max)))
    
