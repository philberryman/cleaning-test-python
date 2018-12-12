
def splitInstructions(instructions):
    instructionsByLine = instructions.split("\n")
    dirtyLocationStrings = [x.split(" ") for x in instructionsByLine[2:-1]]

    class SplitData:
        roomDimensions = [int(x)
                          for x in instructionsByLine[0].split(" ")]
        startPosition = [int(x)
                         for x in instructionsByLine[1].split(" ")]
        dirtyLocationIntegers = map(lambda x:
                                    [int(x[0]), int(x[1])], dirtyLocationStrings)
        movements = list(instructionsByLine[-1])
    return SplitData


def moveRobot(currentPosition, direction, roomDimensions):
    roomX = roomDimensions[0]
    roomY = roomDimensions[1]
    x = currentPosition[0]
    y = currentPosition[1]
    if direction == "N":
        if y + 1 > roomY:
            return [x, roomY]
        return [x, y+1]
    if direction == "E":
        if y + 1 > roomX:
            return [x, roomX]
        return [x+1, y]
    if direction == "S":
        if y - 1 < 0:
            return [x, 0]
        return [x, y-1]
    if direction == "W":
        if x - 1 < 0:
            return [0, y]
        return [x-1, y]


def cleanRoom(instructionData):
    splitData = splitInstructions(instructionData)
    roomDimensions = splitData.roomDimensions
    startPosition = splitData.startPosition
    dirtyLocations = list(splitData.dirtyLocationIntegers)
    movements = splitData.movements

    dirtyToCleaned = dirtyLocations

    currentPosition = startPosition

    for i in range(0, len(movements)):
        # print(list(dirtyToCleaned))
        currentPosition = moveRobot(
            currentPosition, movements[i], roomDimensions)
        dirtyToCleaned = list(
            filter(lambda item: (str(item[0]) + "-" + str(item[1])) != (str(currentPosition[0]) + "-" + str(currentPosition[1])), dirtyToCleaned))
        # print(list(dirtyToCleaned))

    cleanedCount = len(list(dirtyLocations)) - len(list(dirtyToCleaned))

    class Output:
        finishLocation = currentPosition
        count = cleanedCount

    return Output


f = open("index.txt", "r")
if f.mode == 'r':
    instructions = f.read()
    output = cleanRoom(instructions)
    print(output.finishLocation)
    print(output.count)
