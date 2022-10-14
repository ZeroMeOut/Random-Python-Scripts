def is_isogram(string):
    # your code here
    count_list = []
    for count in string.lower():
        if count in count_list:
            return False, print(count_list)
        count_list.append(count)
    return True


print(is_isogram("moOse"))
