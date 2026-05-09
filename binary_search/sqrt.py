def mySqrt(x: int) -> int:
    left:int=0
    right=x
    mid=(right+left)//2
    ans=0

    if x==x*x:
        return x

    while left<right:
        if mid*mid==x:
            return mid

        elif mid**2>x:
            right=mid-1
            mid=(left+right)//2

        else:
            ans = mid
            left=mid+1
            mid=(left+right)//2

    return ans

print(mySqrt(6))