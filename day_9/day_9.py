Instructions = open("day_9/data.txt", "r").read().split("\n") 
Instructions = [Instruction.split(" ") for Instruction in Instructions] 

d = {"R": "[0]+=1", "L": "[0]-=1" , "U": "[1]+=1", "D": "[1]-=1"}
visitedP1 = [(0,0)]
visitedP2 = [(0,0)]

def is_in_range(H, T):
    if abs(H[0] - T[0]) <=  1 and abs(H[1]-T[1]) <=  1:
        return True
    return False


if __name__ == '__main__':
    for b in range(10):
        exec("T"+str(b)+"= [0, 0]")

    for i, instr in enumerate(Instructions):
        direction = instr[0]
        quantite = instr[1]

        for z in range(int(quantite)):
            exec("T0"+d[direction])
            
            for k in range(1,10):
                knot = eval("T"+str(k))
                knotPre = eval("T"+str(k-1))

                if not is_in_range(knotPre,knot):
                    if knotPre[0] > knot[0]:
                        exec("T"+str(k)+d["R"])
                    elif knotPre[0] < knot[0]:
                        exec("T"+str(k)+d["L"])
                    
                    if knotPre[1] > knot[1]:
                        exec("T"+str(k)+d["U"])
                    elif knotPre[1] < knot[1]:
                        exec("T"+str(k)+d["D"])
                    
                    if not visitedP1.__contains__(tuple(knot)) and k == 1:
                        visitedP1.append(tuple(knot))

                    if not visitedP2.__contains__(tuple(knot)) and k == 9:
                        visitedP2.append(tuple(knot))

    # print(T9)
    print("P1: "+str(len(visitedP1)))
    print("P2: "+str(len(visitedP2)))
