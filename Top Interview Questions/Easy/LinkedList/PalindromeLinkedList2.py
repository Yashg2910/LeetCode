# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## REVERSING THE LIST AFTER HALF AND COMPARTING BOTH THE SIDES
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # 1->2
        # 1->2->2->1
        
        if head == None or head.next == None:
            return True
        
        count = 0
        
        slow = head
        fast = head
        
        # Counting until half of the list
        while fast!=None and fast.next!=None:
            count+=1
            slow=slow.next
            fast = fast.next.next
            
        
        # Reversing the second half of the list using slow
        
        curr = slow.next
        
        while curr!=None:
            temp = curr.next
            curr.next = slow
            slow = curr
            curr = temp
        
        for i in range(count):
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
            
        return True