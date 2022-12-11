import json

file = open("day_11/data.txt", "r").read().split("\n") 
instructions = [list(filter(None, i.split(' '))) for i in file if i]



if __name__ == '__main__':

    monkeys = {}
    for index in range(0, len(instructions), 6):
        monkey = instructions[index][0]+instructions[index][1]

        items = [int(i.split(',')[0]) for i in instructions[index+1] if i.split(',')[0].isnumeric()]
        monkeys[monkey] = {'items':items,
                           "item_inspected":0}
    

    for i in range(20):
        for index in range(0, len(instructions), 6):
            monkey = instructions[index][0]+instructions[index][1]

            items = monkeys[monkey]['items'][:]

            operation = ''.join(instructions[index+2][-3:])
            for old in items:
                resultat = eval(operation)
                worry = resultat//3
                test = int(instructions[index+3][-1])
                throwTrue = int(instructions[index+4][-1])
                throwFalse = int(instructions[index+5][-1])

                if worry % test == 0:
                    monkeys[monkey]['items'].remove(old)
                    monkeys["Monkey"+str(throwTrue)+":"]['items'].append(worry)
                    
                else:
                    monkeys[monkey]['items'].remove(old)
                    monkeys["Monkey"+str(throwFalse)+":"]['items'].append(worry)
                    
                monkeys[monkey]['item_inspected'] += 1
                    # print(monkeys)

    # print(json.dumps( monkeys, indent=4 ))

    max = []
    for a in monkeys:
        max.append(monkeys[a]['item_inspected'])
        print(max)
    
    max.sort()
    print("P1: ", max[-2]*max[-1] , max[-2:])