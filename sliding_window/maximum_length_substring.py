def maximumLengthSubstring(s: str) -> int:
    d: dict = {}
    left = 0
    right = 0
    maximum = 0
    while right < len(s):
        if s[right] not in d:
            d[s[right]] = 1
            right += 1

        elif s[right] in d and d[s[right]] == 1:
            d[s[right]] += 1
            right += 1

        else:
            maximum = max(maximum, right - left)
            if d[s[right]] == 2:
                d[s[right]] -= 1
            else:
                del d[s[right]]

            left += 1

    maximum = max(maximum, right - left)
    return maximum


print(maximumLengthSubstring("bcbbbcba"))