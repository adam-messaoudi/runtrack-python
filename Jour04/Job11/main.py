def increment_list(lst):
    for i in range(len(lst)):
        lst[i] += 1
    return lst

L = [7, 11, 42, 39, 2]
print(increment_list(L.copy()))  
