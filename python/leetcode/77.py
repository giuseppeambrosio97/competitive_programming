from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def comb(start,combl) -> List[List[int]]:
            if len(combl) == k:
                return res.append(combl.copy())
            
            for i in range(start, n+1):
                combl.append(i)
                comb(i+1,combl)
                combl.pop()

        comb(1,[])
        return res

if __name__ == '__main__':
    n = 4
    k = 2
    t = Solution().combine(n,k)
    print(t)