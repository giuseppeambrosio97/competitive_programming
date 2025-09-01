import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        N = len(classes)
        # class_pass_ratios
        cprs = [(-((p + 1) / (t + 1) - p / t), p / t, p, t) for p, t in classes]
        res = sum([cp[1] for cp in cprs]) / N
        heapq.heapify(cprs)
        for _ in range(extraStudents):
            delta, _, p, t = heapq.heappop(cprs)
            p += 1
            t += 1
            res -= delta/N
            heapq.heappush(cprs, (-((p + 1) / (t + 1) - p / t), p / t, p, t))
        return res


if __name__ == "__main__":
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    t = Solution().maxAverageRatio(classes, extraStudents)
    print(t)
