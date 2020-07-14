class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx1 = 0
        
        for idx2 in range(1, len(nums)):
            
            if nums[idx1] == nums[idx2]:
                continue
            else:
                idx1 = idx1 + 1
                nums[idx1] = nums[idx2]
        
        return idx1+1