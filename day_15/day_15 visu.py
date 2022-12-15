import json
import re


def affiche_grid(grid):
    string = ''
    for row in grid:
        string += "".join("{:>1}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string
    
    
def build_data():
    data = open("day_15/data.txt", "r").read()
    # data = [i.split("->") for i in data]

    pattern = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    matches = pattern.finditer(data)
    
    data = []
    for match in matches:
        sensor_x = match.group(1)
        sensor_y = match.group(2)
        beacon_x = match.group(3)
        beacon_y = match.group(4)
        
        data.append([[int(sensor_x), int(sensor_y)], [int(beacon_x), int(beacon_y)]])

    return data


def create_grid(data):
    min = [-20, -20]
    max = [50, 50]
    for line in data:
        for i, pair in enumerate(line):
            # pair = (int(pair.split(",")[0]), int(pair.split(",")[1]))
            
            min[0] = pair[0] if pair[0] < min[0] else min[0]
            max[0] = pair[0] if pair[0] > max[0] else max[0]
            max[1] = pair[1] if pair[1] > max[1] else max[1]

            line[i] = pair

    print(min, max)
    grid = [["."for i in range(0, max[0]-min[0]+1)] for j in range(0, max[1]-min[1]+1)]
    print("done")

    return [grid, min, max]

def place_S_and_B(grid, data):
    for line in data:
        for i, pair in enumerate(line):
            if i == 0:
                grid[pair[1]-min[1]][pair[0]-min[0]] = "S"
            else:
                grid[pair[1]-min[1]][pair[0]-min[0]] = "B"
                


def put_signals(grid, start, end):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    pre_queue = []
    pre_queue.append(start)
    
    queue = []
    queue.extend(pre_queue)

    found = False
    visited = [start]
    
    
    
    while pre_queue:
        while queue:

            vertex = queue.pop(0)
            
            if vertex == end:
                return "done"
            
            x, y = vertex[0],vertex[1]
            origin = grid[y][x]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)
                
                if (0 <= nx < len(grid[y]) and
                    0 <= ny < len(grid) and
                    neighbor not in visited):
                    
                    next = grid[ny][nx]
                    
                    if next == ".":
                        grid[ny][nx] = "#"
                        visited.append(neighbor)
                        
                    if neighbor == end:
                        found = True
                    
                    pre_queue.append(neighbor)
                    
        # affiche_grid(grid)
        
        if not found:
            queue.extend(pre_queue)
        else:
            break
    
                    
    return False

def all_signal(grid, data):
    for pair in data:
        sensor = pair[0]
        beacon = pair[1]
        
        put_signals(grid, (sensor[0]-min[0], sensor[1]-min[1]), (beacon[0]-min[0], beacon[1]-min[1]))
        
def affiche_line(grid, n):
    count = 0
    for i in grid[n-min[1]]:
        if i == '#':
            count += 1

    return count

if __name__ == '__main__':

    data = build_data()
    # print(data)
    
    d = create_grid(data)
    grid = d[0]
    min = d[1]
    max = d[2]
    
    place_S_and_B(grid, data)
    affiche_grid(grid)

    all_signal(grid, data)

    affiche_grid(grid)
    print(min, max, "\n")
    
    print(affiche_line(grid, 10))
    
    
    