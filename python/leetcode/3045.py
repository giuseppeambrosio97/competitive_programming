
from typing import Dict, List, Tuple


class Node:
    def __init__(self):
        self.childs: Dict[Tuple[str,str], Node] = {}
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root: Node = Node()

    def add(self, w: str):
        n = len(w)
        curr = self.root
        for i in range(n):
            pair = (w[i], w[n-i-1])
            if pair not in curr.childs:
                curr.childs[pair] = Node()
            curr.childs[pair].cnt += 1
            curr = curr.childs[pair]

    def count(self, w: str) -> int:
        n = len(w)
        curr = self.root
        for i in range(n):
            pair = (w[i], w[n-i-1])
            if pair not in curr.childs:
                return 0
            curr = curr.childs[pair]
        return curr.cnt

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        T = Trie()
        n = len(words)
        res = 0
        for i in range(n):
            res += T.count(words[n-i-1])
            T.add(words[n-i-1])
        return res

if __name__ == '__main__':
    words = ["a","aba","ababa","aa"]
    t = Solution().countPrefixSuffixPairs(words)
    print(t)