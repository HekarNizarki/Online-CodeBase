def countSmaller(nums):
    def merge_sort(enums):
        if len(enums)<=1:
            return enums
        mid=len(enums)//2
        left=merge_sort(enums[:mid])
        right=merge_sort(enums[mid:])
        merged=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i][1]<=right[j][1]:
                merged.append(left[i])
                counts[left[i][0]]+=j
                i+=1
            else:
                merged.append(right[j])
                j+=1
        merged.extend(left[i:])
        for k in range(i,len(left)):
            counts[left[k][0]]+=j
        merged.extend(right[j:])
        return merged
    counts=[0]*len(nums)
    merge_sort(list(enumerate(nums)))
    return counts