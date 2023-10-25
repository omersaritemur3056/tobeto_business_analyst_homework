import math


print("For circle area and circumference, enter 1.")
print("For others area and circumference, enter 2.")
rule = int(input())

if rule == 1 :
    radius = float(input("Please enter the radius of the circle in centimeter: "))

    area = math.pi * math.pow(radius, 2)
    print(f"The area of the circle is {int(area)} square centimeter.")

    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is {int(circumference)} centimeter.")

