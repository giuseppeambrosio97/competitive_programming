from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(list)

        for idx,a in enumerate(nums):
            mapp[a].append(idx)
            
        cnt = 0
        for ky, v in mapp.items():
            if len(v) > 1:
                for i in range(len(v)):
                    for j in range(i+1,len(v)):
                        if (v[i]*v[j]) % k == 0:
                            cnt += 1
        return cnt
