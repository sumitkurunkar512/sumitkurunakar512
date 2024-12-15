def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    if y != 0: 
        return (x / y)
    else: 
        return "Cannot divide by zero"
def main():
    print("SIMPLE CALCULATOR")
    num1=float(input("Enter the 1st number:"))
    num2=float(input("Enter the 2rd number:"))

    print("selection the operation:")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

    choice=input("Enter the choice(1/2/3/4):")

    if choice == '1':
        print(f"The result of addition: {add(num1, num2)}") 
    elif choice == '2': 
        print(f"The result of subtraction: {subtract(num1, num2)}")
    elif choice == '3': 
        print(f"The result of multiplication: {multiply(num1, num2)}") 
    elif choice == '4': 
        print(f"The result of division: {divide(num1, num2)}") 
    else: print("Invalid input")

if __name__ == "__main__": 
    main()

