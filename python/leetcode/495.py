from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt = 0
        for i in range(len(timeSeries) - 1):
            cnt += min(duration, timeSeries[i + 1] - timeSeries[i])
        return cnt + duration if timeSeries else 0



if __name__ == "__main__":
    timeSeries = [0, 2]
    duration = 1
    s = Solution().findPoisonedDuration(timeSeries, duration)
    print(s)
