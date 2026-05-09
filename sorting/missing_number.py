def missingNumber(nums: list[int]) -> int:
    s: set = {x for x in range(0, len(nums) + 1)}
    a:set=set(nums)

    return (s-a).pop()

print(missingNumber([3,0,1]))