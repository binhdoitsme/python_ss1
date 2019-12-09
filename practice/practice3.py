def getInput() -> list:
    size = int(input())
    matrix = list()
    # build matrix
    for i in range(size):
        line = list()
        for k in input().split(" "):
            line.append(int(k))
        matrix.append(line)

def absoluteDiagDifference(matrix: list):
    size = len(matrix)
    primarySum = secondarySum = int(0)

    for i in range(size):
        primarySum = primarySum + (matrix[i])[i]
        secondarySum = secondarySum + (matrix[i])[size - 1 - i]

    print(str(abs(primarySum - secondarySum)))
    
absoluteDiagDifference()