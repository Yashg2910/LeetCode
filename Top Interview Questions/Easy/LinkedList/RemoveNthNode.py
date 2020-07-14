# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # 1->2->3->4->5 n=2
        # 1->2->3->5 
        # i.e.- length-n-2
        # 1->2 n=1 ans= [1]
        # 1->2 n=2 ans= [2] 
        
#         length = 1
        
#         temp = head
#         while temp.next!=None:
#             length+=1
#             temp = temp.next
            
        # print(length)
        
        temp = head
        
        fast = temp
        
        i=0
        while i<n:
            fast = fast.next
            i+=1
        
        if not fast:
            return head.next
        
        while fast.next!=None:
            temp= temp.next
            fast = fast.next
        
        if fast==None and temp==head:
            return head
        
        #deleting the element
        temp.next = temp.next.next
        
        return head