"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flattenHelper(self,node,previous):
        if node == None:
            return None
        # if node.next == None:
        #     previous = node
        head = node
        while node is not None:
            nextNode = node.next
            newNext = self.flattenHelper(node.child,previous)
            newNextEnd = None
            newNextDummy = newNext
            while newNextDummy!=None:
                newNextEnd = newNextDummy
                newNextDummy = newNextDummy.next
            if newNext != None:
                newNext.prev = node
                node.next = newNext
                newNext.child = None
                node.child = None
            if nextNode != None and newNextEnd != None:
                nextNode.prev = newNextEnd
                newNextEnd.next = nextNode
            node = nextNode
        return head
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head = self.flattenHelper(head,None)
        # head2 = head
        # while head2!=None:
        #     if head2.child is not None:
        #         print("Yes",head2.child.val)
        #     print(head2.val,"->")
        #     head2 = head2.next
        return head