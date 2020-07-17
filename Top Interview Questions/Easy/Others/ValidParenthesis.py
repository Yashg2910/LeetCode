class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for x in s:
            
            if not stack:
                stack.append(x)
            else:
                top = stack[-1]
                
                if (top=='{' and x == '}') or (top=='[' and x == ']') or (top=='(' and x == ')'):
                    stack.pop()
                else:
                    stack.append(x)  
        return len(stack)==0