def has22(nums):
    for iterate_number, number in enumerate(nums[0:-1]):
        if number == 2 and nums[iterate_number + 1] == 2:
            return True
    return False


