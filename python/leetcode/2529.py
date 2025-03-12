import bisect
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # cnt = defaultdict(int)

        # for n in nums:
        #     if n > 0:
        #         cnt[1]+=1
        #     elif n < 0:
        #         cnt[-1]+=1
        
        # return max(cnt[1],cnt[-1])
        i = bisect.bisect_left(nums, 0)
        l = len(nums) - bisect.bisect_left(nums, 1)
        return max(i,l)


if __name__ == "__main__":
    nums = [-3,-2,-1,1,2]
    Solution().maximumCount(nums)