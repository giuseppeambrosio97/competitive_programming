from typing import List


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        N = len(startTime)
        best = 0
        psum = [0] * (N+1)

        for i in range(N):
            psum[i+1] = psum[i] + (endTime[i] - startTime[i])

        for i in range(k-1, N):
            r = eventTime if i == N-1 else startTime[i+1]
            l = 0 if i == k-1 else endTime[i-k]
            best = max(best, r - l - (psum[i+1] - psum[i-k+1]))
        return best

if __name__ == "__main__":
    eventTime = 5
    k = 1
    startTime = [1, 3]
    endTime = [2, 5]
    print(
        Solution().maxFreeTime(
            eventTime=eventTime, k=k, startTime=startTime, endTime=endTime
        )
    )
