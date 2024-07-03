def find_numbers_and_sum():
    start = 101
    end = 199
    divisible_by = 7
    count = 0
    total_sum = 0

    for number in range(start, end + 1):
        if number % 7 == 0:
            count += 1
            total_sum += number
    return count, total_sum

count, total_sum = find_numbers_and_sum()
print("Count of numbers divisible by 7:", count)
print("Sum of numbers divisible by 7:", total_sum)
