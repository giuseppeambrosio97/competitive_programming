from collections import defaultdict
from typing import List
import math

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                mp[nums[i]*nums[j]].append((nums[i], nums[j]))

        res = 0
        for v in mp.values():
            if len(v) > 1:
                res += math.comb(len(v), 2)*8
        return res


if __name__ == '__main__':
    nums = [2,3,4,6]
    Solution().tupleSameProduct(nums)