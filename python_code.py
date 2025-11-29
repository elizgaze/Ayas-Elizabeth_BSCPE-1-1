print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = int(input("Choose an operation: "))

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
            
else:
    print("Invalid option selected.")
    
print("The result of the operation is {}".format(result))
