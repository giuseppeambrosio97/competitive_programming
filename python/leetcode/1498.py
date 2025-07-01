from typing import List
import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        N = len(nums)
        pow2 = [1]*N
        for i in range(1,N):
            pow2[i] = 2*pow2[i-1]

        # T(n) = nlogn + n + n*nlogn
        # S(n) = O(n)
        # res = 0
        # for i in range(len(nums)):
        #     tt = target - nums[i]
        #     if tt >= nums[i]:
        #         l = bisect.bisect_right(nums, tt, lo=i+1) - i
        #         res += pow2[l-1]
        #         res %= MOD
        # return res

        res = 0
        l, r = 0, N-1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res += pow2[r-l]
                res %= MOD
                l += 1
            else:
                r -= 1
        return res


if __name__ == "__main__":
    nums = [2,3,3,4,6,7]
    target = 12
    print(Solution().numSubseq(nums, target))