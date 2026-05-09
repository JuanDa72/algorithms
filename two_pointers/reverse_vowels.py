def reverseVowels(s: str) -> str:
    s = list(s)
    vowels: set = {'a', 'e', 'i', 'o', 'u'}
    start: int = 0
    finish: int = len(s) - 1
    flag_start = False
    flag_finish = False
    while start != finish:
        if (s[start].lower() not in vowels and not flag_start):
            start += 1
            if start==finish:
                break

        if (s[start].lower() in vowels and not flag_start):
            flag_start = True

        if (s[finish].lower() not in vowels and not flag_finish):
            finish -= 1
            if start==finish:
                break

        if (s[finish].lower() in vowels and not flag_finish):
            flag_finish = True

        if flag_start and flag_finish:
            s[start], s[finish] = s[finish], s[start]
            flag_start = False
            flag_finish = False
            start += 1
            finish += -1

    return "".join(s)

print(reverseVowels("ai"))
