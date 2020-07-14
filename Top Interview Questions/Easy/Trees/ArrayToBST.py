# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums)==0:
            return None
        
        root = self.constructTree(nums, 0, len(nums)-1)
        
        return root
        
    def constructTree(self, nums, low, high):
        
        if low>high:
            return None
        
        
        ## FINDING MID IS TRICKY! 
        mid = (low + high)//2
        
        if (low + high) % 2 == 1: 
            mid += randint(0, 1)
        
        node = TreeNode(nums[mid])
        
        print(node.val)
        
        node.left = self.constructTree(nums, low, mid-1)
        node.right = self.constructTree(nums, mid+1, high)
        
        return node
        