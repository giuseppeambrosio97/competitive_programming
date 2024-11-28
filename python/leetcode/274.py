from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        cnt = 0
        for i in range(n-1,-1, -1):
            if n-i <= citations[i]:
                cnt += 1
        return cnt

if __name__ == '__main__':
    citations = [4,4,0,0]
    t = Solution().hIndex(citations)
    print(t)