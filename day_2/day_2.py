# print(next(iter(tabPart1)))
# print(list(tabPart1.keys())[-1])
#print(list(tabPart2.keys()).index(opponent))

with open("day_2/data.txt" ,"r") as f:
    data = f.read().split("\n")


tabPart1 = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

scorePart1 = 0
for round in data:

    opponent = tabPart1[round[0]]
    us = tabPart1[round[2]]

    if (opponent-1) % 3 == us%3:
        scorePart1 += us

    elif (opponent+1) % 3 == us%3:
        scorePart1 += 6 + us

    elif opponent == us:
        scorePart1 += 3 + us



tabPart2 = {'A': 1, 'B': 2, 'C': 3}
tabUs = {'X': "lose", 'Y': "draw", 'Z': "win"}

scorePart2 = 0
for round in data:

    index = list(tabPart2.keys()).index(round[0])
    us = tabUs[round[2]]


    if us == "lose":
        scorePart2 += list(tabPart2.values())[index-1]

    elif us == "win":
        scorePart2 += 6 + list(tabPart2.values())[(index+1)%3]

    elif us == "draw":
        scorePart2 += 3 + list(tabPart2.values())[index]


# print(data)

print("P1§ le score est: ", scorePart1)
print("P2§ le score est: ", scorePart2)
