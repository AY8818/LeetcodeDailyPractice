def minimumTotal(triangle):
    tLen = len(triangle)
    dp = [[0]*(tLen+1) for i in range(tLen+1)]
    for level in range(tLen - 1,-1,-1):
        for col in range(level + 1):
            dp[level][col] = triangle[level][col] + min(dp[level+1][col],dp[level+1][col+1])

    return dp[0][0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))
