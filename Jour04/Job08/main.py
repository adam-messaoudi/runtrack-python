def total_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
print(total_numbers(L))
