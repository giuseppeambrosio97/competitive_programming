from typing import Optional


class Node:
    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional["Node"] = None,
        succ: Optional["Node"] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.succ = succ

    @property
    def is_tail(self):
        return self.succ is None

    @property
    def is_head(self):
        return self.prev is None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"""key: {self.key}
value: {self.value}
prev: {self.prev.key if self.prev else None}
succ: {self.succ.key if self.succ else None}
"""


class LRUCache:
    @property
    def is_full(self):
        return len(self.map) == self.capacity

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        """
        Get the element and update the LRU logic
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        if node.is_head:
            return node.value
        ## remove from the linked list
        if node.is_tail:
            self.tail = node.prev
            self.tail.succ = None
        else:
            node.succ.prev = node.prev
            node.prev.succ = node.succ
        ## add in head
        node.prev = None
        node.succ = self.head
        self.head.prev = node
        self.head = node
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        if is full and key not in self.map -> evict
        else add the element and

        update the LRU logic
        """
        if key in self.map:
            node = self.map[key]
            node.value = value
            if node.is_head:
                return
            ## remove from the linked list
            if node.is_tail:
                self.tail = node.prev
                self.tail.succ = None
            else:
                node.succ.prev = node.prev
                node.prev.succ = node.succ
            ## add in head
            node.prev = None
            node.succ = self.head
            self.head.prev = node
            self.head = node
        else:
            if self.is_full:
                del self.map[self.tail.key]
                if self.tail.is_head:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.succ = None
            node = Node(key=key, value=value)
            node.succ = self.head
            if self.head:
                self.head.prev = node
            self.head = node

            if not self.tail:
                self.tail = node
            self.map[key] = node

    def __str__(self):
        return f"""map: {self.map}
len(map): {len(self.map)}
head: {self.head}
tail: {self.tail}
"""


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    obj = LRUCache(3)
    obj.put(1, 1)
    print(obj)
    print("*" * 100)
    obj.put(2, 2)
    print(obj)
    print("*" * 100)
    obj.put(3, 3)
    obj.get(1)

    obj.put(4, 4)
    print("CIAO")
