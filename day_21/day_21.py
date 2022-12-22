import copy

data = open("day_21/data.txt", "r").read().split("\n")
data = [i.split(":") for i in data]

def create_dico(data: list):
    dico = {}
    for line in data:
        dico[line[0]] = line[1].strip().split(" ")

    return dico        
    
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
    
def get_number_p1(monke: str, dico: dict):

    if not is_number(dico[monke][0]):
        dico[monke][0] = get_number_p1(dico[monke][0], dico)
        dico[monke][2] = get_number_p1(dico[monke][2], dico)

        if is_number(dico[monke][0]) and is_number(dico[monke][2]):
            if monke != "root":
                dico[monke] = str(eval("".join(dico[monke])))
                return dico[monke]
        
    else:
        # print(dico)
        return dico[monke][0]

    
    
def part_1(dico: dict):
    dico = copy.deepcopy(dico)
    
    get_number_p1("root", dico)
    # print(eval("".join(dico["root"])))
    # print(float(dico["root"][0])-float(dico["root"][2]))
    # print(dico["humn"])
    

def part_2(dico: dict):
    dico = copy.deepcopy(dico)

    while dico["root"][0] != dico["root"][2]:
        dico["humn"] = [str(int(dico["humn"][0])-1)]
        part_1(dico)
    
    print(dico["humn"])


if __name__ == "__main__":
    
    dico_mere = create_dico(data)

    part_1(dico_mere)
    part_2(dico_mere)
    
    # print(dico)

