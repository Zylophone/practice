def max_night(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    today, prev = 0, 0
    for num in nums:
        today, prev = max(prev + num, today), today
    return today


print max_night([5, 1, 1, 5])
