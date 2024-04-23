# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(-1)
        head = output
        carry = 0

        while l1 or l2:
            first_val = 0
            second_val = 0
            if l1:
                first_val = l1.val
            if l2:
                second_val = l2.val
            num = first_val + second_val + carry
            if num >= 10:
                carry = 1
                num-=10
            else:
                carry = 0
            
            output.next = ListNode(num)
            output = output.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            output.next = ListNode(1)
        return head.next







