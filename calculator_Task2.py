#TASK 1: SIMPLE CALCULATOR

while True:
    print("SIMPLE CALCULATOR")
    print("Calculator Operations\n1. ADD\n2. MULTIPLY\n3. DIVIDE\n4. SUBTRACT")
    operation = int(input("Enter Operation: "))

    if operation == 1:
        print("ADD")
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("\nEnter 2nd number: "))
        answer = num1+num2
        print(num1, "+",num2, "=",str(answer))
    
    elif operation == 2:
        print("MULTIPLY")
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        answer = num1*num2
        print(num1, "x",num2, "=", str(answer))
    
    elif operation == 3:
        print("DIVIDE")
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("\nEnter 2nd number: "))
            answer = num1/num2
            print(num1,"/",num2, "=", str(answer))
        except:
            print("Synthax Error, \nPlease restart calculator!!")
        
    elif operation == 4:
        print("SUBTRACT")
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        answer = num1-num2
        print(num1,"-",num2, "=", str(answer))

    else:
        print("Error!!, \nplease enter value between 1, 2, 3, or 4")

    calculate_again = input("Calculate again? (yes/no): ").lower()
    if calculate_again != "yes":
        print("Thank you for using the calculator")
        break 

