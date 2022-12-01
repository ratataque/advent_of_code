with open("data.txt" ,"r") as f:
    data = []
    
    for lutin in f.read().split("\n\n"):    
        cal = 0
        for i in lutin.split("\n"):
            cal += int(i)
        data.append(cal)

    #print(data)
    data.sort()
    print("top 3: ", data[-1],data[-2],data[-3])
    print("somme: ", data[-1]+data[-2]+data[-3])

