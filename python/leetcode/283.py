from typing import List

class Solution:

    @staticmethod
    def move(nums, l, r):
        while l < r:
            nums[l], nums[l+1] = nums[l+1], nums[l]
            l += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        _n = len(nums)

        if _n == 1:
            return
        
        l = 0
        r = _n - 1
        
        # set r to the first non-zero position 
        while l < r and nums[r] == 0:
            r -=1

        while l < r:
            if nums[l] == 0:
                Solution.move(nums, l, r)
                r -= 1
            else:
                l += 1 
            

        

if __name__ == "__main__":
    s = Solution()

    a = [10,0,1,0,3,12]

    s.moveZeroes(a)

    print(a)