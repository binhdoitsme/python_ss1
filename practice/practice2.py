def getInput() -> int:
    return int(input())
def stairCase(n : int):
    output = list()
    for i in range(n):
        for k in range(n - i - 1):
            output.append(" ")
        for k in range(i + 1):
            output.append("#")
        if i < n - 1:
            output.append("\n")
    print("".join(p for p in output),end='')


stairCase(int(input()))
