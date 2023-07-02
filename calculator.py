# This is a script for a simple calculator
 
# Addition function
def addition(number1, number2):
    return float(number1) + float(number2)

# Subtraction function
def subtraction(number1, number2):
    return float(number1) - float(number2)

# Multiplication function
def multiplication(number1, number2):
    return float(number1) * float(number2)

# Division function
def division(number1, number2):
    if float(number2) !=0:
    	return float(number1) / float(number2)
    else: 
    	print("Error: Division by zero is not allowed!")


number1 = input("Number 1:")
number2 = input("Number 2:") 

operation = input("Please select the desired operation:\n\n 1. Addition (+) \n 2. Subtraction (-)\n 3. Multiplication (*) \n 4. Division (/)\n") 

if operation == "1":
     result=addition(number1,number2)
     print("Result:", result)
elif operation == "2":
     result=subtraction(number1,number2)
     print("Result:", result)
elif operation == "3":
     result=multiplication(number1,number2)
     print("Result:", result)
elif operation == "4":
     result=division(number1,number2)
     print("Result:", result)
else:
    print ("Error")



