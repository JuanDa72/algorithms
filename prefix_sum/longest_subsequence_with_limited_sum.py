def answerQueries(nums:list[int], queries: list[int]) -> list[int]:
    nums.sort()
    prefix_sum = [0]
    counter = 0
    for i in nums:
        counter += i
        prefix_sum.append(counter)

    result = []

    for target in queries:
        index = 0
        while index<len(prefix_sum) and prefix_sum[index] <= target:
            index += 1

        result.append(index - 1)

    return result


print(answerQueries([4,5,2,1],[3,10,21]))