import math
def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))
hypotenuse = calculate_hypotenuse(side_a, side_b)
print(f"The hypotenuse of the triangle is: {hypotenuse:.2f}")
