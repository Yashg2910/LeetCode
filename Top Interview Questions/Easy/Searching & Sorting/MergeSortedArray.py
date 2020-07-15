class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ## STARTING FROM THE END AND COMPARING BOTH THE ARRAYS

        first = m-1
        
        second = n-1
        
        i = m+n-1
        
        while i>=0:
            
            if second<0:
                break
            
            if nums1[first] > nums2[second] and first!=-1:
                print("Exec1")
                nums1[i] = nums1[first]
                first-=1
            else:
                print("Exec2")
                nums1[i] = nums2[second]
                second-=1
            
            
            i-=1
        
        
        
#         Input:
#         nums1 = [1,2,3,0,0,0], m = 3
#         nums2 = [2,5,6],       n = 3

#         Output: [1,2,2,3,5,6]