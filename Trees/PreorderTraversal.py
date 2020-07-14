# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        if root == None:
            return res
        
        self.preorder(root, res)
        
        return res
    
    def preorder(self, root, res):
        if root==None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)