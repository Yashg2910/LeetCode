# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two pointer approach

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        if head is None or head.next is None:
            return False
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow==fast:
                return True
            
        return False