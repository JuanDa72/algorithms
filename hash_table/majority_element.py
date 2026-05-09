def majorityElement(nums: list[int]) -> int:
    nums_sorted = sorted(nums)
    objetive: int = len(nums_sorted) // 2
    current_value=nums_sorted[0]
    max:int=1
    counter:int=1
    for i in range(1,len(nums_sorted)):
        if nums_sorted[i]==nums_sorted[i-1]:
            counter+=1
            if counter>max:
                max=counter
                current_value=nums_sorted[i]
                if max>objetive:
                    return current_value

        else:
            counter=1

    return current_value

print(majorityElement([3,2,3]))



