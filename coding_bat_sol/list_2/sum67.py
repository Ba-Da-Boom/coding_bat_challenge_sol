def sum67(nums):
    count = 0
    block = False

    for num in nums:
        if num == 6:
            block = True
        if num == 7 and block:
            block = False
            continue
        else:
            count += num
    return count