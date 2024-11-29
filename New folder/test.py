import time
def factorial(n):
  
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calculate_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


number = 1000
result, time_taken = calculate_time(factorial, number)

print(f"Factorial of {number} is {result}")
print(f"Time taken to calculate: {time_taken:.10f} seconds")