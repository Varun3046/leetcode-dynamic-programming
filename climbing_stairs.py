class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
# this problem is same as change problem
        if n == 0 or n== 1:
            return 1
        if n==2:
            return 2
        dp = [[0] for x in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        onestep = 0
        twostep =0
        
        
        for i in range(2,n+1):
            if i >=1:
                onestep = dp[i -1] 
            else:
                onestep=0
            if i >=2:
                twostep = dp[i-2] 
            else:
                twostep = 0
            dp[i] = onestep + twostep

        return dp[n]        
