# Menu-Driven Calculator using Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! 0 se divide nahi hota"
    return a / b

# Main Program
while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice 1/2/3/4/5: ")
    
    if choice == '5':
        print("Calculator closed. Bye Kajal!")
        break
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Pehla number daal: "))
        num2 = float(input("Dusra number daal: "))
        
        if choice == '1':
            print("Result:", num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print("Result:", num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
            print("Result:", num1, "*", num2, "=", mult(num1, num2))
        elif choice == '4':
            print("Result:", num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid choice! 1 se 5 ke beech daal")
