from typing import List

def b_search(nums: List[int], l: int, r: int) -> int:
    m = (l + r) // 2

    prev = nums[m-1] if m - 1 >= 0 else float("-inf")
    succ = nums[m+1] if m + 1 < len(nums) else float("-inf")

    if prev < nums[m] and nums[m] > succ:
        return m
    elif prev < nums[m] < succ:
        return b_search(nums, m + 1, r)
    elif prev > nums[m] > succ:
        return b_search(nums, l, m - 1)
    else:
        return b_search(nums, l, m - 1)
    



class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        return b_search(nums, 0, len(nums) - 1)
    

if __name__ == '__main__':
    print(Solution().findPeakElement([1,3,1,2]))