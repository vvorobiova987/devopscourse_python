# This is a script for a simple calculator
 
# Addition function
def addition(number1, number2):
    return number1 + number2

# Subtraction function
def subtraction(number1, number2):
    return number1 - number2

# Multiplication function
def multiplication(number1, number2):
    return number1 * number2

# Division function
def division(number1, number2):
    return number1 / number2

while True:
    # First number for our calculator
    number1 = input("Number 1: ")

    # Check if the first input number is correct
    if number1.isdigit():
        number1 = int(number1)
        break
    else:
        try:
            number1 = float(number1)
            break
        except ValueError:
            print("Error: Number 1 is neither an integer nor a float. Please try to write Number 1 again ")

while True:
    # Second number for our calculator
    number2 = input("Number 2: ")

    # Check if the second input number is correct
    if number2.isdigit():
        number2 = int(number2)
        break
    else:
        try:
            number2 = float(number2)
            break
        except ValueError:
            print("Error: Number 2 is neither an integer nor a float. Please try to write Number 2 again ")

while True:

#Choose the operation  
    operation = input("\nPlease select operation:\n\n 1. Addition (+) \n 2. Subtraction (-)\n 3. Multiplication (*) \n 4. Division (/)\n") 

#Check if the operation is correct
    if operation.isdigit() and int(operation) in range(1, 5):
        operation = int(operation)
        break
    else:
        print("Oops.Invalid input. Please try again")

if operation == 1:
     result=addition(number1,number2)
     print("Result:", result)
elif operation == 2:
     result=subtraction(number1,number2)
     print("Result:", result)
elif operation == 3:
     result=multiplication(number1,number2)
     print("Result:", result)
elif operation == 4:
     if number2 != 0:
         result=division(number1,number2)
         print("Result:", result)
     else:
         print("Error: Division by zero is not allowed!")
     
else:
    print ("Error")



