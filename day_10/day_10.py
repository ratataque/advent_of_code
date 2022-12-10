Instructions = open("day_10/data.txt", "r").read().split("\n") 
Instructions = [Instruction.split(" ") for Instruction in Instructions] 


if __name__ == "__main__":
        
    cycle = 1
    X = 1
    total = 0
    for instr in Instructions:
        if not instr[0] == 'noop':
            cycle += 1
            if (cycle-20)%40 == 0:
                total += cycle * X

            X += int(instr[1])

        cycle += 1
        # print(cycle, X)
        if (cycle-20)%40 == 0:
            total += cycle * X


    print(total)


