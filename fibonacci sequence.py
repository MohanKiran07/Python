def fibonacci_series(n):
    # Initialize the Fibonacci series with the first two terms
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci series up to n terms
    for i in range(2, n):
        next_term = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Get input from the user for the number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate and print the Fibonacci series
fib_series = fibonacci_series(num_terms)
print("Fibonacci Series:")
print(fib_series)
