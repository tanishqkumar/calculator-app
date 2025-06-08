from calculator import add, subtract, multiply, divide, rectangle_area, rectangle_perimeter

def main():
    print("Calculator Demo")
    print("----------------")
    print(f"Addition: 2 + 3 = {add(2, 3)}")
    print(f"Subtraction: 5 - 2 = {subtract(5, 2)}")
    print(f"Multiplication: 4 * 5 = {multiply(4, 5)}")
    print(f"Division: 10 / 2 = {divide(10, 2)}")
    print(f"Rectangle Area: 4 * 5 = {rectangle_area(4, 5)}")
    print(f"Rectangle Perimeter: 4 * 5 = {rectangle_perimeter(4, 5)}")

if __name__ == '__main__':
    main()