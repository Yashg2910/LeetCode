class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        
        dp = []
        
        dp.append(nums[0])
        
        dp.append(max(nums[0],nums[1]))
        
        for i in range(2, n):
            maximum = max(dp[i-1], dp[i-2]+nums[i])
            dp.append(maximum)
            
        return dp[n-1]