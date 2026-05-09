def addBinary(a: str, b: str) -> str:
    aditional: int = 0
    result = []
    a=a[::-1]
    b=b[::-1]
    if(len(a)>=len(b)):
        for i in range(len(b)):
            a_i: int = int(a[i])
            b_i: int = int(b[i])
            sum: int = a_i + b_i + aditional

            if(sum<=1):
                result.append(sum)
                aditional=0

            elif sum==2:
                result.append(0)
                aditional=1

            else:
                result.append(1)
                aditional=1

        for i in range(len(b),len(a)):
            a_i: int = int(a[i])
            sum:int=a_i+aditional

            if (sum <= 1):
                result.append(sum)
                aditional=0

            elif sum == 2:
                result.append(0)
                aditional = 1

            else:
                result.append(1)
                aditional = 1

    else:
        for i in range(len(a)):
            a_i: int = int(a[i])
            b_i: int = int(b[i])
            sum: int = a_i + b_i + aditional

            if (sum <= 1):
                result.append(sum)
                aditional=0

            elif sum == 2:
                result.append(0)
                aditional = 1

            else:
                result.append(1)
                aditional = 1

        for i in range(len(a),len(b)):
            b_i: int = int(b[i])
            sum:int=b_i+aditional

            if (sum <= 1):
                result.append(sum)
                aditional=0

            elif sum == 2:
                result.append(0)
                aditional = 1

            else:
                result.append(1)
                aditional = 1

    if(aditional!=0):
        result.append(aditional)

    f:list[int]=result[::-1]
    return "".join(map(str, f))


print(addBinary("11","1"))