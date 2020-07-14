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
        
        # Everytime we travel down a level path, we increase the depth.
        # Applied level order traversal. Increased the depth at each level.
        
        depth = 0
        
        if not root: return 0
        
        q = []
        
        q.append(root)
        
        while q:
            
            size = len(q)
            
            for i in range(size):
                
                node = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            depth+=1
        
        return depth
        
        