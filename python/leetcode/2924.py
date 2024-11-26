from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s = set([i for i in range(n)])
        st = set([e[1] for e in edges])
        s_st = s - st
        return next(iter(s_st)) if len(s_st) == 1 else - 1


if __name__ == "__main__":
    n = 4
    edges = [[0,2],[1,3],[1,2]]
    print(Solution().findChampion(n, edges))
