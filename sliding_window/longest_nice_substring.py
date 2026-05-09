def longestNiceSubstring(s: str) -> str:
    l: list[str] = sorted(s)
    current: str = l[0]
    if current.islower():
        return False
    for i in range(1, len(l)):
        if l[i].islower():
            return False