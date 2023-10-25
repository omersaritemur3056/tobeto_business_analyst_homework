salary = float(input("Please enter your salary in dollars :) : "))
raise_rate = float(input("Please enter the determined raise rate numerically, without using percentage units.: "))

if salary < 0 and raise_rate < 0 :
    raise ValueError("Please enter values greater than zero!")

raised_salary = salary + ((salary * raise_rate) / 100)

print(f"Your increased salary: {raised_salary}")