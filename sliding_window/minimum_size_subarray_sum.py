def minSubArrayLen(target: int, nums: list[int]) -> int:
    minimum = float('inf')
    left = 0
    right = 0
    current = 0
    flag:bool=False
    while right < len(nums)+1:
        if current < target:
            if right==len(nums):
                break
            current += nums[right]
            right += 1


        else:
            minimum = min(minimum, right - left)
            if minimum == 1:
                return 1
            current -= nums[left]
            left += 1

    return 0 if current==sum(nums) else minimum


print(minSubArrayLen(7, [2,3,1,2,4,3]))