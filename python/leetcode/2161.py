from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot]*len(nums)
        idxl, idxr = 0, n-1
        for i in range(n):
            if nums[i] < pivot:
                res[idxl] = nums[i]
                idxl+=1
            if nums[n-i-1] > pivot:
                res[idxr] = nums[n-i-1]
                idxr-=1
        return res
        

        # rs, rm, rl = [], [],[]
        # for n in nums:
        #     if n < pivot:
        #         rs.append(n)
        #     elif n > pivot:
        #         rl.append(n)
        #     else:
        #         rm.append(n)

        # return rs + rm + rl