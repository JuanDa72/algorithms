def find_max_crossing_subarray(A, low, mid, high):
    """
    :param A: array
    :param low: index first array
    :param mid: index last position first half
    :param high: index last position second half
    :return:
    """

    left_sum=float("-inf")
    sum=0
    for i in range(mid, low-1, -1):
        sum+=A[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i

    right_sum=float("-inf")
    sum=0
    for j in range(mid+1, high+1):
        sum+=A[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j

    return (max_left, max_right, left_sum+right_sum)


def find_maximum_subarray(A, low, high):
    if high==low:
        return (low, high, A[high])

    else:
        mid=(low+high)//2
        (left_low, left_high, left_sum)=find_maximum_subarray(A, low, mid)
        (right_low, right_high, right_sum)=find_maximum_subarray(A, mid+1, high)
        (cross_low,cross_high, cross_sum)=find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)

        else:
            return (cross_low, cross_high, cross_sum)


A = [-2,1,-3,4,-1,2,1,-5,4]

low, high, total = find_maximum_subarray(A, 0, len(A)-1)

print(low, high, total)
print(A[low:high+1])