''' 
four line solution
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*(len(nums)+2)
        for i in reversed(range(len(nums))):
            dp[i] = max(dp[i+2]+nums[i],dp[i+1])
        return dp[0]
