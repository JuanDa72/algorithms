def removeDuplicates(nums: list[int]) -> int:
    without_repetitions: set = set(nums)
    new_list: list = list(without_repetitions)
    counter=0
    for j in range(len(new_list)):
        if(j==0):
            nums[j]=new_list[j]
            continue

        change:bool=False
        for i in range(j):
            if(nums[i]>new_list[j]):
                current=nums[i]
                nums[i]=new_list[j]
                nums[j]=current
                change=True

        if(not(change)):
            nums[j]=new_list[j]




    return len(without_repetitions)

print(removeDuplicates([1,3,5,2,5,35,363]))