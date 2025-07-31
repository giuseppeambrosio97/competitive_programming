from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = {0}
        for n in arr:
            curr = { n | nn for nn in curr } | { n }
            res |= curr
        return len(res)