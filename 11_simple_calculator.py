# ===============================================================
# Simple Calculator
# ===============================================================

while True:
    print(
        "7  8  9  *\n"
        "4  5  6  -\n"
        "1  2  3  +\n"
        "   0     /\n"
    )

    try:
        equation = input("Enter your math equation (or 'q' to quit): ")

        if equation.lower() == 'q':
            break

        result = eval(equation)
        print(f"Result: {result}\n")

    except:
        print("Invalid input!")