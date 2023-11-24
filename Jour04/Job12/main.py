def sort_list(list):
    n = 0
    while n < len(list)-1:
        if list[n] > list[n+1]:
            list[n], list[n+1] = list[n+1], list[n]
            n = 0
        else:
            n += 1

my_list = [7, 2, 5, 1, 9, 3]
sort_list(my_list)
print("sorted list :", my_list)
