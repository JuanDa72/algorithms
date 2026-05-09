def lengthOfLastWord(s: str) -> int:
    size:int=len(s)
    counter:int=size-1
    l:int=0
    flag:bool=False
    while(counter>=0):

        while(counter>=0 and s[counter]!=" "):
            l+=1
            counter-=1
            flag:bool=True

        if(flag):
            return l

        counter-=1

    return l


print(lengthOfLastWord("a"))