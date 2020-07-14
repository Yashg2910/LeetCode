# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        temp = None
        l3 = None
        
        if l1==None:
            return l2
        if l2==None:
            return l1
        
        if l1.val <=l2.val:
            l3 = l1
            l1=l1.next
        else:
            l3=l2
            l2=l2.next
        
        temp =l3
        
        while l1!=None or l2!=None:
            
            if l1==None:
                temp.next = l2
                break
            
            if l2==None:
                temp.next =l1
                break
            
            print(l1.val, l2.val, temp)
            
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next=l2
                l2=l2.next
                temp = temp.next
                
        return l3