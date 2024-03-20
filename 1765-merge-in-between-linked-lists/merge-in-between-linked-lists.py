# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aEnd,bEnd = list1,list1
        i = 0
        while i<=b and bEnd!=None:
            i+=1
            bEnd = bEnd.next
        i = 1
        while aEnd.next!=None:
            if i == a:
                aEnd.next = list2
            aEnd = aEnd.next
            i+=1
        
        aEnd.next = bEnd
        return list1