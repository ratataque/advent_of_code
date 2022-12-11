import json

file = open("day_11/data.txt", "r").read().split("\n") 
instructions = [list(filter(None, i.split(' '))) for i in file if i]



if __name__ == '__main__':
    # p = 23*19*13*17
    p = 11*19*5*3*13*17*7*2
    monkeys = {}
    for index in range(0, len(instructions), 6):
        monkey = instructions[index][0]+instructions[index][1]

        items = [int(i.split(',')[0]) for i in instructions[index+1] if i.split(',')[0].isnumeric()]
        monkeys[monkey] = {'items':items,
                           "item_inspected":0}
    

    for i in range(100):
        for index in range(0, len(instructions), 6):
            monkey = instructions[index][0]+instructions[index][1]

            items = monkeys[monkey]['items'][:]

            operation = ''.join(instructions[index+2][-3:])
            for n, old in enumerate(items):
                old %= p
                # print(old)
                resultat = eval(operation)
       
                test = int(instructions[index+3][-1])
                throwTrue = int(instructions[index+4][-1])
                throwFalse = int(instructions[index+5][-1])

                if resultat % test == 0:
                    monkeys[monkey]['items'].remove(items[n])
                    monkeys["Monkey"+str(throwTrue)+":"]['items'].append(resultat)
                    
                else:
                    monkeys[monkey]['items'].remove(items[n])
                    monkeys["Monkey"+str(throwFalse)+":"]['items'].append(resultat)
                    
                monkeys[monkey]['item_inspected'] += 1
                    # print(monkeys)
        # print(i)

    max = []
    for a in monkeys:
        max.append(monkeys[a]['item_inspected'])
        # print(max)
    
    max.sort()
    print("P2: ", max[-2]*max[-1] , max[-2:])
    # print(p)