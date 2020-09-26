class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        max_global = nums[0]
        
        for i in range(len(nums)):
            max_so_far +=nums[i]
            if max_so_far > max_global:
                max_global = max_so_far
            if max_so_far < 0:
                max_so_far = 0
           
                
        return max_global
