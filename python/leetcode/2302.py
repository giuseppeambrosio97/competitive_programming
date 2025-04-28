from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = l = csum = 0
        for r in range(len(nums)):
            csum += nums[r]
            while csum * (r-l+1) >= k:
                csum -= nums[l]
                l += 1
            res += (r - l + 1)
        return res



if __name__ == "__main__":
    nums = [2,1,4,3,5]
    k = 10
    print(Solution().countSubarrays(nums, k))