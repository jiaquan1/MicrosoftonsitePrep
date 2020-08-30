def minimummoves(arr):
    if not arr:
        return 0
    n = len(arr)
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for l in range(1,n+1):
        i = 0
        j = l-1
        while j<n:
            if l==1:
                dp[i][j]=1
            else:
                dp[i][j]=1+dp[i+1][j]
                if arr[i]==arr[i+1]:
                    dp[i][j]=min(dp[i][j],dp[i+2][j]+1)
                for k in range(i+2,j+1):
                    if arr[i]==arr[k]:
                        dp[i][j]=min(dp[i][j],dp[i+1][k-1]+dp[k+1][j])
            i +=1
            j +=1
    return dp[0][n-1]
if __name__=="__main__":
    str = "2553432"
    print( minimummoves(str)) 

            