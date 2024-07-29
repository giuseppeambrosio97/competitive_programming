from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        best = 0
        for i in range(0, len(gain)):
            prefix_sum += gain[i]
            best = max(best, prefix_sum)

        return best