class Solution(object):
    def reverse(self, num):
        num.reverse()

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        if k == 0: return 
        new_nums = nums[-k:] + nums[:(n-k)]
        
        nums[:] = new_nums