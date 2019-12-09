import math
def findMax(numbers: list()) -> int:
    max = int(numbers[0])
    for n in numbers:
        if n > max:
            max = n
    return max

def firstPrimeNumbers(quantity: int) -> list():
    firstPrimes = list()
    firstPrimes.append(2)
    i = 2
    i = 1
    while len(firstPrimes) <= quantity:
        i = i + 2
        isNotPrime = False
        for k in range(2, int(math.sqrt(i) + 1)):
            if i % k == 0:
                isNotPrime = True
                break
        if not isNotPrime:
            firstPrimes.append(i)
    return firstPrimes

# other algorithm to improve efficiency

numbers = [5, 2, 3, 4, 1]
print(findMax(numbers))

print(firstPrimeNumbers(15))