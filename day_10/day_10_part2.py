Instructions = open("day_10/data.txt", "r").read().split("\n") 
Instructions = [Instruction.split(" ") for Instruction in Instructions] 


if __name__ == "__main__":
        
    cycle = 1
    X = 1
    img = "#"
    for instr in Instructions:
        if not instr[0] == 'noop':
            cycle += 1

            if X <= cycle <= X+2:
                img += "#"
            else:
                img += "."

            if (cycle)%40 == 0:
                img += "\n"
                cycle = 0
                print(cycle, X) 

            X += int(instr[1])

        cycle += 1

        if X <= cycle <= X+2:
            img += "#"
        else:
            img += "."

        if (cycle)%40 == 0:
            img += "\n"
            cycle = 0

            print(cycle, X) 

    # print(cycle)
    print(img)


