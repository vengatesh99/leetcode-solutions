# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,list1,list2):
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        mergeList = ListNode(-1)
        head = mergeList
        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
            print(head.val)
            head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return mergeList.next
    def getMid(self,head):
        hare,tort = head,head
        prev = hare
        while hare and hare.next:
            hare = hare.next.next
            prev = tort
            tort = tort.next
        prev.next = None
        return head,tort
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head1,head2 = self.getMid(head)
        left = self.sortList(head1)
        right = self.sortList(head2)
        merged = self.merge(left,right)
        return merged
        
        