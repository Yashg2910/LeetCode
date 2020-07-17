class Solution(object):
    def romanToInt(self, x):
        """
        :type s: str
        :rtype: int
        """
        from_to = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        i = 0
        value = 0
        while i < len(x):
            current = from_to[x[i]]
            if i == 0:
                value += current
            else:
                last = from_to[x[i-1]]
                value += current if last >= current else (current - 2 * last)
            i += 1
        return value