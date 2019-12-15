class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.curCap = 0
        self.cap = capacity
        self.tail = Node(0, 0)
        self.head = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        val = self.store[key].val
        self._remove(self.store[key])
        self._add(Node(key, val))
        return val

    def put(self, key: int, value: int) -> None:
        # remove the original if exists
        if key in self.store:
            self._remove(self.store[key])
        if self.curCap == self.cap:
            self._remove(self.tail.pre)
        self._add(Node(key, value))

    def _remove(self, Node):
        p, n = Node.pre, Node.nxt
        p.nxt, n.pre = n, p
        assert(Node.key in self.store)
        del self.store[Node.key]
        self.curCap -= 1

    def _add(self, Node):
        # add a node to the beginning
        tmp = self.head.nxt
        self.head.nxt = Node
        Node.nxt = tmp
        tmp.pre = Node
        Node.pre = self.head
        assert(Node.key not in self.store)
        self.store[Node.key] = Node
        self.curCap += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
