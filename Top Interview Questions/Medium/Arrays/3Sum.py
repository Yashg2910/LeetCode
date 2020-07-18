## BRUTE FORCE. TLE!!!!! 

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
            j=i+1
            while j<size-1:
                k=j+1
                while k<size:
                    sum = nums[i]+nums[j]+nums[k]
                    if sum==0:
                        if [nums[i],nums[j],nums[k]] not in result:
                            result.append([nums[i],nums[j],nums[k]])
                    k+=1
                j+=1
            i+=1
            
        return result