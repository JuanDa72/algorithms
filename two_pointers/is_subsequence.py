def isSubsequence(s: str, t: str) -> bool:
    pointer_s = 0
    pointer_t = 0
    counter: int = 0
    while pointer_t < len(t) and pointer_s < len(s):
        if s[pointer_s] != t[pointer_t]:
            pointer_s += 1


        else:
            pointer_s += 1
            pointer_t += 1
            counter += 1

    return True if counter == len(s) else False


print(isSubsequence("abc", "ahbgdc"))