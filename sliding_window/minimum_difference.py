def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()
    result = float('inf')
    current = 0
    left = 0
    right = k-1
    while right < len(nums):
        current = nums[right] - nums[left]
        if current < result:
            result = current

        right += 1
        left += 1

    return result


print(minimumDifference([90],1))