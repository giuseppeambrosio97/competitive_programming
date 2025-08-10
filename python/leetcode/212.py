from typing import List 


class Node:
    def __init__(self, ch: str):
        self.ch = ch
        self.neis = [None] * 26
        self.is_end = False
        self.word = None

chid = lambda ch: ord(ch) - ord("a")

def build_trie(words):
    root = Node("*")
    for w in words:
        cnode = root
        for ch in w:
            if cnode.neis[chid(ch)] is None:
                cnode.neis[chid(ch)] = Node(ch)
            cnode = cnode.neis[chid(ch)]
        cnode.is_end = True
        cnode.word = w
    return root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])

        words = [word for word in words if len(word) <= R*C]

        root = build_trie(words)
        tofound = set(words)
        found = set()
        visited = set()

        def dfs(r, c, cnode: Node):
            if not tofound:
                return
            if cnode is None:
                return
            if cnode.is_end:
                if cnode.word in tofound:
                    tofound.remove(cnode.word)
                found.add(cnode.word)
            
            visited.add((r,c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in visited:
                    nxt = cnode.neis[chid(board[nr][nc])]
                    if nxt is not None:
                        dfs(nr,nc,nxt)
            visited.remove((r,c))
            

        for r in range(R):
            for c in range(C):
                startnode = root.neis[chid(board[r][c])]
                if startnode is not None:
                    dfs(r, c, startnode)
                if not tofound:
                    return list(found)

        return list(found)


if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain","hklf", "hf"]
    print(Solution().findWords(board, words))
