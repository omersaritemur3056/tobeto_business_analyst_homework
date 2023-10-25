height = float(input("Please enter your height in meter: "))
weight = float(input("Please enter your weight in kilogram: "))

if height < 0 and weight < 0 :
    raise ValueError("Please enter values greater than zero!")

body_mass_index = weight / (height * height)

print(f"Your body mass index is {body_mass_index} ")
