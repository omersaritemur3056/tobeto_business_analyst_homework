fibonacci_array = [1, 1]

while len(fibonacci_array) < 20:
    new_array = fibonacci_array[-1] + fibonacci_array[-2]
    fibonacci_array.append(new_array)

print(fibonacci_array)
