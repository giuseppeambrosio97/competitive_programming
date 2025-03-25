from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted([(r[0], r[2]) for r in rectangles])
        y = sorted([(r[1], r[3]) for r in rectangles])

        def cnt_non_overlap(arr):
            cnt = 0
            prevend = -1 
            for start, end in arr:
                if prevend <= start:
                    cnt += 1
                prevend = max(prevend, end)
            return cnt
        
        return max(cnt_non_overlap(x), cnt_non_overlap(y)) >= 3

if __name__ == "__main__":
    n = 5
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    Solution().checkValidCuts(n, rectangles)