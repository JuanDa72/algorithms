def maxProduct(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        value = nums[i]
        max_product = max(value, value * max_product, value * min_product)
        min_product = min(value, value * max_product, value * min_product)

        result = max(result, max_product)

    return result


print(maxProduct([-4,-3,-2]))
