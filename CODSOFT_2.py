#CODSOFT
#TASK 2- CALCULATOR
#Design a simple calculator with basic arithmetic operations.
#prompt the user to input two no. and an operation choice .
#perform the calculations and display the results

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("----Select the following operations to perform-----")

    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

    op = int(input("Enter the choice from 1-4: "))

    if op == 1:
        print("The sum is:", num1 + num2)
    elif op == 2:
        print("The substraction  is:", num1 - num2)
    elif op == 3:
        print("The Multiplication  is:", num1 * num2)
    elif op == 4:
        if num2 != 0:
            print("The division is:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid input! please enter the valid input")

    next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if next_calculation == "no":
        print("Exiting the calculator")
        break
    elif next_calculation != "yes":
        print("Invalid input! Please enter 'yes' or 'no'.")
