# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__ (self):
        
        self.result = []
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ## Perform an Inorder traversal to result in a sorted array.
        ## if array not sorted. return false else return true
        
        self.InOrder(root)
        
        print(self.result)
        
        for i in range(len(self.result)-1):
            if self.result[i+1] <= self.result[i]:
                return False
            
        return True
    
    def InOrder(self, root):
        
        if root==None:
            return
        
        self.InOrder(root.left)
        
        self.result.append(root.val)
        
        self.InOrder(root.right)
        
        
        