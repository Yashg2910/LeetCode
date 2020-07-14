# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Everytime we travel down a level path, we increase the depth
        # Using Depth First Traversal, we return the level from both left and right
        # Compare them are return the max of both
        
        
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        
        right = self.maxDepth(root.right)
        
        return max(left, right)+1