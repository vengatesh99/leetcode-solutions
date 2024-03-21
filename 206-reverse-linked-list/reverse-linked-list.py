# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node,next = head,head
        prev = None
        while node!=None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
