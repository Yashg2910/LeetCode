class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        
        maxSize = 0
        
        currSize = 0
        
        dict = {}
        
        i=0
        while i < len(s):
            if s[i] not in dict.keys():
                dict[s[i]]= i
                currSize +=1
                if currSize>maxSize:
                    maxSize = currSize
                i+=1
            else:
                i = dict[s[i]]+1
                dict.clear()
                currSize = 0
                
        return maxSize