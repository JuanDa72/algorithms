def targetIndices(nums: list[int], target: int) -> list[int]:
    nums.sort()
    index = nums.index(target)
    if index == -1:
        return []

    solution = []
    while index < len(nums) and nums[index] == target:
        solution.append(index)
        index += 1

    return solution


print(targetIndices([1,2,5,2,3],4))
