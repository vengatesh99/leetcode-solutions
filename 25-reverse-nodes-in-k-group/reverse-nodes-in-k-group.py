# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        final_head = prev_tail = ListNode(None)
        
        def count_nodes(head):
            temp = head
            len = 0
            while temp:
                len+=1
                temp = temp.next    
            return len
        
        def reverse(node):
            prev,head,next = None,node,None
            i = 0
            while head and i<k:
                next = head.next
                head.next = prev
                prev = head
                head = next
                i+=1
            return (prev,next)

        while head:
            len = count_nodes(head)
            if len>=k:
                new_tail = head
                new_head,next_head = reverse(head)
                if prev_tail:
                    prev_tail.next = new_head
                else:
                    final_head = new_head
                prev_tail = new_tail
            else:
                prev_tail.next = next_head
                break
            head = next_head
        return final_head.next