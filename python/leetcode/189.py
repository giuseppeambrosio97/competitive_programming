from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """O(n)=S(n)."""
        # c = nums.copy()

        # for i in range(len(c)):
        #     c[(i+k)%len(c)] = nums[i]

        # for i in range(len(c)):
        #     nums[i] = c[i]
        """O(1)=S(n)."""
        n = len(nums)
        k = k % n
        def reversea(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        reversea(0, n-1)
        reversea(0, k - 1)
        reversea(k,n-1)


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    k = 4
    Solution().rotate(nums, k)
    print(nums)
