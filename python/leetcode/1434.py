from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9+7
        mapping = defaultdict(list)
        for person, person_hats in enumerate(hats):
            for hat in person_hats:
                mapping[hat].append(person)
        mapping = list(mapping.items())
        TARGET_MASK = (1 << len(hats)) - 1
        @lru_cache(maxsize=None)
        def dfs(hatid: int, mask: int):
            if mask == TARGET_MASK:
                return 1
            if hatid >= len(mapping):
                return 0
            tmp = 0
            tmp += dfs(hatid+1, mask) # don't take the hat with hatid
            for i in mapping[hatid][1]:
                if mask & (1<<i):
                    continue
                tmp += dfs(hatid+1, mask | (1<<i))
            return tmp % MOD
        return dfs(0,0)


if __name__ == "__main__":
    hats = [[3,4],[4,5],[5]]
    Solution().numberWays(hats)