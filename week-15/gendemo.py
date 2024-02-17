def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to print Fibonacci numbers up to a certain limit
limit = 10
fib_gen = fibonacci_generator()

for _ in range(limit):
    print(next(fib_gen))
