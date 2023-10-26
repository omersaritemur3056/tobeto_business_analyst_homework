number = int(input("Insert a number: "))

if number <= 0:
    raise ValueError("Please enter a number greater than zero!")

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
