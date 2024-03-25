# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        node = head
        length = 0
        while node != None:
            length+=1
            node = node.next
        
        part_length = length // k
        remainder = length % k
        output = []
        node = head
        curr_part_length = int(node != None)
        curr_part_head = node
        while node != None or len(output) < k:

            if curr_part_length == part_length + int(remainder > 0):
                output.append(curr_part_head)
                if node:
                    curr_part_head = node.next
                    node.next = None
                
                if remainder > 0:
                    remainder-=1
                node = curr_part_head
                curr_part_length= int(node != None)
            else:
                node = node.next
                curr_part_length+=1
        return output