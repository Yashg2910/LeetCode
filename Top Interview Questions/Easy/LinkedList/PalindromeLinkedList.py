# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## USING STACK UP UNTIL THE HALF OF THE LIST
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # 1->2
        # 1->2->2->1
        
        if head == None:
            return True
        
        count = 0
        
        temp = head
        while temp!=None:
            count+=1
            temp = temp.next
        
        
        i=0
        
        stack = []
        
        temp = head
        while i<count/2:
            stack.append(temp.val)
            temp = temp.next
            i+=1
        
        if count%2==1:
            count -=1
            temp = temp.next
        
        
        while i<count:
            if temp.val!= stack.pop():
                return False
            i+=1
            temp = temp.next
        
        return True            