from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([(0 if len(str(n)) & 1 else 1) for n in nums ])