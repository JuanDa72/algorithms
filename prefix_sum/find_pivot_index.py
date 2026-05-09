def pivotIndex(nums: list[int]) -> int:
    def prefix_sum(n: list[int]) -> list[int]:
        result = [0]
        counter = 0
        for i in n:
            counter += i
            result.append(counter)

        return result

    array_sum = prefix_sum(nums)
    value = 0
    while value < len(nums):
        if value == 0:
            l = 0
            r = array_sum[len(nums)] - array_sum[value + 1]
            if l == r:
                return value


        elif value == len(nums) - 1:
            l = array_sum[len(nums) - 1]
            r = 0
            if l == r:
                return value

        else:
            l = array_sum[value]
            r = array_sum[len(nums)] - array_sum[value + 1]
            if l == r:
                return value

        value += 1

    return -1


print(pivotIndex([1,7,3,6,5,6]))