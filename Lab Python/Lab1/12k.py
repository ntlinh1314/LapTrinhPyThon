def count_occurrences(arr, num):
    return arr.count(num)
arr = [4, 6, 8]
num = int(input("Enter a number to count occurrences: "))
print(f"Number of occurrences of {num}:", count_occurrences(arr, num))
