def rob(nums: list[int]) -> int:
    if len(nums) < 2:
        return nums[0]

    if len(nums) < 3:
        return max(nums[0], nums[1])

    dp = [[0] * 2 for i in range(len(nums) - 1)]

    n = len(nums) - 1

    dp[0][0] = nums[0]
    dp[0][1] = nums[1]

    dp[1][0] = max(nums[0], nums[1])
    dp[1][1] = max(nums[1], nums[2])

    for i in range(2, len(nums) - 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 2][0] + nums[i])
        dp[i][1] = max(dp[i-1][1], dp[i - 2][1] + nums[i + 1])

    return max(dp[n - 1][0], dp[n - 1][1])


print(rob([1,7,9,2]))