from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
    
        def back(idx: int, v: int = 0):
            if idx == N:
                return v
            return back(idx+1, v^nums[idx]) + back(idx+1,v)    
    
        return back(0)


if __name__ == "__main__":
    nums = [5,1,6]
    print(Solution().subsetXORSum(nums))