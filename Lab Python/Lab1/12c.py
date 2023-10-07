def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime(arr):
    prime_numbers = [num for num in arr if is_prime(num)]
    return max(prime_numbers)

n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)
print("Largest prime number:", largest_prime(arr))