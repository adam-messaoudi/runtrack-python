def count_multiples_of_3(lst):
    count = 0
    for num in lst:
        if num % 3 == 0:
            count += 1
    return count

L = [8, 24, 48, 2, 16]
print(count_multiples_of_3(L))
