class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        result = 0
        mask = 1
        
        for i in range(32):
            result = (result<<1) | (n & mask)
            n >>= 1
        return result