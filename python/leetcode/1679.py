from typing import List
import bisect

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        l = 0
        r = bisect.bisect_left(sorted_nums, k)
        count = 0
        while l < r:
            cs = sorted_nums[l] + sorted_nums[min(r, len(sorted_nums)-1)]
            if cs == k:
                count += 1
                r -= 1
                l +=1
            elif cs < k:
                l += 1
            else:
                r -= 1
        return count



if __name__ == '__main__':
    nums = [3,1,3,4,3]
    k = 6
    print(Solution().maxOperations(nums=nums, k=k))