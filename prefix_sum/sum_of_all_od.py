def sumOddLengthSubarrays(arr: list[int]) -> int:
    def prefix_sum(nums):
        result = [0]
        count = 0
        for num in nums:
            count += num
            result.append(count )

        return result

    ps = prefix_sum(arr)
    s: int = 0
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            if (j - i) % 2 == 1:
                s += ps[j] - ps[i]

    return s


print(sumOddLengthSubarrays([1,4,2,5,3]))