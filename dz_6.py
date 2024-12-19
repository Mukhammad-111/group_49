from random import choice


def selection_sort(nums):
    for i in range(0, len(nums) - 1):
        min_x = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_x]:
                min_x = j
        nums[i], nums[min_x] = nums[min_x], nums[i]

    return nums

print(selection_sort([12, 445, 6, 87, 1111, 2024]))


def buble_sort(numbers):
    for h in range(0, len(numbers) - 1):
        for i in range(0, len(numbers) - h - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers

nums = [2005, 3, 115, 456, 1001, 227]
print(buble_sort(nums))


def binary_search(val, n: list):
    result_ok = False
    first = 0
    last = len(n) - 1
    while first <= last:
        middle = (first + last) // 2
        if val == n[middle]:
            result_ok = True
            break
        elif val > n[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if result_ok:
        return 'Элемент найден'
    else:
        return "Элемент не найден"

numbers_list = list(range(0, 100))
vall = choice(numbers_list)

print(binary_search(vall, numbers_list))
