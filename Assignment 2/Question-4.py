def sort_tuples(tuples):

    sorted_tuples = sorted(tuples, key=lambda x: x[-1])
    return sorted_tuples


tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


sorted_tuples = sort_tuples(tuples_list)


print(sorted_tuples)
