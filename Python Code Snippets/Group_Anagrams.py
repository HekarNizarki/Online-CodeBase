def groupAnagrams(strs):
    from collections import defaultdict
    anagrams=defaultdict(list)
    for s in strs:
        key=''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())