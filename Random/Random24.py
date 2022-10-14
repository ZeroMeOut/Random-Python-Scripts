def sort2(unsorted_list):
    for i in range(0, len(unsorted_list) - 1):
        key = i

        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[key]:
                key = j
        unsorted_list[key], unsorted_list[i] = unsorted_list[i], unsorted_list[key]

    return unsorted_list


print(sort2([2, 3, 4, 2, 4, 2, 3, 5, 6, 7, 8, 9, 0, 7, 8]))
