import copy

grille = open("day_12/data.txt", "r").read().split("\n") 
grille = [list(i) for i in grille]

grilletest = copy.deepcopy(grille)

# definit le start et le end
for i, line in enumerate(grille):
    for j, cell in enumerate(line):
        if cell == 'S':
            end = (i, j)
            grille[i][j] = 'a'
        if cell == 'E':
            start = (i, j)
            grille[i][j] = 'z'
            

def breadth_first_search(graph, start, end, P):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Create a queue for storing the vertices that need to be explored
    queue = []

    # Create a dictionary for storing the distances from the starting vertex
    distances = {start: 0}

    # Add the starting vertex to the queue and mark it as visited
    queue.append(start)

    # Loop through the queue while it's not empty
    while queue:

        # Get the first vertex from the queue
        vertex = queue.pop(0)

        # Check if the current vertex is the end vertex
        if vertex == end and P == 1:
            return distances[vertex]
        
        if grille[vertex[0]][vertex[1]] == "a" and P == 2:
            return distances[vertex]

        x, y = vertex[1],vertex[0]
        origin = graph[y][x]

        # Loop through the neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (ny, nx)
            if (0 <= nx < len(grille[y]) and
                0 <= ny < len(grille) and
                ((ord(origin) - ord(grille[ny][nx]) <= 1))):

                distance = distances[vertex] + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                                        
                    queue.append(neighbor)
                    if not grilletest[ny][nx] == "E":
                        grilletest[ny][nx]= str(distance)
                    
    # Return false if there is no path from the start to the end vertex
    return False



# print(start, end)
print("P1: ",(breadth_first_search(grille, start, end, 1)))
print("P2: ",(breadth_first_search(grille, start, end, 2)))

# string = ''
# for row in grilletest:
#     string += "".join("{:>2}".format(x) for x in row)+"\n"
# print(string, "\n")
