def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    left: int = 0
    s: set = set()
    right=0
    while right < len(nums):
        if nums[right] in s:
            return True

        s.add(nums[right])
        right+=1

        if right-left>k:
            s.remove(nums[left])
            left+=1

    return False



print(containsNearbyDuplicate([1,0,1,1],1))