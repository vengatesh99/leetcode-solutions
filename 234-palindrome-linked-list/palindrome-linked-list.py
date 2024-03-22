# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    global head2
    def checkPalindrome(self,head1):
        global head2
        if head1==None:
            return True
        check = self.checkPalindrome(head1.next)
        if not check:
            return False
        if head1.val == head2.val:
            head2 = head2.next
            return True
        else:
            return False
        return  check

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global head2 
        head2 = head
        return self.checkPalindrome(head)