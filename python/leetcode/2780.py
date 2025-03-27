from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find the dominant element in the entire array
        freq = defaultdict(int)
        dominant, max_count = -1, -1

        for num in nums:
            freq[num] += 1
            if freq[num] > max_count:
                dominant, max_count = num, freq[num]

        left_count = 0
        # Iterate and find the split point
        for i, num in enumerate(nums):
            if num == dominant:
                left_count += 1

            if left_count > (i + 1) // 2 and max_count - left_count > (len(nums) - (i + 1)) // 2:
                return i
        
        return -1
