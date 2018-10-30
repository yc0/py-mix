class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if not key:
            return
        trie = self.trie
        for c in key:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return 0
            trie = trie[c]
        return self._dfs(trie)
    def _dfs(self,trie):
        v = 0 
        if '#' in trie:
            v += trie['#']
        v += sum([self._dfs(trie[child]) for child in trie if child != '#'])
        return v
# class MapSum:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

#     def insert(self, key, val):
#         """
#         :type key: str
#         :type val: int
#         :rtype: void
#         """
#         if not key:
#             return
#         cur = self.root
#         for c in key:
#             if c not in cur.hashing:
#                 cur.hashing[c] = TrieNode(cur)
#             cur = cur.hashing[c]
#             print("^", cur)
#         print(cur)
#         print(val)
#         cur.val = val
        
#     def sum(self, prefix):
#         """
#         :type prefix: str
#         :rtype: int
#         """
#         cur = self.root
#         from collections import deque
#         queue = deque()
#         _sum = 0
#         for c in prefix:
#             if c not in cur.hashing:
#                 return 0
#             else:
#                 cur = cur.hashing[c]
#                 print("->",cur)
        
#         queue.append(cur)
        
#         while queue:
#             v = queue.popleft()
#             print("V",v)
#             _sum += v.val
#             for c, child in v.hashing.items():
#                 queue.append(child)
            
#         return _sum
    
# class TrieNode:
#     def __init__(self, parent=None):
#         self.hashing = {}
#         self.next = None
#         self.parent = parent
#         self.val = 0

if __name__ == "__main__":
    ms = MapSum()
    ms.insert("apple",3)
    assert ms.sum("ap") == 3
    ms.insert("app", 2)
    assert ms.sum("ap") == 5
    print("passed all")
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)