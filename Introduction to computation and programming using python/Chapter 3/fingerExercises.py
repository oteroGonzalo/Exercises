# Write a program that asks the user to enter an integer and prints two integers, root and pwr,
#  such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. 
#  If no such pair of integers exists, it should print a message to that effect.

#NOTE TO THE EXERCISE
#Since every integer can be expressed as itself to the power of 1 I've decided to ignore those results and 
#limit the program to check for powers larger than 1 and smaller than 6


num = int(input("enter a non-zero positive integer: "))
root = 0

finalRoot = 0
finalPwr = 0

while root <= num/2:
    pwr = 2
    while pwr < 6:
        if root**pwr == num:
            finalRoot = root
            finalPwr = pwr
            root = num + 1
            break
        pwr += 1
   
    root += 1
  
if finalRoot == 0:
    print("no suitable integers have been found")
else:
    print("integer root is: ", finalRoot, " integer power is ", finalPwr)





#Let s be a string that contains a sequence of decimal numbers separated by commas, 
# e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s

s = '1.23,2.4,3.123, 6.25,-0.65,0,0,123'
newStr = ""
totalSum = 0

for c in s:
    if c != ',':
        newStr += c
    else:
        totalSum += float(newStr)
        newStr = ""

totalSum += float(newStr)

print(totalSum)


# What is the decimal equivalent of the binary number 10011?


s = '10011'
index = 0
sumNum = 0

for c in s:
    sumNum += 2**((len(s)-index)-1) * int(c)
    index += 1
    
print(sumNum)

#Result: 19





