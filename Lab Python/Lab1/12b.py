import math
def fibonacci_numbers(arr):
    a, b = 0, 1
    fib = []
    while b < max(arr):
        if b in arr:
            fib.append(b)
        a, b = b, a + b
    return fib
'''arr = [1, 2, 3, 5, 8, 10]
print(" So Fibonacci la:", fibonacci_numbers(arr))'''

arr = list(map(int, input("Enter a list of integers separated by spaces: ").split(" ")))
print("b) Fibonacci numbers:", fibonacci_numbers(arr))
  