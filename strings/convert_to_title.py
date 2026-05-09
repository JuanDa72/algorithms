def convertToTitle(columnNumber: int) -> str:
    convertion:dict= {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
        14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
        20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
        26: 'Z'}

    current_value:int=columnNumber
    residue:float=float('inf')
    result:list[str]=[]
    flag:bool=False

    while current_value>0:
        current_value-=1
        residue=current_value%26
        current_value=current_value//26
        result.append(convertion[residue+1])

    result.reverse()
    return "".join(result)


print(convertToTitle(2147483647))