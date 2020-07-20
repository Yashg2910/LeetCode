class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if (l < 1):
            return 0
        if (l == 1):
            return 1
        ans = 1
        start = 0
        chars = {}
        for end,char in enumerate(s):
            if char in chars:
                val = chars.get(char) + 1
                if (val > start):
                    start = val
            ans = end-start+1 if end-start+1 > ans else ans
            chars[char]=end
                
        return ans