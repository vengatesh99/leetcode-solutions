# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(-1)
        ans = res
        hm = {}
        minheap = []
        i = 0
        n = len(lists)
        visit = set()
        while len(visit)<n:
            curr_head = lists[i]
            if curr_head:
                heapq.heappush(minheap,curr_head.val)
                lists[i] = curr_head.next
            else:
                visit.add(i)
            if i+1 == n and minheap:
                addNode = ListNode(heapq.heappop(minheap))
                res.next = addNode
                res = res.next
            i = (i+1)%n
        while minheap:
            addNode = ListNode(heapq.heappop(minheap))
            res.next = addNode
            res = res.next
        return ans.next


"""
minheap => minimum among the lot in nlogn
index that cyclens around the length of lists and pick the corrrect list for processing
takes the elemtn, adds to the minheap, moves to the next list. 
"""