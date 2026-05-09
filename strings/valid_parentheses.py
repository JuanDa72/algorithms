def isValid(s: str) -> bool:
    f:dict={")":"(","}":"{","]":"["}
    stack:list=[]
    for i in s:
        if i in f:

            if stack:
                if f[i] == stack[-1]:
                    stack.pop()

                else:
                    return False

            else:
                return False

        else:
            stack.append(i)

    return True if len(stack)==0 else False


print(isValid("]"))