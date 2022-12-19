shapes = {
    0 : lambda y : ((2, y), (3, y), (4, y), (5, y)),
    1 : lambda y : ((3, y - 2), (2, y - 1), (3, y - 1), (4, y - 1), (3, y)),
    2 : lambda y : ((4, y - 2), (4, y - 1), (2, y), (3, y), (4, y)),
    3 : lambda y : ((2, y - 3), (2, y - 2), (2, y - 1), (2, y)),
    4 : lambda y : ((2, y - 1), (3, y - 1), (2, y), (3, y))
}

with open("day_17/data.txt", "r") as file:
    states = {}
    data = file.read()
    grid = {x : [0] for x in range(7)}
    i, vert, e = 0, -4, 0
    length = len(data)
    p1, p2 = None, None
    seen = {}
    while not all([p1, p2]):
        rock_i = i % 5
        p1 = p1 or (-min(sum(grid.values(), [])) if i == 2022 else None)
        shape = shapes[rock_i](vert)
        while True:
            jet_e = e % length
            op = data[jet_e]
            e += 1
            if not any((shift := (x + 1 if op == ">" else x - 1)) > 6 or shift < 0 or y in grid[shift] for x, y in shape):
                shape = [((x + 1 if op == ">" else x - 1), y) for x, y in shape]
            if not any(y + 1 in grid[x] for x, y in shape):
                shape = [(x, y + 1) for x, y in shape]
                continue
            break  
        for x, y in shape:
            grid[x].append(y)
        mn = min(sum(grid.values(), []))
        current = [mn - min(grid[x]) for x in grid]
        if (rock_i, jet_e) not in seen:
            seen[rock_i, jet_e] = (current, mn, i)
        else:
            if (p := seen[(rock_i, jet_e)])[0] != current:
                seen[(rock_i, jet_e)] = (current, mn, i)
            else:
                prev, prev_mn, prev_i = p
                diff = i - prev_i
                if not (1000000000000 - i) % diff:
                    p2 = (prev_mn - mn) * ((1000000000000 - i) // diff)
        i += 1
        vert = min(sum(grid.values(), [])) - 4
    print("day 17 :", p1, p2)