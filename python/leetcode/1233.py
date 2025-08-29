from typing import Dict, List

class Node:
    def __init__(self, label: str, is_final: bool = False):
        self.label = label
        self.childs: Dict[str,Node] = {} 
        self.is_final = is_final

class Trie:
    def __init__(self):
        self.root = Node("*")

    def add(self, folder: str):
        parts = folder.strip("/").split("/")
        cnode = self.root
        for p in parts:
            if p not in cnode.childs:
                cnode.childs[p] = Node(label=p)
            cnode = cnode.childs[p]
        cnode.is_final = True
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)
        res = []
        def dfs(node: Node, parts: List[str]):
            if node.is_final:
                res.append("/" + "/".join(parts))
                return
            for cnode in node.childs.values():
                dfs(cnode, parts=parts+[cnode.label])
        dfs(trie.root, [])
        return res

if __name__ == "__main__":
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print(Solution().removeSubfolders(folder))