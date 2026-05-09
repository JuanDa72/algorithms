def findRepeatedDnaSequences(s: str) -> list[str]:
    d: dict = {}
    result: list[str] = []
    left = 0
    right = 9
    for i in range(right, len(s)):
        current = "".join(s[left:i+1])
        if current not in d:
            d[current] = 1

        else:
            if d[current] == 1:
                result.append(current)

            d[current] += 1

        left += 1

    return result


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))