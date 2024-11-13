from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        cnt = 0
        while l < r:
            if nums[l] + nums[r] < target:
                cnt += (r - l)
                l += 1
            else:
                r -= 1
        return cnt
            

if __name__ == '__main__':

    nums = [-6,2,5,-2,-7,-1,3]
    target = -2
    s = Solution().countPairs(nums, target)
    print(s)