def isIsomorphic(s: str, t: str) -> bool:
    convertion:dict={}
    checker:set=set()
    for i in range(len(s)):
        if s[i] in convertion:
            if convertion[s[i]]!=t[i]:
                return False

        else:
            if t[i] in checker:
                return False
            convertion[s[i]]=t[i]
            checker.add(t[i])

    return True


print(isIsomorphic("badc", "baba"))