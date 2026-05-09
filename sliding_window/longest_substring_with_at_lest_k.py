from collections import Counter, deque

def longestSubstring(s: str, k: int) -> int:
    count = Counter(s)
    current_count: dict = {}
    size:int=0
    left = None
    maximum: int = 0
    queue = deque()
    right=0
    while right <len(s):
        if count[s[right]]>=k:
            if left==None:
                left=right

            if s[right]!=s[left] and len(queue)==0:
                queue.append(right)

            if s[right] not in current_count or current_count[s[right]]==0:
                current_count[s[right]]=1

            else:
                current_count[s[right]] += 1
                if current_count[s[right]] == k:
                    size+=1

            right+=1


        else:
            if size == len(set(s[left:right])):
                if left == None:
                    left = right

                maximum = max(maximum, right - left)

            if len(queue) != 0:
                if current_count[s[left]]>=3:
                    size-=1
                current_count[s[left]]=0
                left = queue.popleft()

            else:
                current_count[s[left]]=0
                right+=1
                left = right



    return len(s) if left == 0 else maximum



print(longestSubstring("baaabcb",3))