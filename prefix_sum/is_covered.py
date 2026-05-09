def isCovered(ranges: list[list[int]], left: int, right: int) -> bool:
    for i in range(left, right + 1):
        flag = False
        for l, r in ranges:
            if i >= left and i <= right:
                flag = True
                break

        if not flag:
            return False

    return True


print(isCovered([[1,10],[10,20]],21,21))