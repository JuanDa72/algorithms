def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # string vacío

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[n]


print(wordBreak("aaaaaaa", ["aaaa","aaa"]))