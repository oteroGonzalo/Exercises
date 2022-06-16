# Write a function named collatz() that has one parameter named number. If number is even,
# then collatz() should print number // 2 and return this value. If number is odd, then collatz()
# should print and return 3 * number + 1.



def collatz():
    try:
        n = int(input('Introduce a non-negative integer: '))
        calculateCollatz(n)
    except:
        print('Number itroduced is not valid')

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




