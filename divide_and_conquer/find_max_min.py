def find_dac(array):
    if len(array)==1:
        return array[0], array[0]

    else:
        n=len(array)//2
        left_min, left_max=find_dac(array[:n])
        right_min, right_max=find_dac(array[n:])

        global_min=min(left_min,right_min)
        global_max=max(right_max, left_max)

        return global_min, global_max

print(find_dac([4, 4, 4, 4]))