from collections import deque
def strStr(haystack: str, needle: str) -> int:
    first:str=needle[0]
    needle_position:int=0
    current_position:int=0
    start:int=0
    could:bool=False
    index=-1
    queue=deque()
    while(current_position<len(haystack)):
        if(haystack[current_position]==needle[needle_position]):

            if not(could):
                start=current_position
                could=True


            current_position+=1
            needle_position+=1

            if (needle_position == len(needle)):
                index = start
                break

            if(current_position!=len(haystack)):
                if (haystack[current_position] == first and len(queue) == 0):
                    queue.append(current_position)

        else:
            if(len(queue)==0):
                could=False
                needle_position=0
                current_position+=1

            else:
                could = False
                needle_position = 0
                current_position=queue.popleft()

    return index


print(strStr("mississippi", "issip"))

