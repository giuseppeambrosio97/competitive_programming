from typing import List

class Node:

    def __init__(self):
        self.end_node = False
        self.childs: List[Node] = [None for _ in range(26)]

    def __getitem__(self, letter) -> "Node":
        return self.childs[ord(letter)-97]
    
    def __setitem__(self, letter, node: "Node") -> None:
        self.childs[ord(letter)-97] = node

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """T(word) = len(word)"""
        current_node = self.root
        for idx, ch in enumerate(word):
            if current_node[ch] is None:
                current_node[ch] = Node()

            if idx == len(word) - 1:
                current_node[ch].end_node = True
            current_node = current_node[ch]
        

    def search(self, word: str) -> bool:
        """T(word) = len(word)""" 
        current_node = self.root
        for ch in word:
            if current_node[ch] is None:
                return False
            
            current_node = current_node[ch]
            
        return current_node.end_node
    

    def startsWith(self, prefix: str) -> bool:
        """T(word) = len(word)"""
        chs = list(prefix)
        current_node = self.root
        for ch in chs:
            if current_node[ch] is None:
                return False
            
            current_node = current_node[ch]
            
        return True


if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))  
    print(trie.search("app"))    
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
