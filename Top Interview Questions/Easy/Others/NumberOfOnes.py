class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        mask = 1
        
        for i in range(32):
            #print(bin(n), bin(mask), "AND ", str(n & mask))
            if n & mask != 0:
                count+=1
            mask = mask<<1
            
        return count