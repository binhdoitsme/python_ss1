# 
def sumFourOfFive(arr: list):
    intArr = list()
    for num in arr:
        intArr.append(int(num))
    intArr.sort()
    print(sum(intArr[0:len(intArr) - 1]), sum(intArr[1:len(intArr)]), sep=' ')
    return

arr = list()
for k in input().split(" "):
    arr.append(int(k))
sumFourOfFive(arr)
