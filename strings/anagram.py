def isAnagraml(s: str, t: str) -> bool:
    count:dict={}
    counter:int=0
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]]+=1
            counter+=count[s[i]]

        if s[i] not in count:
            count[s[i]]=1
            counter+=count[s[i]]

        if t[i] in count:
            count[t[i]]-=1
            counter+=count[t[i]]

        if t[i] not in count:
            count[t[i]]=-1
            counter+=count[t[i]]

    #print(counter)
    for element in count:
        if count[element]!=0:
            return False

    return True

print(isAnagraml("anagram", "nagaram"))