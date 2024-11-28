from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        l, r, n = 0, 0, len(nums)

        while r < n:
            ## expand r until a new number is encountered after nums[r]
            ## if r - l == 1 -> nums[i] = nums[l] i++
            ## if r - l >= 2 -> nums[i],nums[i+1] = nums[l], nums[l+1] i +=2
            ## l = r
            while r < n and nums[l] == nums[r]:
                r+=1
            if r - l == 1:
                nums[i] = nums[l]
                i+=1
            else:
                nums[i],nums[i+1] = nums[l], nums[l+1]
                i+=2
            l = r
        return i

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    t = Solution().removeDuplicates(nums)
    print(t)