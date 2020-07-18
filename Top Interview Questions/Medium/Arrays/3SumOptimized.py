class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        size = len(nums)
        
        if size<3:
            return []
        
        nums.sort()
        
        result = []
        
        i=0
        
        while i<size-2:
            
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            
            left = i+1
            right = size-1
            
            while left<right:
                
                sum = nums[i]+nums[left]+nums[right]
                
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
            i+=1
        return result
            