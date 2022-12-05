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
#print(ord("A")-38)

# dataPart2 = [data[i:i+3] for i in range(0, len(data), 3)]

with open("day_3/data.txt" ,"r") as f:
    data = f.read().split("\n")

# m1 = []
# m2 = []


for row in data:
    m1 = row[0:len(row)//2]
    m2 = row[len(row)//2:len(row)]

    print(m1,m2, len(m1),len(m2))

    if m2.__contains__("h"):
        print(True)
