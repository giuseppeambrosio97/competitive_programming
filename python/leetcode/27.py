from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        k = 0
        while l <= r:
            if nums[l] != val:
                k += 1
            else:
                while l < r and nums[r] == val:
                    r -= 1
                if l < r and nums[r] != val:
                    nums[l], nums[r] = nums[r], nums[l]
                    k += 1
            l += 1
        return k


if __name__ == "__main__":
    nums = [2]
    val = 3
    s = Solution().removeElement(nums, val)
    print(nums[:s])
