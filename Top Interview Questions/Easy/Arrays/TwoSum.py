class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [2,7,11,15] target = 9, (2+7) return [0,1]
        # TWO POINTER APPROACH
        # HashMap
        
        dictionary = {}
        
        for i,v in enumerate(nums):
            temp = target-v
            
            if temp in dictionary:
                return [dictionary[temp], i]
            else:
                dictionary[v]=i