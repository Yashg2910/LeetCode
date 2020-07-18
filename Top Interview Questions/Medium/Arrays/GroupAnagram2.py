### Sorting every word and mapping to the dictionary.
class Solution(object):
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        
        for word in strs:
            key = tuple(sorted(word))
            hashmap[key] = hashmap.get(key, [])+[word]
            
        return hashmap.values()