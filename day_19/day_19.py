import re
import copy

def create_data():
    data = open("day_19/data.txt", "r").read().split("\n\n")
    data = [i.split("\n") for i in data]

    bp_data = []
    for i in data:
        bp = []
        for j in i:
            ore_robot = re.search(r"Each ore robot costs (\d+) ore", j)
            clay_robot = re.search(r"Each clay robot costs (\d+) ore", j)
            obsidian_robot = re.search(r"Each obsidian robot costs (\d+) ore and (\d+) clay", j)
            geode_robot = re.search(r"Each geode robot costs (\d+) ore and (\d+) obsidian", j)
            if ore_robot:
                bp.append(int(ore_robot.group(1)))
            if clay_robot:
                bp.append(int(clay_robot.group(1)))
            if obsidian_robot:
                bp.append((int(obsidian_robot.group(1)), int(obsidian_robot.group(2))))
            if geode_robot:
                bp.append((int(geode_robot.group(1)), int(geode_robot.group(2))))
            
        bp_data.append(bp)

    return bp_data

def dfs(minerai, collecting, cost, minute):
    global GEODE_MAX

    for i in range(8 - minute):
        # print("minute: ", minute)
        # print(GEODE_MAX)
        
        building = []
        # if minerai[min] + collecting[min]

        if minerai["ore"] >= cost["geode"][0] and minerai["obsidian"] >= cost["geode"][1]:
            dict_copy = copy.deepcopy(minerai)
            dict_copy["ore"] -= cost["geode"][0]
            dict_copy["obsidian"] -= cost["geode"][1]
            dict_copy_collecting = copy.deepcopy(collecting)

            for min in collecting:
                dict_copy[min] += dict_copy_collecting[min]
                
            dict_copy_collecting["geode"] += 1

            dfs(dict_copy, dict_copy_collecting, cost, minute+1)
            
        if minerai["ore"] >= cost["obsidian"][0] and minerai["clay"] >= cost["obsidian"][1]:
            # minerai["ore"] -= cost["obsidian"][0]
            # minerai["clay"] -= cost["obsidian"][1]
            # building.append("obsidian")
            # # collecting["obsidian"] += 1
            # print("création obsidian")
            dict_copy = copy.deepcopy(minerai)
            dict_copy["ore"] -= cost["obsidian"][0]
            dict_copy["clay"] -= cost["obsidian"][1]
            dict_copy_collecting = copy.deepcopy(collecting)

            for min in collecting:
                dict_copy[min] += dict_copy_collecting[min]
                
            dict_copy_collecting["obsidian"] += 1

            dfs(dict_copy, dict_copy_collecting, cost, minute+1)
            
        if minerai["ore"] >= cost["clay"] and collecting["clay"] < 6:
            # minerai["ore"] -= cost["clay"]
            # building.append("clay")
            # # collecting["clay"] += 1
            # print("création clay")
            dict_copy = copy.deepcopy(minerai)
            dict_copy["ore"] -= cost["clay"]
            dict_copy_collecting = copy.deepcopy(collecting)

            for min in collecting:
                dict_copy[min] += dict_copy_collecting[min]
                
            dict_copy_collecting["clay"] += 1
            dfs(dict_copy, dict_copy_collecting, cost, minute+1)
            
        
        if minerai["ore"] >= cost["ore"] and collecting["ore"] < 4:
            # minerai["ore"] -= cost["ore"]
            # building.append("ore")
            # # collecting["ore"] += 1
            # print("création ore")
            dict_copy = copy.deepcopy(minerai)
            dict_copy["ore"] -= cost["clay"]
            dict_copy_collecting = copy.deepcopy(collecting)

            for min in collecting:
                dict_copy[min] += dict_copy_collecting[min]
                
            dict_copy_collecting["clay"] += 1
            dfs(dict_copy, dict_copy_collecting, cost, minute+1)
            
            
        # print(minerai)
        # print(collecting)
        for min in collecting:
            minerai[min] += collecting[min]

        # for mine in building:
        #     collecting[mine] += 1

        dfs(minerai, collecting, cost, minute+1)
            
        
    if GEODE_MAX > minerai["geode"]:
        GEODE_MAX = minerai["geode"]
    return GEODE_MAX
    

def life_cycle(bp):
    minerai = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    collecting = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    cost = {"ore": bp[0], "clay": bp[1], "obsidian": bp[2], "geode": bp[3]}

    dfs(minerai, collecting, cost, 1)
            
            

GEODE_MAX = 0
if __name__ == "__main__":
    
    data = create_data()
    print(data)
    
    life_cycle(data[0])
    print(GEODE_MAX)