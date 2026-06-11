def check_dac(array):
    if len(array)==1:
        return True

    else:
        n=len(array)//2
        v1=check_dac(array[:n])
        v2=check_dac(array[n:])

        if v1 and v2:
            if array[n-1]<=array[n]:
                return True

        return False

print(check_dac([5, 4, 3, 2, 1]))