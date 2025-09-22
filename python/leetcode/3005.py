from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        maxf = 0
        for n in nums:
            cnt[n]+=1
            maxf = max(maxf, cnt[n])
        res = 0
        for v in cnt.values():
            if v == maxf:
                res += v
        return res




if __name__ == "__main__":
    nums = [1,2,2,3,1,4]
    print(Solution().maxFrequencyElements(nums))