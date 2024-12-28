from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, n = sorted(nums), len(nums)
        res = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, n - 1
                ctarget = target - (nums[i] + nums[j])
                while l < r:
                    current = nums[l] + nums[r]

                    if ctarget == current:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif current > ctarget:
                        r -= 1
                    else:
                        l += 1
        return res

if __name__ == '__main__':
    nums = [-2,-1,-1,1,1,2,2]
    target = 0
    r = Solution().fourSum(nums, target)
    print(r)