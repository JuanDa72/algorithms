import random

def containsDuplicate(nums: list[int]) -> bool:
    s: set = set()
    while len(nums) > 0:
        index: int = random.randint(0, len(nums) - 1)
        if nums[index] in s:
            return False

        s.add(nums[index])
        nums.pop(index)

    return True

print(containsDuplicate([1,2,3,1]))