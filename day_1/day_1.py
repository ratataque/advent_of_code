with open("day_1/data.txt" ,"r") as f:
    data = []
    
    for lutin in f.read().split("\n\n"):    
        cal = 0
        for i in lutin.split("\n"):
            cal += int(i)
        data.append(cal)

    data.sort()
    # print(data)
    print("top 3: ", data[-1],data[-2],data[-3])
    print("somme: ", data[-1]+data[-2]+data[-3])

