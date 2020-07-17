class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        hash_array = [None]*(size+1)
        
        for x in nums:
            hash_array[x]=1
        
        print(hash_array)
        for i in range(size+1):
            if hash_array[i]==None:
                return i
        return None