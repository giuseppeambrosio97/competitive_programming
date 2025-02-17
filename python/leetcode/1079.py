from collections import Counter, defaultdict
from typing import Dict


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter_capacity = Counter(tiles)
        res = [0]

        def backtrack(counter_used: Dict):
            for t in counter_capacity.keys():
                if counter_used[t] < counter_capacity[t]:
                    counter_used[t] += 1
                    res[0] += 1
                    backtrack(counter_used)
                    counter_used[t] -= 1

        backtrack(defaultdict(int))
        return res[0]
    
if __name__ == "__main__":
    tiles = "AAABBC"
    print(Solution().numTilePossibilities(tiles))