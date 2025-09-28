from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        for i in range(N-1,1,-1):
            if nums[i-2]+nums[i-1]>nums[i]:
                return nums[i-2]+nums[i-1]+nums[i]
        return 0

if __name__ == "__main__":
    nums = [2,6,2,5,4,15,1]
    print(Solution().largestPerimeter(nums))