from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        l, r = 0, 1
        while r < n:
            if nums[r] > nums[l] and l + 1 < n:
                nums[l+1], nums[r] = nums[r], nums[l+1]
                l += 1
            r += 1

        return l+1


if __name__ == '__main__':
    nums = [1,1,2]
    s = Solution().removeDuplicates(nums)
    print(s)