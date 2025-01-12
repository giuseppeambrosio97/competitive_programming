from collections import Counter, defaultdict
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        letter_mapping = defaultdict(list)
        nw = len(word)
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                letter_mapping[board[r][c]].append((r, c))
        
        ## prune if the string word has too many characters
        if nw > m*n:
            return False
        
        ## prune if the board do not contain at least the letter occurrence 
        wordcounter = Counter(word)
        for w, cnt in wordcounter.items():
            if len(letter_mapping[w]) < cnt:
                return False
            
        def backtrack(i, r, c, visited):
            if i >= nw:
                return True
            
            moves = [(1,0), (-1,0), (0,1), (0,-1)]
            childs = []
            for rr, cc in moves:
                rr, cc = r+rr, c+cc
                if 0 <= rr < m and 0 <= cc < n and (rr,cc) not in visited and board[rr][cc] == word[i]:
                    childs.append((rr,cc))
            
            if len(childs) == 0:
                return False
            
            return any([backtrack(i+1, r_, c_, visited | {(r_, c_)}) for r_, c_ in childs])
        

        for rs, cs in letter_mapping[word[0]]:
            if backtrack(1, rs,cs, set([(rs, cs)])):
                return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # board = [["A", "A"]]
    # word = "AAAAAAA"
    t = Solution().exist(board, word)
    print(t)
