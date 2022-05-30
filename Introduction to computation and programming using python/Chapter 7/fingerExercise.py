# Implement a function that meets the specification below. Usea try-except block.


def sumDigits(s):
    
    """ Assumes s is a string 
        Returns the sum of the decimal digits in s
            For example, if s is 'a2b3c' it returns 5"""
    counter = 0
    for x in s:
        try:
            counter += int(x)
        except ValueError:
            print("this character is not an integer")
    print(counter)
