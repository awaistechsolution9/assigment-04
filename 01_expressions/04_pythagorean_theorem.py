import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


try:
    a = float(input("Enter the length of the first perpendicular side (a): "))
    b = float(input("Enter the length of the second perpendicular side (b): "))

    if a <= 0 or b <= 0:
        print("Side lengths must be positive numbers.")
    else:
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
