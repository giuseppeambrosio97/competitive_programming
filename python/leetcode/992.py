from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        

        def atleastk(kp: int)->int:
            cnt = defaultdict(int)
            res = 0
            l = 0
            n = len(nums)

            for r in range(n):
                cnt[nums[r]] += 1
                while len(cnt) >= kp:
                    res += (n-r)
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        cnt.pop(nums[l])
                    l += 1
            return res


        return atleastk(k) - atleastk(k+1)


if __name__ == "__main__":
    nums = [1,2,1,2,3]
    k = 2
    print(Solution().subarraysWithKDistinct(nums, k))