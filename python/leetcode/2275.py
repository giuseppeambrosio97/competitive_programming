from typing import List
import math

MAX_N = 10**7

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        idxs = [0 for _ in range(math.floor(math.log2(MAX_N)) + 1)]
        
        max_ = -math.inf
        for a in candidates:
            bn = bin(a)[2:][::-1]

            for i, bni in enumerate(bn):
                if bni == "1":
                    idxs[i]+=1
                    max_ = max(max_, idxs[i])
        return max_



if __name__ == '__main__':
    print(Solution().largestCombination([
        16,17,
        # 71,
        62,
        # 12,
        24,
        # 14
        ]
    ))