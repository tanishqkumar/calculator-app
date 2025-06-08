from calculator import add, subtract, multiply, divide

def main():
    print("Calculator Demo")
    print("----------------")
    
    print("Addition: 2 + 3 = ", add(2, 3))
    print("Subtraction: 5 - 2 = ", subtract(5, 2))
    print("Multiplication: 4 * 5 = ", multiply(4, 5))
    print("Division: 10 / 2 = ", divide(10, 2))

if __name__ == "__main__":
    main()