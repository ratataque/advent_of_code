import re
from collections import deque
import time
from itertools import permutations
start_time = time.time()

def build_data():
    valves = {}
    data = open("day_16/data.txt", "r").read().split("\n")
    
    for line in data:
        valve_name = re.search(r"Valve (\w+)", line).group(1)
        flow_rate = re.search(r"=(\d+)", line).group(1)
        
        i = (re.search(' valve', line)).end() + 1
        next_valves = [s.strip() for s in line[i:].split(",")]
        
        valves[valve_name] = {"flow_rate": int(flow_rate), "next_valves": next_valves}
        
        
    return valves
    
def find_path_bfs(valve_map, start, end):
    if start not in valve_map:
        return None
    
    queue = [start]
    
    visited = [start]
    
    distances = {start: 0}
    while queue:
        
        curr_valve = queue.pop(0)
        
        for valve in valve_map[curr_valve]['next_valves']:
            # print(distances)
            distance = distances[curr_valve] + 1
            if valve not in visited:
                distances[valve] = distance
                
                # if valve == end:
                #     print(distances)
                #     return distances[valve]
                # else:
                queue.append(valve)
                visited.append(valve)
                    
    # print(distances)
    return distances
    

def valve_with_flow(valve_map):
    valves_with_flow = []
    for valve in valve_map:
        if valve_map[valve]['flow_rate'] > 0:
            valves_with_flow.append(valve)
        
    return valves_with_flow

def better(valves_with_flow, start):
    count = 0
    for valve in valves_with_flow:
        if start != valve:
            paths = []
            find_path_dfs(valve_map, start, valve, paths=paths)
            flow = valve_map[valve]['flow_rate']
            
            path = min(paths, key=len)
            
            if count <= flow//(len(path)-1):
                count = flow//(len(path)-1)
                valve_to_take = valve
        else:
            valve_to_take = valve
        
    return (valve_to_take, len(path)-1)

def minute_plus(open, pressure, n):
    for i in range(n):
        for valve in open:
            pressure += valve_map[valve]['flow_rate']
            print("pressure: ", valve_map[valve]['flow_rate'])
    
    return pressure
    
    
def part1(valve_map, start):

    valves_with_flows = valve_with_flow(valve_map)
    valves_with_flows.reverse()
    valves_with_flows = permutations(valves_with_flows)
    
    total = []
    a = 0
    for valves_with_flow in valves_with_flows:
        if a <= 10000:
            # print(valves_with_flow)
            valves_with_flow = list(valves_with_flow)
            valves_with_flow.reverse()
            # if valves_with_flow == ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']:
            open = set()
            
            start = ('KR', 0)
            minute = 0
            pressure = 0
            timer = 0
            valve = 0
            while minute <= 30:
                # print("minutes: ", minute)
                # print("pressure: ", sum([valve_map[i]['flow_rate'] for i in open]), "\n")
                pressure += sum([valve_map[i]['flow_rate'] for i in open])
                
                if start[0] in valves_with_flow:
                    open.add(start[0])
                    valves_with_flow.remove(start[0])
                    
                else:
                    if timer:
                            timer -= 1
                    else:
                        if valve:
                            open.add(valve)
                            
                        if valves_with_flow:
                            
                            valve = valves_with_flow[0]

                            path_len = callendar[start[0]][valve]
                            # path_len = find_path_bfs(valve_map, start[0], valve)
                            # print(minute)
                            flow = valve_map[valve]['flow_rate']
                            
                            start = (valve, path_len)
                            
                            # print(start)
                            
                            valves_with_flow.remove(start[0])
                            timer = path_len
                        
                    
                minute += 1
                            
                    
            # print(open, minute)
            # print(pressure)
            total.append(pressure)
            a += 1
        
        else:
            break

        # print(sorted(total))
    return sorted(total)[-1]

valve_map = build_data()


paths = [] 
# print(valve_map)
# print(find_path_dfs(valve_map, 'BB', 'JJ', paths=paths))
# print(paths)
# print(min(paths, key=len))


start = 'BB'
end = "HH"
callendar = {}
for i in valve_map:
    callendar[i] = find_path_bfs(valve_map, i, end)

# print(callendar)
    
print(part1(valve_map, ('KR', 0)))
# print(valve_map)




print("--- %s seconds ---" % (time.time() - start_time))
