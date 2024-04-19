# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast != None and fast.next != None :
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        second_head = slow.next
        slow.next = None
        prev = None
        node = second_head
        while node != None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        first_head = head
        second_head = prev
        while first_head and second_head:
            temp_first = first_head.next
            first_head.next = second_head
            temp_second = second_head.next
            second_head.next = temp_first
            second_head = temp_second
            first_head = temp_first
        
        return head
