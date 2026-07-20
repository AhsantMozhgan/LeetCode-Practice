# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        bucket_index = self._hash(key)
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)
        
    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)
        
    def contains(self, key: int) -> bool:
        bucket_index = self._hash(key)
        return key in self.buckets[bucket_index]