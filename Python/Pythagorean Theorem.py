import math

def pythagorean_theorem(a, b):
    return math.hypot(a, b)

print("Pythagorean Theorem Calculator")

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = pythagorean_theorem(a, b)
print(f"The length of the hypotenuse c is: {c}")