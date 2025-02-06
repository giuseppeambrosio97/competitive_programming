from collections import defaultdict
from typing import List
import math

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                mp[nums[i]*nums[j]]+= 1

        res = 0
        for v in mp.values():
            if v > 1:
                res += math.comb(v, 2)*8
        return res


if __name__ == '__main__':
    nums = [2,3,4,6]
    Solution().tupleSameProduct(nums)