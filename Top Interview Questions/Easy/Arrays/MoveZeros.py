class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #[0,1,0,3,12] => [1,3,12,0,0]
        
        n = len(nums)
        
        j=0
        for i in range(0, n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        
        while j<n:
            nums[j]=0
            j+=1