def singleNumber(nums: list[int]) -> int:
    d: dict = dict()
    values:list[int]=[]
    for num in nums:
        #print(num)
        if num in d:
            #print("num se encuentra en el diccionario")
            d[num]+=1
            if d[num]==2:
                values.remove(num)
                #print(values)

        else:
            #print("no existe")
            d[num]=1
            values.append(num)
            #print(values)

    return values[0]


print(singleNumber([1]))




