def titleToNumber(columnTitle: str) -> int:
    to_rest: int = 64
    counter: int = 0
    result: int = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        result += (ord(columnTitle[i]) - to_rest) * 26 ** counter
        counter += 1

    return result

print(titleToNumber("ZY"))