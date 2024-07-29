from typing import List

class Node:

    def __init__(self):
        self.end_node = False
        self.childs: List[Node] = [None for _ in range(26)]

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """T(word) = len(word)"""
        chs = list(word)
        current_node = self.root
        for idx, ch in enumerate(chs):
            if current_node.childs[ord(ch)- 97] is None:
                current_node.childs[ord(ch)- 97] = Node()

            if idx == len(chs) - 1:
                current_node.childs[ord(ch)- 97].end_node = True
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


if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))  
    print(trie.search("app"))    
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
