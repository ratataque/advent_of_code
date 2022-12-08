Instructions = open("day_7/data.txt", "r").read().split("\n") 
Instructions = [Instruction.split(" ") for Instruction in Instructions] 


curr_dir = [] 
PathTotalSize = {} 
for Instruction in Instructions:
    # print(curr_dir)
    if Instruction[0] == "$": 
        if Instruction[1] == "cd": 
            if Instruction[2] == "..": 
                curr_dir.pop() 

            else: 
                curr_dir.append(Instruction[2]) 

    else: 
        if Instruction[0] != "dir": 

            for dir in curr_dir: 
                if dir == "/": 
                    current_path = dir 

                else: 
                    current_path += dir + "/" 
                if current_path in PathTotalSize: 
                    PathTotalSize[current_path] += int(Instruction[0]) 

                else: 
                    PathTotalSize[current_path] = int(Instruction[0]) 


# print(PathTotalSize)
total = 0 
for path in PathTotalSize: 
    if PathTotalSize[path] <= 100000: 
        # print(path + ": " + str(PathTotalSize[path])) 

        total += PathTotalSize[path] 

print(total) 


# for path in PathTotalSize: 
delta = 30000000 - (70000000 - PathTotalSize["/"])
test_file = 70000000
for path in PathTotalSize: 
    if delta <= PathTotalSize[path] <= test_file: 
        print(path + ": " + str(PathTotalSize[path])) 
        test_file = PathTotalSize[path]

print(test_file)
print(test_file+(70000000 - PathTotalSize["/"]))