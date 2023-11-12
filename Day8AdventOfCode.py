def isVisible(arr, i, j, matrixLength):
    numbers = []
    for x in range(i - 1, -1, -1):  # all numbers on top
        numbers.append(arr[x][j])
    if arr[i][j] > max(numbers): return True
    numbers.clear()
    for x in range(i + 1, matrixLength):  # all numbers below
        numbers.append(arr[x][j])
    if arr[i][j] > max(numbers): return True
    numbers.clear()
    for x in range(j + 1, matrixLength):  # all numbers to the right
        numbers.append(arr[i][x])
    if arr[i][j] > max(numbers): return True
    numbers.clear()
    for x in range(j - 1, -1, -1):  # all numbers to the left
        numbers.append(arr[i][x])
    if arr[i][j] > max(numbers): return True
    return False


def getScenicScore(arr, i, j, matrixLength):
    scenicScore, scoreOnSide = (1, 0)

    for x in range(i - 1, -1, -1):
        if arr[i][j] > arr[x][j]: scoreOnSide += 1
        if arr[i][j] <= arr[x][j]:
            scoreOnSide += 1
            scenicScore *= scoreOnSide
            scoreOnSide = 0
            break
    else:
        scenicScore *= scoreOnSide
        scoreOnSide = 0

    for x in range(i + 1, matrixLength):
        if arr[i][j] > arr[x][j]: scoreOnSide += 1
        if arr[i][j] <= arr[x][j]:
            scoreOnSide += 1
            scenicScore *= scoreOnSide
            scoreOnSide = 0
            break
    else:
        scenicScore *= scoreOnSide
        scoreOnSide = 0

    for x in range(j - 1, -1, -1):
        if arr[i][j] > arr[i][x]: scoreOnSide += 1
        if arr[i][j] <= arr[i][x]:
            scoreOnSide += 1
            scenicScore *= scoreOnSide
            scoreOnSide = 0
            break
    else:
        scenicScore *= scoreOnSide
        scoreOnSide = 0

    for x in range(j + 1, matrixLength):
        if arr[i][j] > arr[i][x]: scoreOnSide += 1
        if arr[i][j] <= arr[i][x]:
            scoreOnSide += 1
            scenicScore *= scoreOnSide
            break
    else:
        scenicScore *= scoreOnSide

    return scenicScore


file = open("day8input.txt", "r")
line = file.readline()
matrixLength = len(line) - 1
visibleTrees = 2 * matrixLength + (matrixLength - 2) * 2
arr = [[0 for i in range(matrixLength)] for j in range(matrixLength)]
for i in range(matrixLength):
    for j in range(matrixLength):
        arr[i][j] = int(line[j])
    if i != matrixLength: line = file.readline()

scenicScore = 0
for i in range(1, matrixLength - 1):
    for j in range(1, matrixLength - 1):
        scenicScore = max(scenicScore, getScenicScore(arr, i, j, matrixLength))
        if isVisible(arr, i, j, matrixLength):
            visibleTrees += 1
# print("Part 1 Answer: " + str(visibleTrees))
print("Part 2 Answer: " + str(scenicScore))