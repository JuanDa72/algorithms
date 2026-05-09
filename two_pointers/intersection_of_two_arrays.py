def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    result: list[int] = []
    nums1.sort()
    nums2.sort()
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(nums1) and pointer2 < len(nums2):
        while pointer1 < len(nums1) and  pointer2 < len(nums2) and nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1

        while pointer2 < len(nums2) and pointer1 < len(nums1) and nums2[pointer2] < nums1[pointer1]:
            pointer2 += 1

        if pointer1 < len(nums1) and pointer2 < len(nums2) and nums1[pointer1] == nums2[pointer2]:
            result.append(nums1[pointer1])
            pointer1 += 1
            pointer2 += 1

    return result


print(intersect([2], [4]))