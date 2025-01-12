# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        forward = head
        ans = 0
        def recurse(h):
            nonlocal forward,ans
            if not h:
                return
            recurse(h.next)
            ans = max(ans,forward.val+h.val)
            forward = forward.next
        recurse(head)
        return ans
