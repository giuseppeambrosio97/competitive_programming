from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = deque()

        nt = len(temperatures)

        i = nt - 1
        sol = [0 for _ in range(nt)]
        while i >= 0:
            while len(s) != 0:
                if s[-1][0] > temperatures[i]:
                    sol[i] =  s[-1][1] - i
                    s.append((temperatures[i], i))
                    break
                else:
                    s.pop()
            else:
                s.append((temperatures[i], i))
            i -= 1
        
        return sol
            

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))