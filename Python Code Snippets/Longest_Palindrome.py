def longestPalindrome(s):
    from collections import Counter
    count=Counter(s)
    length=0
    odd_found=False
    for char,freq in count.items():
        if freq%2==0:
            length+=freq
        else:
            length+=freq-1
            odd_found=True
    return length+1 if odd_found else length