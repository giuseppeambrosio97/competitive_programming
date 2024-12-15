import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        nc = len(classes)
        cprs = [
            (-((c[0] + 1) / (c[1] + 1) - (c[0] / c[1])), c[0] / c[1], c[0], c[1])
            for c in classes
        ]
        res = sum([c[1] for c in cprs]) / nc
        heapq.heapify(cprs)
        for _ in range(extraStudents):
            delta, r, p,t = heapq.heappop(cprs)
            res -= delta/nc
            heapq.heappush(
                cprs,
                (-((p+2)/(t+2)-(p+1)/(t+1)),
                (p+1)/(t+1),
                p+1,
                t+1,)
            )
        return res


if __name__ == "__main__":
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    t = Solution().maxAverageRatio(classes, extraStudents)
    print(t)
