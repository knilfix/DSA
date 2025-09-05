from typing import Optional, List


class HashNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        pass


class MyHashMap:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.buckets: List[Optional[HashNode]] = [None] * capacity

    def _get_index(self, key):
        return hash(key) % self.capacity

    def get(self):
        pass

    def put(self, key, value):
        index = self._get_index(key)
        node = self.buckets[index]
        # space is empty so add item
        if node is None:
            self.buckets[index] = HashNode(key, value=value)
        else:
            current = node
            prev = None

            while current:
                if current.key == key:
                    current.value = value
                    return
                prev = current
                current = current.next

    def remove(self):
        pass
