def removeElement(nums, val):
    nums.append("a")
    k:int = 0
    counter:int = 0
    limit:int=len(nums)
    while (nums[counter]!="a"):
        if (nums[counter] == val):
            nums.pop(counter)
            nums.append(val)

        else:
            k+=1
            counter += 1
            #print(counter, k)

    print(nums)
    return k

print(removeElement([0,1,2,2,3,0,4,2], 2))