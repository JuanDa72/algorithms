def specialArray(nums: list[int]) -> int:
    nums.sort()
    cb: list[int] = [x for x in range(0, len(nums) + 1)]
    for c in cb:
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= c:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        if len(nums) - ans == c:
            return c

    return -1


print(specialArray([0,0]))