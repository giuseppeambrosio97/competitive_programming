from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """O(nlogn) + O(n^2)"""
        nums, n, res = sorted(nums), len(nums), []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ## two pointer to find all pairs of elements such that sum to -nums[i]
            l,r = i+1, n-1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return res   


if __name__ == '__main__':
    nums = [-2,0,0,2,2]
    t = Solution().threeSum(nums)
    print(t)

