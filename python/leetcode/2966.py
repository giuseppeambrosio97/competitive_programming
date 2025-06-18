from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(0,len(nums), 3):
            ll = nums[i:i+3]
            if ll[2] - ll[0] > k:
                return []
            res.append(ll)
        return res



if __name__ == "__main__":
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(Solution().divideArray(nums, k))