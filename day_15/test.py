def affiche(grid):
    string = ''
    for row in grid:
        string += "".join("{:>3}".format(x) for x in row)+"\n"
    print(string, "\n")
    # return string


row = [0,1,2,3,4,5,6,7,8,9]
column = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]

grid = [[i+j for i in range(10)] for j in range(0,100, 10)]

point1 = (5, 0)
point2 = (0, 4)
# inter = grid[point2[1]][point1[0]]

point3 = (3,9)
point4 = (9,3)


x = ((point3[0] + point3[1])+(point4[0] - point4[1]))//2
y = point3[0] + point3[1] - x
print(x,y)
inter_diago = grid[y][x]

print(inter_diago)




affiche(grid)







