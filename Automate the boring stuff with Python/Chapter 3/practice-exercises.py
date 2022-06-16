def collatz():
    try:
        n = int(input('Introduce a non-negative integer: '))
        calculateCollatz(n)
    except:
        print('Number itroduces is not valid')

def calculateCollatz(n):
    print(n)
    if n == 1:
        return
    else:
        if n % 2 == 0:
            nextNum = n // 2
            return calculateCollatz(nextNum)
        else:
            nextNum = n * 3 + 1
            return calculateCollatz(nextNum)




