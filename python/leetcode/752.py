from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """T(n)=O(10*10*10*10)=S(n)."""
        deadendsset = set(deadends)

        if "0000" in deadendsset:
            return -1

        def str_replace(s: str, i: int, ch: int):
            return s[:i] + str(ch) + s[(i+1):]
        
        def ng(state: str) -> List[str]:
            ng_ = []
            for i, s in enumerate(state):
                succ = (int(s) + 1) % 10
                succstate = str_replace(state, i, succ)
                if succstate not in deadendsset:
                    ng_.append(succstate)
                prev = (int(s) - 1) % 10
                prevstate = str_replace(state,i,prev)
                if prevstate not in deadendsset:
                    ng_.append(prevstate)
            return ng_
        
        q = deque([("0000", 0)])
        prevstates = set(["0000"])

        while q:
            s, dp = q.popleft()
            if s == target:
                return dp

            for sng in ng(s):
                if sng not in prevstates:
                    prevstates.add(sng)
                    q.append((sng, dp+1))
        
        return -1
        

if __name__ == '__main__':
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    s = Solution().openLock(deadends, target)
    print(s)