class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [2,2,1] [4,1,2,1,2]
        
        total = sum(nums)
        
        num_set = set(nums)
        
        total_set = sum(num_set)
        
        num = (total_set*2)-total
        
        return num