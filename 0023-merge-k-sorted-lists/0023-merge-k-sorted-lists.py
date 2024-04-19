# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        node = lists[0]
        for node_to_merge in lists[1:]:
            head = node
            prev = None
            while node is not None and node_to_merge is not None:
                if node_to_merge.val < node.val:
                    temp = node_to_merge.next
                    if head == node:
                        head = node_to_merge
                    else:
                        prev.next = node_to_merge
                    node_to_merge.next = node
                    prev = node_to_merge
                    node_to_merge = temp
                else:
                    prev = node
                    node = node.next
            if node_to_merge:
                prev.next = node_to_merge
                
            node = head
        return node




