# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number,len = 0,0
        head2,newHead = head,ListNode(None)
        while head2!=None:
            val = head2.val
            number = number*10+val
            head2 = head2.next
            len+=1
        ans = newHead

        number = number*2

        if number == 0:
            return ListNode(0)
        while number!=0:
            remainder = number%10
            number//=10
            node = ListNode(remainder,None)
            newHead.next = node
            newHead = newHead.next
        ans = ans.next
        start = ans
        prev=None
        next=None
        while start!=None:
            next = start.next
            start.next = prev
            prev = start
            start = next
        return prev
