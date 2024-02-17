def create_primes(numbers):
    # Creating a list that will be populated with primes
    primes = []

    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    # Iterate through the numbers and add prime numbers to the primes list
    for num in numbers:
        if is_prime(num):
            primes.append(num)

    return primes

# creating a list of numbers using comprehensions
numbers = [i for i in range(1, 20)]


# call the function to generate primes
primes = create_primes(numbers)

# Lastly, we print the prime numbers
print (primes)
