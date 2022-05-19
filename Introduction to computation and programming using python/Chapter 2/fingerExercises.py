
# Write a program tat examines three variables-x, y, 
# and z-and prints the largest odd number among them. 
# If none of them are odd, it should print a message to that effect


x = int(input('introduce positive integer for variable x: '))
y = int(input('introduce positive integer for variable y: '))
z = int(input('introduce positive integer for variable z: '))
largestOdd = ""
if x % 2 == 0:
    largestOdd = x
    
if y % 2 == 0 and y > x:
    largestOdd = y
    
if z % 2 == 0 and z > largestOdd:
    largestOdd = z
if largestOdd != "":
    print(largestOdd)
else:
    print("no odd numbers were introduced")





# Replace the comment in the following code with a while loop.

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#Start of exercise
while numXs > 0:
    print("X", end= "")
    numXs -= 1
#End of exercise
print(toPrint)



# Write a program that asks  the user to input 10 integers,
# and then prints the largest odd number that was entered. 
# If no odd number was entered, it should print a message to that effect

while x > 0:
    num = input("Introduce an integer: ")
    if num == "":
        print("Not valid input")
    elif float(num) - round(float(num)) != 0:
        print("Not an integer")
    else: 
        num = int(num)
        if largestNum == "":
            largestNum = num
            x -= 1
        else:
            if num % 2 == 0 and num > largestNum:
                largestNum = num
            x -= 1
        
if largestNum % 2 != 0:
    print("No odd numbers were introduced")
else:
    print(largestNum)
