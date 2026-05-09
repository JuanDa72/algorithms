def longestCommonPrefix(strs: list[str]) -> str:
    first=min(strs)
    last=max(strs)
    last_size=len(last)-1
    counter=0
    for i in range(len(first)):
        if(i>last_size or first[i]!=last[i]):
            break

        counter+=1

    if counter!=0:
        return first[:counter]

    else:
        return ""



print(longestCommonPrefix(["belsy","tuur","entonces"]))

