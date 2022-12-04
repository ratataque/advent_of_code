import string

with open("day_3/data.txt" ,"r") as f:
    data = f.read().split("\n")



totalPart1 = 0
for i in data:
    m1 = i[0:len(i)//2]
    m2 = i[len(i)//2:len(i)]

    letter = (set(m1) & set(m2)).pop()

    totalPart1 += string.ascii_letters.index(letter)+1 

print("Partie 1: ", totalPart1)



totalPart2 = 0
for i in range(0, len(data), 3):
    m1 = data[i]
    m2 = data[i+1]
    m3 = data[i+2]

    letter = (set(m1) & set(m2) & set(m3)).pop()

    totalPart2 += string.ascii_letters.index(letter)+1 

print("Partie 2: ", totalPart2)

