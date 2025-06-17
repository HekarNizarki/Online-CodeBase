def minWindow(s,t):
    from collections import Counter
    target_counts=Counter(t)
    required=len(target_counts)
    formed=0
    window_counts={}
    left=right=0
    min_length=float('inf')
    result=''
    while right<len(s):
        char=s[right]
        window_counts[char]=window_counts.get(char,0)+1
        if char in target_counts and window_counts[char]==target_counts[char]:
            formed+=1
        while left<=right and formed==required:
            char=s[left]
            if right-left+1<min_length:
                min_length=right-left+1
                result=s[left:right+1]
            window_counts[char]-=1
            if char in target_counts and window_counts[char]<target_counts[char]:
                formed-=1
            left+=1
        right+=1
    return result