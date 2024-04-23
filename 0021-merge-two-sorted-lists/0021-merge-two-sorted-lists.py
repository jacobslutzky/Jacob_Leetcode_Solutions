# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = list1
        prev = None
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                if prev == None:
                    head = list2
                else:
                    prev.next = list2
                temp = list2.next
                prev = list2
                list2.next = list1
                list2 = temp
        if list2:
            if prev:
                prev.next = list2
            else:
                head = list2
        return head

         