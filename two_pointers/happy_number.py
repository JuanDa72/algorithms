def isHappy(n: int) -> bool:
    n_str: str = str(n)
    s: set = set()
    flag: bool = False
    while not flag or n_str not in s:
        s.add(n_str)
        result = 0
        for digit in n_str:
            result += int(digit) ** 2

        flag = True
        if result == 1:
            return True

        n_str = str(result)

    return False

print(isHappy(19))
