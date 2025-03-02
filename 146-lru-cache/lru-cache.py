class Node:
    def __init__(self,k=-1,v=-1):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.hm = {}
        self.sz = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def delete(self,todelete):
        prevNode = todelete.prev
        prevNode.next = todelete.next
        todelete.next.prev = prevNode
        self.sz-=1
        del self.hm[todelete.key]

    def add(self,toadd):
        curr = self.head.next
        self.head.next = toadd
        toadd.prev = self.head
        toadd.next = curr
        curr.prev = toadd
        self.sz+=1
        self.hm[toadd.key] = toadd

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.delete(node)
        self.add(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        toadd = Node(key,value)
        if key in self.hm:
            todel = self.hm[key]
            self.delete(todel)
        self.add(toadd)
        if self.sz>self.capacity:
            self.delete(self.tail.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)