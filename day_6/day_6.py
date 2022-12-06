with open("day_6/data.txt" ,"r") as f:
    data = f.read().split("\n")

count1 = 4
for i in data:
    for j in range(3,len(i)):

        if len(set(i[j-3:j+1])) >= 4:
            break

        count1 += 1

print("P1: ", count1)



count2 = 14
for i in data:
    for j in range(13,len(i)):

        if len(set(i[j-13:j+1])) >= 14:
            break

        count2 += 1

print("P2: ", count2)