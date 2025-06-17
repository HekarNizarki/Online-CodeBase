def maxSlidingWindow(nums,k):
    from collections import deque
    q=deque()
    result=[]
    for i,num in enumerate(nums):
        while q and nums[q[-1]]<num:
            q.pop()
        q.append(i)
        if q[0]==i-k:
            q.popleft()
        if i>=k-1:
            result.append(nums[q[0]])
    return result