with open("day_5/data.txt" ,"r") as f:
    data = f.read().split("\n")


l1 = ["Z","N"]
l2 = ["M", "C", "D"]
l3 = ["P"]


l1 = ["H", "T", "Z", "D"]
l2 = ["Q", "R", "W", "T", "G", "C", "S"]
l3 = ["P", "B", "F", "Q", "N", "R", "C", "H"]
l4 = ["L", "C", "N", "F", "H", "Z"]
l5 = ["G", "L", "F", "Q", "S"]
l6 = ["V", "P", "W", "Z", "B", "R", "C", "S"]
l7 = ["Z", "F", "J"]
l8 = ["D", "L", "V", "Z", "R", "H", "Q"]
l9 = ["B", "H", "G", "N", "F", "Z", "L", "D"]


def move(f, t):
    t.append(f[-1])
    del f[-1]

def moverest(f, t, cb):
    t.append(f[len(f)-1 - cb])
    del f[len(f)-1 - cb]


for i in range(10, len(data)):
    d = data[i].split(" ")

    # for j in range(int(d[1])):
    #     move(eval("l"+d[3]),eval("l"+d[5]))

    for j in range(int(d[1]), 0, -1):
        moverest(eval("l"+d[3]), eval("l"+d[5]), j-1)
    


a = ""
for v in range(1,10):
    a += eval("l"+str(v))[-1]
    print(eval("l"+str(v)))

print(a)



