from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        snums = sorted(nums)
        l = 0
        res = -1
        for r in range(len(snums)):
            if snums[r] - snums[l] > k*2:
                l += 1
            res = max(res, r-l+1)
        return res

if __name__ == '__main__':
    nums = [4,6,1,2]
    k = 2
    t = Solution().maximumBeauty(nums, k)
    print(t)