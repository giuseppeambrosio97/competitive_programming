from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0]*3
        for a in nums:
            counter[a] += 1
        
        i = 0
        for color, count in enumerate(counter):
            for _ in range(count):
                nums[i] = color
                i += 1


if __name__ == "__main__":
    nums = [2]
    Solution().sortColors(nums)