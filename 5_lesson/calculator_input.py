import calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
action = (input("Enter action (+ or - or * or /: "))
match action:
    case "+":
        print(f"Result: {calculator.add(a,b)}")
    case "_":
        print(f"Result: {calculator.subtract(a,b)}")
    case "*":
        print(f"Result: {calculator.multiply(a,b)}")
    case "/":
        print(f"Result: {calculator.divide(a,b)}")