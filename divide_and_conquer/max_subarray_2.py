def cross_value(array, low, high, h):
    left_sum=float("-inf")
    right_sum=float("-inf")
    value_l=0
    value_r=0

    for i in range(h, low-1, -1):
        value_l+=array[i]
        left_sum=max(left_sum, value_l)

    for j in range(h+1,high+1):
        value_r+=array[j]
        right_sum=max(right_sum, value_r)

    return max(left_sum, right_sum, left_sum+right_sum)



def maxsub_dac(array, low, high):
    if low==high:
        return array[low]

    else:
        h=(low+high)//2
        left=maxsub_dac(array, low, h)
        right=maxsub_dac(array, h+1, high)
        crossing=cross_value(array, low, high, h)
        return max(left, right, crossing)


print(maxsub_dac([1, -2, 3, 4, -1, 2], 0, 5))