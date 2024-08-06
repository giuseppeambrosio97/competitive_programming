from typing import List
import bisect
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        res = []

        for spell in spells:
            res.append(len(potions) - bisect.bisect_left(potions, math.ceil(success / spell)))

        return res


if __name__ == '__main__':
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    s = Solution().successfulPairs(spells=spells, potions=potions, success=success)
    print(s)