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
    
def find_path_dfs(valve_map, start, end, paths, path=[]):
    path = path + [start]
    
    if start == end:
        paths.append(path)
        
    if start not in valve_map:
        return False
    
    for valve in valve_map[start]['next_valves']:
        if valve not in path:
            find_path_dfs(valve_map, valve, end, paths, path)

    if len(paths):
        return True
    else:
        return False
    

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
    valves_with_flows = permutations(valves_with_flows)
    
    total = []
    a = 0
    for valves_with_flow in valves_with_flows:
        if a <= 1000:
            # print("test")
            valves_with_flow = list(valves_with_flow)
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
                            paths = []
                            find_path_dfs(valve_map, start[0], valve, paths=paths)
                            print(minute)
                            flow = valve_map[valve]['flow_rate']
                            
                            start = (valve, len(min(paths, key=len))-1)
                            
                            # print(start)
                            
                            valves_with_flow.remove(start[0])
                            timer = len(min(paths, key=len))-1
                        
                    
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
print(find_path_dfs(valve_map, 'KR', 'ZY', paths=paths))
# print(paths)
print(len(min(paths, key=len)))
# print(part1(valve_map, ('KR', 0)))




print("--- %s seconds ---" % (time.time() - start_time))
