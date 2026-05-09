def divisorSubstrings(num: int, k: int) -> int:
    num = str(num)
    count: int = 0
    left = 0
    for right in range(k - 1, len(num)):
        case:int=int(num[left:right + 1])
        if case!=0 and int(num) % case == 0:
            count += 1

        left += 1

    return count


print(divisorSubstrings(430043, 2))