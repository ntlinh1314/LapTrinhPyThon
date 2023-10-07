def numbers_occurred_n_times(arr, n):
    result = []
    for num in set(arr):
        if arr.count(num) == n:
            result.append(num)
    return result
arr = [3,3,4,5,4,5,6]
n = int(input("Enter n: "))
print(f"Numbers occurred {n} times:", numbers_occurred_n_times(arr, n))