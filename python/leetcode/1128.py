from collections import defaultdict
import math
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0

        counter = defaultdict(int)

        for d in dominoes:
            dd = sorted(d)
            strdd = str(dd)
            counter[strdd]+=1

        for k,v in counter.items():
            cnt += math.comb(v,2)
        
        return cnt
        


