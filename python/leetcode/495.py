from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        end = 0

        cnt = 0
        for t in timeSeries:
            if t > end:
                cnt += duration
            else:
                cnt += max(0, t + duration - end)
            end = max(end, t + duration)

        return cnt


if __name__ == "__main__":
    timeSeries = [0, 2]
    duration = 1
    s = Solution().findPoisonedDuration(timeSeries, duration)
    print(s)
