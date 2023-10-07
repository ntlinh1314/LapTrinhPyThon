def average_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return sum(odd_numbers) / len(odd_numbers)
arr = [ 2, 6, 8, 9, 29]
print("Trung binh cac so le la:", average_odd_numbers(arr))