#The Fibonacci series is a sequence where each number is the sum of the two preceding numbers, defined by a mathematical recurrence relationship
# The Fibonacci series starts with: 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number is the sum of the previous two numbers:F(n) = F(n-1) + F(n-2)


def fibonacci_generator():
    a, b = 0, 1  # Initial two values of the Fibonacci series
    while True:
        yield a        # Yield the current value
        a, b = b, a + b  # Update a and b to the next two numbers

fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))

