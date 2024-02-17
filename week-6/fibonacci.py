def generate_fibonacci_loop(n):
    
    fibonacci_series = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b
        
    return fibonacci_series


n = 10  # Change this value to generate a different number of terms

fibonacci_series_loop = generate_fibonacci_loop(n)
print("Fibonacci Series (using loop):", fibonacci_series_loop)
