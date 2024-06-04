# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            temp = node
            prev,next = None,None
            i = 0
            while i<k:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
                i+=1
            # print("reversed")
            return (prev,next)
        def count_nodes(node):
            temp = node
            len = 0
            print(node.val)
            while temp:
                temp = temp.next
                len+=1
            return len>=k
        def recursive_reverse(node):
            if node and count_nodes(node):
                new_head,next = reverse(node)
                node.next = recursive_reverse(next)
                return new_head
            return node
        return recursive_reverse(head)