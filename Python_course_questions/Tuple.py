def get_last_element(tuple):
    return tuple[-1]

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(sample_list, key=get_last_element)

print("Sample List:", sample_list)
print("Sorted List:", sorted_list)
