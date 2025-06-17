def combinationSum(candidates,target):
    result=[]
    def backtrack(start,path,remaining):
        if remaining==0:
            result.append(path)
            return
        for i in range(start,len(candidates)):
            if candidates[i]>remaining:
                continue
            backtrack(i,path+[candidates[i]],remaining-candidates[i])
    backtrack(0,[],target)
    return result