def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m,n=len(matrix),len(matrix[0])
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    dp=[[0]*n for _ in range(m)]
    def dfs(i,j):
        if dp[i][j]:
            return dp[i][j]
        max_length=1
        for dx,dy in directions:
            x,y=i+dx,j+dy
            if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[i][j]:
                max_length=max(max_length,1+dfs(x,y))
        dp[i][j]=max_length
        return dp[i][j]
    result=0
    for i in range(m):
        for j in range(n):
            result=max(result,dfs(i,j))
    return result