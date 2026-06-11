def counting_dac(array,value):
    counter=0
    if len(array)==1:
        if array[0]==value:
            counter+=1

        return counter

    else:
        k=len(array)//2
        first_part=counting_dac(array[:k],value)
        second_part=counting_dac(array[k:],value)

        total=first_part+second_part
        return total

print(counting_dac([6, 6, 6, 6],6))