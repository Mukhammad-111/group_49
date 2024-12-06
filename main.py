try:
    show_numbers = input('напишите список чисел каждую через пробел: ').strip().split()
    nums = [int(num) for num in show_numbers]
    max_num = max(nums)
    min_num = min(nums)
    difference = max_num - min_num
    print(f'разница максимальной {max_num} и минималтной {min_num} это: {difference}')
except ValueError:
    print("вы совершали ошибку")

