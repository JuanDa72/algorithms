def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    if k == 0:
        return [0] * n

    result = code[:]
    if k > 0:
        value: int = sum(code[1:(k%n)+1])
        for i in range(len(code)):
            result[i] = value
            value -= code[(i + 1) % n]
            value += code[(i + 1 + k) % n]

    else:
        value:int=sum(code[k:n])
        first:int=n+k
        for i in range(len(code)):
            result[i]=value
            value-=code[(first+i)%n]
            value+=code[i]

    return result

print(decrypt([2,4,9,3],-2))