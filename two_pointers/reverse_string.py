def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    slow = len(s) - 1
    for fast in range(len(s)//2):
        s[fast], s[slow] = s[slow], s[fast]
        slow += -1

    return s


print(reverseString(["h","e","l","l","o"]))