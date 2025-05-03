from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x: int) -> int:
            tswap = bswap = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    tswap += 1
                elif bottoms[i] != x:
                    bswap += 1
            return min(tswap, bswap)
        
        t = check(tops[0])
        if t != -1:
            return t
        if tops[0] != bottoms[0]:
            return check(bottoms[0])
        return -1


if __name__ == "__main__":
    tops = [1,2,1,1,1,2,2,2]
    bottoms = [2,1,2,2,2,2,2,2]
    print(Solution().minDominoRotations(tops, bottoms))