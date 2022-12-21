import copy

data = open("day_20/data.txt", "r").read().split("\n")
data = [int(i) for i in data]

seen = []
for i, num in enumerate(data):

    a=0
    while (data[i], a) in seen:
        a += 1

    seen.append((data[i], a))
    data[i] = (data[i], a)
    
print(data)
    
def mix(initial: list):
    copy_file = copy.deepcopy(initial)
    
    for n in initial:
        n_index = copy_file.index(n)
        del copy_file[n_index]
        copy_file.insert((n_index+n[0])%(len(copy_file)), n[0])

    return copy_file


if __name__ == "__main__":
    
    initial = copy.deepcopy(data)
    
    tab = mix(initial)
    # print(tab)
    print(tab[(tab.index(0)+1000)%len(tab)] + tab[(tab.index(0)+2000)%len(tab)] + tab[(tab.index(0)+3000)%len(tab)])



