def sum_of_digits_in_list(arr):
    total_sum = 0
    for num in arr:
        total_sum += sum(int(digit) for digit in str(num))
    return total_sum
arr = [ 1, 2, 3, 8]
print("Sum of digits in list:", sum_of_digits_in_list(arr))