class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        
        for word in strs:
            anagram = False
            index = None
            
            if not res:
                res.append([word])
                continue
            
            for i,x in enumerate(res):
                if self.isAnagram(word, res[i][0]):
                    anagram=True
                    index = i
                    break
            
            if anagram==True:
                res[index].append(word)
            else:
                res.append([word])
                
            
        
        return res
    
    def isAnagram(self,str1, str2):
        dict = {}
        
        for s in str1:
            dict[s] = dict.get(s,0)+1
        
        for s in str2:
            if s in dict.keys():
                dict[s]-=1
                if dict[s]==0:
                    del dict[s]
            else:
                return False
        
        return len(dict)==0