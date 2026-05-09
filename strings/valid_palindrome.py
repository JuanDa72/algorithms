def isPalindrome(s: str) -> bool:
    stack:list[str]=[]
    for letter in s:
        if letter.isalnum():
            stack.append(letter.lower())

    return True if stack==stack[::-1] else False


print(isPalindrome("race a car"))