from collections import Counter

def checkIfExist(arr: list[int]) -> bool:
    c = Counter(arr)
    for number in arr:
        if number == number * 2 and c[number] == 1:
            continue

        elif number == number * 2 and c[number] > 1:
            return True

        if number * 2 in c:
            return True

    return False


print(checkIfExist([0,-2,2]))