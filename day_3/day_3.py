import string

# test1 = 3
# test2 = 8
# print(test1)
# print(test2)

# test2 ^= test1
# print(test1)
# print(test2)
# test1 ^= test2
# print(test1)
# print(test2)
# test2 ^= test1

# print(test1)
# print(test2)

# print([i for i in zip(a,b)])
# char = ord("a")^ord("a")^ord("b")^ord("D")^ord("C")^ord("c")
# print(chr(char))

# a = [12, 2, 32, 62, 54]
# z = [1, 2, 943, 4, 42]
# b = [9, 8, 2, 6, 5]
# c = "tetest"
# d = "gfvdgfdge"
# # print((set(c) & set(d)).pop())
# # print((set(a) & set(b)).pop())
# print(set(a) & set(b) & set(z))

# print(string.ascii_letters.index('a')+1)

# print(ord("a")-96)
# print(ord("A")-38)

# dataPart2 = [data[i:i+3] for i in range(0, len(data), 3)]

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
for i in range(len(data)):
    if i%3 == 0:
        m1 = data[i]
        m2 = data[i+1]
        m3 = data[i+2]

        letter = (set(m1) & set(m2) & set(m3)).pop()

        totalPart2 += string.ascii_letters.index(letter)+1 

print("Partie 2: ", totalPart2)

