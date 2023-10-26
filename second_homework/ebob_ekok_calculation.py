def find_ebob(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2

    return number1

def find_ekok(number1, number2):
    return number1 * number2 // find_ebob(number1, number2) # // operator take the integer value from result

number1 = int(input("Insert to first number: "))
number2 = int(input("Insert to second number: "))

ebob = find_ebob(number1, number2)
ekok = find_ekok(number1, number2)

print(f"The numbers of ebob is {ebob}.")
print(f"The numbers of ekok is {ekok}.")
