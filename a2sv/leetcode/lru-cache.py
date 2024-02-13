class LRUCache:
    class DoublyLinkedListNode:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.DoublyLinkedListNode(None, None)
        self.tail = self.DoublyLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                self._evict_last()
            node = self.DoublyLinkedListNode(key, value)
            self.cache[key] = node
            self._add_to_front(node)

    def _move_to_front(self, node: 'DoublyLinkedListNode') -> None:
        self._remove_node(node)
        self._add_to_front(node)

    def _add_to_front(self, node: 'DoublyLinkedListNode') -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: 'DoublyLinkedListNode') -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _evict_last(self) -> None:
        last_node = self.tail.prev
        del self.cache[last_node.key]
        self._remove_node(last_node)