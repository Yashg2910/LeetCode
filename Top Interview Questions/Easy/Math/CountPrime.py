class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        isPrime = []
        
        isPrime.append(False)
        isPrime.append(False)
        
        for i in range(2, n):
            isPrime.append(True)
            
        i=2
        
        while i*i<n:
            
            if not isPrime[i]:
                pass
            else:
                j=i*i
                while j<n:
                    isPrime[j]= False
                    j+=i
            i+=1
            
        count = 0
        for num in isPrime:
            if num: count+=1
        return count