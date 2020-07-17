class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        
        mask = 1
        
        for i in range(32):
            if x & mask != y & mask:
                count+=1
                
            mask <<=1
            
        return count
        