import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        maxq = max(quantities)
        m = len(quantities)
        best = math.ceil(sum(quantities) / n)
    
        def is_good(guessedq: int) -> bool:
            r = 0
            for q in quantities:
                r += math.ceil(q / guessedq)
            return r <= n
        
        if n == m:
            return maxq
        
        if is_good(best):
            return best

        l, r = best, maxq
        while l <= r:
            guessed = (r + l) // 2
            is_gooodpp = is_good(guessed + 1)
            is_goodp = is_good(guessed)
            if is_gooodpp and not is_goodp:
                return guessed + 1
            elif not is_gooodpp and not is_goodp:
                l = guessed
            elif is_gooodpp and is_goodp:
                r = guessed 
        return guessed

if __name__ == '__main__':
    quantities = [25,11,29,6,24,4,29,18,6,13,25,30]
    n = 22

    a = Solution().minimizedMaximum(n, quantities)
    print(a)
