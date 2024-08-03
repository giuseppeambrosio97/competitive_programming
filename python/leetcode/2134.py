from typing import List
import collections as cll

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        solution_length =  cll.Counter(nums)[1]

        if solution_length <= 1:
            return 0

        best = solution_length - sum(nums[:solution_length])
        prev_sum = best
        for i in range(1, len(nums)):
            left = -1 if nums[i-1] == 0 else 0
            right = 1 if nums[(i + solution_length - 1) % len(nums)] == 0 else 0
            current_solution_value = prev_sum + left + right
            best = min(best, current_solution_value)
            prev_sum = current_solution_value
        return best

if __name__ == '__main__':
    print("--->", Solution().minSwaps([0,1,0,1,1,0,0]))