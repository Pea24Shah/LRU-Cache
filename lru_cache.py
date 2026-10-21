class Node:
    """One entry in the doubly linked list."""

    def __init__(self, key, value):
        self.key = key  # kept so we can delete it from the dict on eviction
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.cache = {}  # key -> Node, for O(1) lookup
        # Dummy nodes so we never have to handle an empty list specially.
        # head.next is the most recently used, tail.prev the least.
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Unlink node by pointing its neighbors at each other.
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        # Insert node right after head (the most recent spot).
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Using a key makes it the most recent, so move it to the front.
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Existing key: update the value and mark it most recent.
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        # New key: add it at the front.
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        if len(self.cache) > self.capacity:
            # Too many items: evict the least recent one (just before tail).
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, "A"); c.put(2, "B")
    print(c.get(1))  # A
    c.put(3, "C")    # evicts 2, the least recently used
    print(c.get(2))  # -1
    print(c.get(3))  # C
