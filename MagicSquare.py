import random

def printMagicSquare(sum, n, numbers):
    print()
    for i in range(n + 2):
        for j in range(n + 1):
            if(i == 0 or i == 4):
                print(sum, end = ' ')
            else:
                if(j == 0):
                   print(sum, end = ' ')
                else:
                    print(numbers[j - 1 + n * (i - 1)], end = '  ')
        print(sum)
        print()

def checkMagicSquare(sum, n, numbers):
    tlbr, trbl, tb, lr = 0, 0, 0, 0
    for i in range(n): 
        tlbr += numbers[i * (n + 1)]
        trbl += numbers[(i + 1) * (n - 1)]
        for j in range(n):
            tb += numbers[j * n + i]
        if(tb != sum):
            return False
        for j in range(n):
            lr += numbers[j + (n * i)]
        if(lr != sum):
            return False
        tb, lr = 0, 0
    if(tlbr == sum and trbl == sum):
        printMagicSquare(sum, n, numbers)
        return True
    else:
        return False

# n determines the size of the magic square
def magicSquare(n):
    found = False
    numbers = []
    while(found == False): 
        for i in range(1, n * n + 1):
            x = random.randint(1, 9)
            numbers.append(x)
        for i in range(n, n * 9):
            if(checkMagicSquare(i, n, numbers) == True):
                found = True
        numbers = []