import operator
# print(eval(i,ops,ops))


with open("day_4/data.txt" ,"r") as f:
    data = f.read().split("\n")

ops = { "-": operator.add}

group = [i.split(",") for i in data]



count1 = 0
for elf in group:
    for i in range(0, len(elf), 2):
        n = elf[i].split("-")
        n2 = elf[i+1].split("-")

        if (int(n[0]) >= int(n2[0]) and int(n[1]) <= int(n2[1])) or (int(n2[0]) >= int(n[0]) and int(n2[1]) <= int(n[1])):
            count1 += 1

print("partie 1: ",count1)




count2 = 0
for elf in group:
    for i in range(0, len(elf), 2):
        n = elf[i].split("-")
        n2 = elf[i+1].split("-")

        if ((int(n2[0]) <= int(n[0]) <= int(n2[1]))) or ((int(n[0]) <= int(n2[0]) <= int(n[1]))):
            count2 += 1


print("partie 2: ", count2)
