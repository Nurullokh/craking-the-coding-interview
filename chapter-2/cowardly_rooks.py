
def move_exactly_one(coordinates, n, m):
    if n <= m:
        return "NO"
    if m == 0:
        return "NO"

    coordinates_x = {}
    coordinates_y = {}
    for coordinate in coordinates:
        if coordinate[0] in coordinates_x:
            return "NO"
        else:
            coordinates_x[coordinate[0]] = 1
    for coordinate in coordinates:
        if coordinate[1] in coordinates_y:
            return "NO"
        else:
            coordinates_y[coordinate[1]] = 1
    return "YES"



if __name__ == "__main__":
    t = int(input())
    outputs = []
    for i in range(t):
        inp = input().split()
        n, m = int(inp[0]), int(inp[1])
        coordinates = []
        for k in range(m):
            _coordinates = input().split()
            coordinates.append([int(_coordinates[0]) - 1, int(_coordinates[1]) - 1])
        outputs.append(move_exactly_one(coordinates, n, m))
    for output in outputs:
        print(output)
            
        