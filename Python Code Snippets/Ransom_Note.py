def canConstruct(ransomNote,magazine):
    from collections import Counter
    return not Counter(ransomNote)-Counter(magazine)