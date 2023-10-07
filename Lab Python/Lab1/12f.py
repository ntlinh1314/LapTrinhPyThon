def product_odd_not_divisible_by_3(arr):
    odd_numbers = [num for num in arr if num % 2 != 0 and num % 3 != 0]
    product = 1
    for num in odd_numbers:
        product *= num
    return product
arr = [2,5,7]
print("f) Product of odd numbers not divisible by 3:", product_odd_not_divisible_by_3(arr))