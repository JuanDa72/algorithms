def myPow(x: float, n: int) -> float:
    def pow(x, value, current, n):

        if n == 0:
            return 1

        if n == 1 or n == -1:
            return x

        if current == n:
            return value

        if n > 0:
            value = value * x
            new_current = current + 1
            return pow(x,value, new_current, n)


        elif n < 0:
            value = value * x
            new_current = current - 1
            return pow(x,value, new_current, n)


    if n < 0:
        return pow(1 / x,1, 0, n)

    else:
        return pow(x,1, 0, n)


print(myPow(2.0000,10))