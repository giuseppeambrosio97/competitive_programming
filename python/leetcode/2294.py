from typing import List
import bisect as bs

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        prev = 0
        res = 0
        while prev < len(nums):
            prev = bs.bisect_left(nums, nums[prev]+k+1)
            res += 1
        return res



if __name__ == "__main__":
    nums = [2,2,4,5]
    k = 0
    print(Solution().partitionArray(nums, k))