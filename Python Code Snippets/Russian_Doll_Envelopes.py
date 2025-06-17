def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x:(x[0],-x[1]))
    dp=[]
    for _,height in envelopes:
        left,right=0,len(dp)
        while left<right:
            mid=(left+right)//2
            if dp[mid]<height:
                left=mid+1
            else:
                right=mid
        if right==len(dp):
            dp.append(height)
        else:
            dp[right]=height
    return len(dp)