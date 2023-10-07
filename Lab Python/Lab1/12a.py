def odd_numbers_not_divisible_by_5(arr):
    return [num for num in arr if num % 2 != 0 and num % 5 != 0]
'''arr = [2, 5, 7, 9, 15]
print("So le khong chia het cho 5 la: ", odd_numbers_not_divisible_by_5(arr))'''

'''n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)
print(odd_numbers_not_divisible_by_5(arr))'''

arr = list(map(int, input("Enter a list of integers separated by spaces: ").split(" ")))
print("Odd numbers not divisible by 5:", odd_numbers_not_divisible_by_5(arr))