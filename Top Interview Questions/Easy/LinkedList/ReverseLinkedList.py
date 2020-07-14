# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## ITERATIVE APPROACH

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 1->2->3->4->5->NULL
        #
        # 5->4->3->2->1->NULL        

        curr = head
        prev = None
        
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev