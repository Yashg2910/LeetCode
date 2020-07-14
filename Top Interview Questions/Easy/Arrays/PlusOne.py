class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        carry=0
        while i>=0:
            
            if i==0 and digits[i]==9:
                digits[i]=0
                digits.insert(0,1)
                break
                
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]=digits[i]+1
                break
            
            print(digits)
            i-=1
        
        return digits