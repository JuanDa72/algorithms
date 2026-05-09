import math

def findLHS(nums: list[int]) -> int:
    solution=0
    left: int = 0
    right: int = 1
    while right < len(nums) and abs(nums[left]-nums[right])!=1:
        left+=1
        right+=1

    #start
    minimun=min(nums[left],nums[right])
    maximum=max(nums[left], nums[right])
    solution=2
    for i in range(right+1, len(nums)):
        if nums[i]==minimun or nums[i]==maximum:
            solution+=1

    return solution


print(findLHS([1,1,1,1]))