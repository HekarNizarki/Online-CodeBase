def maximalRectangle(matrix):
    if not matrix:
        return 0
    max_area=0
    dp=[0]*len(matrix[0])
    for row in matrix:
        for j in range(len(row)):
            dp[j]=dp[j]+1 if row[j]=='1' else 0
        stack=[]
        for i,h in enumerate(dp+[0]):
            while stack and h<dp[stack[-1]]:
                height=dp[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i)
    return max_area