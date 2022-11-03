def array_advance(nums):
    furthes_reached = 0
    last_idx = len(nums) - 1
    i = 0
    while i <= furthes_reached and furthes_reached < last_idx:
        furthes_reached = max(furthes_reached, nums[i] + i)
        i += 1
    return furthes_reached >= last_idx