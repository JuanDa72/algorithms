def maxScore(s: str) -> int:
    con = list(s)
    for i in range(len(con)):
        if con[i] == "0":
            con[i] = "1"
        else:
            con[i] = "0"

    con = "".join(con)
    #print(con)

    def prefix_sum(n: list[int]):
        result = [0]
        counter = 0
        for num in n:
            counter += int(num)
            result.append(counter)

        return result

    def acc(left: int, right: int, arr) -> int:
        return arr[right + 1] - arr[left]

    prefix_sum_s = prefix_sum(s)
    prefix_sum_con = prefix_sum(con)

    maximum = float("-inf")
    for j in range(len(s)-1):
        current = acc(0, j, prefix_sum_con) + acc(j + 1, len(s)-1, prefix_sum_s)
        maximum = max(maximum, current)

    return maximum


print(maxScore("00"))