number = int(input("Please enter a number equal or greater than 2 : "))

if number < 2:
    raise ValueError()

def find_prime_factors(number):
    prime_factors = []
    factor = 2

    while number > 1:
        if number % factor == 0:
            prime_factors.append(factor)
            number //= factor
        else:
            factor += 1
        
    return prime_factors

prime_factors = find_prime_factors(number)

print(f"The prime factors of {number} are: {prime_factors}")
