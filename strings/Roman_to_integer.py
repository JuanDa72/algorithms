def romanToInt(s: str) -> int:
    convertion:dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total:int=0
    rest: int = 0
    flag:bool=False
    for i in range(len(s)):
        #print(s[i])
        if flag:
            #print("Hay que restar")
            total+=convertion[s[i]]-rest
            rest=0
            flag=False

        elif i==len(s)-1 or convertion[s[i]]>=convertion[s[i+1]]:
            #print("Suma simple")
            total+=convertion[s[i]]

        else:
            #print("hay que acumular")
            rest+=convertion[s[i]]
            flag=True

    return total


print(romanToInt("MCMXCIV"))