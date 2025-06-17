def findTheDifference(s,t):
    from collections import Counter
    return list((Counter(t)-Counter(s)).keys())[0]