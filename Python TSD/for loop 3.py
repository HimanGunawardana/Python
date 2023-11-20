'''write a python program to get three numbers from the user and check
how many numbers between number 1 and number 2 are divisible by number 3.'''

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

count=0
if number1<number2:
    for x in range (number1,number2):
        
        if (x%number3==0):
            count=count+1

else:
    for x in range (number2,number1):
        if (x%number3==0):
            count=count+1


print("Number of divisibles: ",count)
