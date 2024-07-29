from typing import List

class Node:

    def __init__(self, ch: str = None):
        self.ch = ch or ""
        self.frequency = 0
        self.childs: List[Node] = [None for _ in range(26)]

    @property
    def end_node(self):
        return self.frequency >= 1

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """T(word) = len(word)"""
        chs = list(word)
        current_node = self.root
        for idx, ch in enumerate(chs):
            if current_node.childs[ord(ch)- 97] is None:
                current_node.childs[ord(ch)- 97] = Node(ch=ch)

            if idx == len(chs) - 1:
                current_node.childs[ord(ch)- 97].frequency += 1
            current_node = current_node.childs[ord(ch)- 97]
        

    def search(self, word: str) -> bool:
        """T(word) = len(word)"""       
        chs = list(word)
        current_node = self.root
        for ch in chs:
            if current_node.childs[ord(ch)- 97] is None:
                return False
            
            current_node = current_node.childs[ord(ch)- 97]
            
        return current_node.end_node
    

    def startsWith(self, prefix: str) -> bool:
        """T(word) = len(word)"""
        chs = list(prefix)
        current_node = self.root
        for ch in chs:
            if current_node.childs[ord(ch)- 97] is None:
                return False
            
            current_node = current_node.childs[ord(ch)- 97]
            
        return True
    
    @staticmethod
    def recommend_3(a: Node, top_3: List[str], current_word: str) -> None:
        """
        Find the top 3 words (in lexicographically order) starting from the node a and so that has the path from root 
        to a node prefix
        """
        if not a:
            return 
        
        if len(top_3) >= 3:
            return
        
        if a.end_node:
            top_3 += [current_word for _ in range(min(a.frequency, 3 - len(top_3)))]

        for child in a.childs:
            if child is not None:
                Trie.recommend_3(child, top_3, current_word + child.ch)        
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        res = []

        chs = list(searchWord)
        prefix = ""
        current_node = trie.root
        for ch in chs:
            prefix += ch
            top_3_prefix = []

            if current_node is not None and current_node.childs[ord(ch)- 97] is not None:
                Trie.recommend_3(current_node.childs[ord(ch)- 97], top_3_prefix, prefix)  
            res.append(top_3_prefix)
            if current_node is not None:
                current_node = current_node.childs[ord(ch)- 97]

        return res

   


if __name__ == '__main__':
    res = Solution().suggestedProducts(products=["havana"], searchWord="havana")
    print(res)
