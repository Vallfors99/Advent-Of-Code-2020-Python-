import sys
input_file = sys.stdin
input_file = open(sys.argv[1], 'r')
lines = input_file.readlines()

directions = ["e", "se", "sw", "w", "nw", "ne"]
vector = dict()
vector["e"] = [0, 2]  # y,x coords
vector["se"] = [-1, 1]
vector["sw"] = [-1, -1]
vector["w"] = [0, -2]
vector["nw"] = [1, -1]
vector["ne"] = [1, 1]
# input prep
for idx in range(0, len(lines)):
    lines[idx] = lines[idx].strip("\n")
    lines[idx] = lines[idx].replace("sw", ",sw,")
    lines[idx] = lines[idx].replace("nw", ",nw,")
    lines[idx] = lines[idx].replace("ne", ",ne,")
    lines[idx] = lines[idx].replace("se", ",se,")
    lines[idx] = lines[idx].replace("en", ",e,n,")
    lines[idx] = lines[idx].replace("ew", ",e,w,")
    lines[idx] = lines[idx].replace("we", ",w,e,")
    lines[idx] = lines[idx].replace("ww", ",w,w,")
    lines[idx] = lines[idx].replace("ee", ",e,e,")
    lines[idx] = lines[idx].split(",")
    lines[idx] = [elem.replace(",", "") for elem in lines[idx]]
    lines[idx] = [elem for elem in lines[idx] if len(elem) > 0]
tileDict = dict()
for line in lines:
    tileID = (0, 0)
    for elem in line:
        tileID = tileID[0] + vector[elem][0], tileID[1] + \
            vector[elem][1]
    if tileID in tileDict:
        tileDict[tileID] += 1
    else:
        tileDict[tileID] = 1

for tile in tileDict:
    tileDict[tile] = tileDict[tile] % 2

res_1 = sum(tileDict.values())
print(f'Part 1 result: {res_1}')

# part 2


def getWhiteNeighbours(blacktile):
    neighbours = [(blacktile[0] + direction[0], blacktile[1] + direction[1])
                  for direction in vector.values()]

    for tile in neighbours:
        if tile not in tileDict:
            white2check.append(tile)
            tileDict[tile] = 0

        elif tileDict[tile] == 0:
            white2check.append(tile)


def updateTile(tile):
    neighbours = [(tile[0] + direction[0], tile[1] + direction[1])
                  for direction in vector.values()]
    relevantvalues = [tileDict[coords]
                      for coords in neighbours if coords in tileDict]
    if tileDict[tile] == 1 and (sum(relevantvalues) == 0 or sum(relevantvalues) > 2):
        return 0
    elif tileDict[tile] == 0 and sum(relevantvalues) == 2:
        return 1
    else:
        return None


days = 1
while days < 101:
    blackTiles = []
    white2check = []
    newValues = []
    initial_len = len(tileDict)
    initial_keys = list(tileDict.keys())
    for idx in range(0, initial_len):
        tile = initial_keys[idx]
        if tileDict[tile] == 1:  # black
            blackTiles.append(tile)
            getWhiteNeighbours(tile)

    tiles2check = set(blackTiles + white2check)  # dubbelkolla
    for tile in tiles2check:
        newTileValue = updateTile(tile)
        if newTileValue != None:
            newValues.append([tile, newTileValue])

    for idx_val in newValues:
        tileDict[idx_val[0]] = idx_val[1]

    days += 1

print(f'Part 2 result: {sum(tileDict.values())}')
input_file.close()
