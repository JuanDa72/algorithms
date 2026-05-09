def findMaxAverage(nums: list[int], k: int) -> float:
    left = 0
    right = 0
    result: int = 0
    current: int = 0
    while right < len(nums):
        if right - left < k:
            current += nums[right]
            right += 1
            result = max(current, result)

        else:
            current -= nums[left]
            left += 1
            #print(nums[right], nums[5])
            current += nums[right]
            result = max(current, result)
            right+=1

    return result/4


print(findMaxAverage([1,12,-5,-6,50,3], 4))