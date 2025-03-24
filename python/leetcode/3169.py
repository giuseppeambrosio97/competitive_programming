from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()        
        res, current_end = days, 0

        for start, finish in meetings:
            if start > current_end:
                res -= (finish-start+1)
            else:
                res -= max(0,finish-current_end)
            current_end = max(current_end, finish)

        return res
    
if __name__ == "__main__":
    days = 57
    meetings = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]
    print(Solution().countDays(days, meetings))