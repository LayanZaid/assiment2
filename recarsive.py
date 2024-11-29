import time

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


number = 500
result, time_taken = calculate_time(factorial, number)

print(f"Factorial of {number} is {result}")
print(f"Time taken to calculate: {time_taken:.10f} seconds")