def numDecodings(s: str) -> int:
    dp = [0] * len(s)
    for i in range(len(s)):
        print(ord(s[i]))


print(numDecodings("ABCD"))