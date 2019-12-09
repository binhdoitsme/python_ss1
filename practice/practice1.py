def plusMinus():
    n = int(input())
    arr = input().split(" ")
    
    positives = int(0)
    negatives = int(0)
    zeros = int(0)

    for integer in arr:
        integer = int(integer)
        if integer == 0:
            zeros = zeros + 1
        elif integer < 0:
            negatives = negatives + 1
        else:
            positives = positives + 1
    
    print(str(round(positives/n, 6)))
    print(str(round(negatives/n, 6)))
    print(str(round(zeros/n, 6)))
    
plusMinus()
