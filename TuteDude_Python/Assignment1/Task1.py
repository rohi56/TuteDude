'''Problem Statement: Write a Python program that does the following:
    1.  Takes two numbers as input from the user.
    2.  Performs the basic mathematical operations on these two numbers:
        o	Addition
        o	Subtraction
        o	Multiplication
        o	Division
    3.  Displays the results of each operation on the screen.'''

num1= int(input("Enter the first number: "))
num2= int(input("Enter the Second number: "))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print("Addition :", add)
print("Substraction :", sub)
print("Multiplication :", multi)
print("Division :", div)