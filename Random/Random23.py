def sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]
        j = i - 1

        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j + 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j + 1]
            j -= 1
        unsorted_list[j + 1] = key
    return unsorted_list


print(sort([2, 3, 4, 3, 4, 5, 3, 4, 6, 78, 6, 3, 2, 4, 6]))
