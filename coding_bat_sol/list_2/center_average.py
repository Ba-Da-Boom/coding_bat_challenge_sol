def center_average(nums):
    nums.sort()
    return sum(nums[1:-1]) / (len(nums) - 2)
