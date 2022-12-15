import re


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


def manhattan(sensor, beacon):
    distance = 0
    for s,b in zip(sensor,beacon):
        distance += abs(s - b)
    return distance


def min_max(data):
    min = [0, 20000000]
    max = [0, 0]
    for line in data:
        for i, pair in enumerate(line):
            
            min[0] = pair[0] if pair[0] < min[0] else min[0]
            min[1] = pair[1] if pair[1] < min[1] else min[1]
            max[0] = pair[0] if pair[0] > max[0] else max[0]
            max[1] = pair[1] if pair[1] > max[1] else max[1]

    return [min, max]


def min_max_sensor(data):
    min = [0, 0]
    max = [0, 0]
    for pair in data:
                    
        min[0] = pair[0][0] if pair[0][0] < min[0] else min[0]
        min[1] = pair[0][1] if pair[0][1] < min[1] else min[1]
        max[0] = pair[0][0] if pair[0][0] > max[0] else max[0]
        max[1] = pair[0][1] if pair[0][1] > max[1] else max[1]

    return [min, max]

def part1(data):
    count = 0
    for i in range(min[0], 5000000):
        test = (i, 2000000)        
        for pair in data:
            sensor = pair[0]
            beacon = pair[1]

            distance_ligne = manhattan(sensor, test)
            distance_beacon = manhattan(sensor, beacon)
            
            if distance_ligne <= distance_beacon:
                count += 1
                break
        
    return count - 1


def part2(data):
    
    tests = []
    for pair in data:
        sensor_a = pair[0]
        beacon_a = pair[1]
        
        for p in data:
            sensor_b = p[0]
            beacon_b = p[1]
                    
            if pair != p:
                
                distance_beacon_a = manhattan(sensor_a, beacon_a)
                distance_beacon_b = manhattan(sensor_b, beacon_b)
                distance_sensor_ab = manhattan(sensor_a, sensor_b)
                
                if distance_beacon_a + distance_beacon_b + 2 == distance_sensor_ab:
                    # print(sensor_a, sensor_b, distance_sensor_ab)
                    
                    if sensor_a[0] > sensor_b[0]:
                        blank_line = midle_coord((sensor_a[0]-distance_beacon_a-1, sensor_a[1]), (sensor_b[0]+distance_beacon_b+1, sensor_b[1]))    
                    else:
                        blank_line = midle_coord((sensor_a[0]+distance_beacon_a+1, sensor_a[1]), (sensor_b[0]-distance_beacon_b-1, sensor_b[1]))    
                    
                    ligne = set(blank_line)
                    tests.append(ligne)

    for test in tests:
        for a in tests:
            if test != a:
                if a & test:
                    reponse = (a&test).pop()
                    return reponse                    
                    

def midle_coord(start, end):
    
    if start[0] <= end[0]:
        range_x = [i for i in range(start[0], end[0])]
    else:
        range_x = [i for i in range(start[0], end[0], -1)]    

    if start[1] <= end[1]:
        range_y = [i for i in range(start[1], end[1])]
    else:
        range_y = [i for i in range(start[1], end[1], -1)]    
            
    coord = []
    for x, y in zip(range_x, range_y):
        coord.append((x, y))

    coord.append(end)
    
    return coord
    
    
    
if __name__ == '__main__':

    data = build_data()    
    
    # d = min_max(data)
    d = min_max_sensor(data)
    min = d[0]
    max = d[1]
    
    # print(d)
    
    # print(part1(data))
    coord = part2(data)
    print(coord[0] * 4000000 + coord[1])
