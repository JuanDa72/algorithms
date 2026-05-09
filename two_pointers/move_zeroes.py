def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = 0
    z:int=0
    while counter < len(nums):
        if nums[counter] == 0:
            nums.pop(counter)
            z+=1

        else:
            counter += 1

    for i in range(z):
        nums.append(0)



print(moveZeroes([0]))
