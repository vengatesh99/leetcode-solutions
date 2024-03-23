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
        fast,slow = head,head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        slowNext = slow.next
        slow.next = None
        slow = slowNext
        
        while slow!=None:
            next,slow.next, prev,  = slow.next, prev, slow
            slow = next
        
        curr = head
        while prev!=None:
            next = curr.next
            curr.next = prev
            next2 = prev.next
            prev.next = next
            curr = next 
            prev = next2
        return head