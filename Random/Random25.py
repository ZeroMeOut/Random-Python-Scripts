def removeElement(nums, val):

    for index, item in enumerate(nums):
        if nums[index] == val:
            nums.remove(item)
    return nums


print(removeElement([0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 0, 4, 2], 1))
