from collections import deque

def longestAlternatingSubarray(nums: list[int], threshold: int) -> int:
    maximum: int = 0
    left: int = 0
    right: int = 0
    queue = deque()
    def find_next_odd(start:int):
        while start<len(nums):
            if nums[start]%2!=0 or nums[start]>threshold:
                start+=1
            else:
                return start

        return -1

    left=find_next_odd(0)
    if left ==-1:
        return 0

    current_module = 0
    right = left + 1
    while right < len(nums):
        new_module = nums[right] % 2
        if new_module == 0 and nums[right]<=threshold:
            if len(queue)==0:
                queue.append(right)
            else:
                if right!=queue[0]:
                    queue.append(right)

        if new_module != current_module and nums[right] <= threshold:
            current_module = new_module
            right += 1

        else:
            if nums[right] < threshold and new_module!=current_module:
                maximum = max(maximum, right + 1 - left)
                left = queue.popleft()
                right = left + 1

            else:
                maximum = max(maximum, right - left)
                if len(queue) > 0:
                    left = queue.popleft()
                    right = left + 1

                else:
                    if right+1>=len(nums):
                        break

                    else:
                        left=find_next_odd(right+1)
                        if left==-1:
                            return maximum
                        right=left+1
                        current_module=0

    maximum = max(maximum, right - left)
    return maximum


print(longestAlternatingSubarray([2,8,9,2,10,1,4,4,4,4,1,10,9,7,2,8,5],18))
