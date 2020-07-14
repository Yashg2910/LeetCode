# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.isMirror(root, root)
        
        return res
    
    def isMirror(self, r1, r2):
        
        if r1 is None and r2 is None:
            return True
        if r1 is None or r2 is None:
            return False
        
        return r1.val == r2.val and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)
    