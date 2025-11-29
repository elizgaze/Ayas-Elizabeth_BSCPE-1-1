import math

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Exit")
try:
    option = int(input("Choose an operation: "))
except ValueError:
    print("Invalid input. Please enter a number corresponding to an option.")
    exit()

output_message = ""

if(option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif option == 2:
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif option == 3:
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif option == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
            
elif option == 5:
    try:
        num1 = float(input("Enter number: "))
    except ValueError:
        output_message = "Invalid number input."
    else:
        if num1 >= 0:
            result = math.sqrt(num1)
            output_message = f"The square root of {num1} is: {result}"
        else:
            output_message = "Error: Cannot calculate the square root of a negative number."
            
elif option == 6:
    output_message = "Thank you for using the calculator. Exiting program."
    
else:
    print("Invalid option selected.")
    
print(output_message)
