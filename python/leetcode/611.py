import bisect
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        # for i in range(N):
        #     for j in range(i+1,N):
        #         res += max(0,bisect.bisect_right(nums,x=nums[i]+nums[j]-1)-j-1)

        for k in range(N-1,-1,-1):
            i,j=0,k-1
            while i < j:
                if nums[i]+nums[j] > nums[k]:
                    res += (j-i) # fix j and the lowest side can be from i,i+1,...,j-1
                    j -= 1
                else:
                    i += 1
        return res

if __name__ == "__main__":
    nums = [1,2,2,3,4,4,5,6]
    print(Solution().triangleNumber(nums))