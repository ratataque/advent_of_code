forest = open("day_8/data.txt", "r").read().split("\n") 

tree = []

def is_visible(tree, i, j):
    # print(tree, i , j)
    test = 0
    for z in range(j-1, -1, -1):
        if tree <= forest[i][z]:
            
            for z in range(j+1, len(forest), 1):
                if tree <= forest[i][z]:

                    for z in range(i-1, -1, -1):
                        if tree <= forest[z][j]:

                            for z in range(i+1, len(forest), 1):
                                if tree <= forest[z][j]:
                                    return False

    return True


def scenic(tree, i, j):
    scenic = 1
    # print(tree)
    count = 0
    for z in range(j-1, -1, -1):
        count += 1
        if tree <= forest[i][z]:
            break
    scenic *= count

    count = 0
    for z in range(j+1, len(forest), 1):
        count += 1
        if tree <= forest[i][z]:
            break
    scenic *= count

    count = 0
    for z in range(i-1, -1, -1):
        count += 1
        if tree <= forest[z][j]:
            break
    scenic *= count

    count = 0
    for z in range(i+1, len(forest), 1):
        count += 1
        if tree <= forest[z][j]:
            break
    scenic *= count

    return scenic

test = 0
total = len(forest)*4-4
for i in range(1, len(forest)- 1):
    for j in range(1, len(forest)-1):

        if is_visible(forest[i][j], i,j):
            tree.append((i,j))
            # print(forest[i][j], i,j)
        
        if scenic(forest[i][j], i,j) > test:
            test = scenic(forest[i][j], i,j)


# print(tree)
print("P1: ",total+len(tree))
print("P2: ", test)