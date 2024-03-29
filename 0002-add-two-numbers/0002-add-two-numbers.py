# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_list = ListNode()
        head = new_list
        while l1 != None or l2 != None or carry != 0:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            val = l1.val + l2.val + carry
            
            if val >= 10:
                val -= 10
                carry = 1
            else:
                carry = 0
            new_list.val = val
            
            if l1.next or l2.next or carry != 0:
                new_list.next = ListNode()
                new_list = new_list.next
                
            
            l1 = l1.next
            l2 = l2.next
    
        return head
        
            

