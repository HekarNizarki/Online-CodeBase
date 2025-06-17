def firstUniqChar(s):
    from collections import Counter
    count=Counter(s)
    for i,char in enumerate(s):
        if count[char]==1:
            return i
    return -1