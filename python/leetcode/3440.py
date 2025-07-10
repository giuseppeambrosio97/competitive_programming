from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        free = []
        N = len(startTime)
        prevend = 0
        for i in range(N):
            if prevend < startTime[i]:
                free.append([startTime[i]-prevend, prevend, startTime[i]])
            prevend = endTime[i]
        if prevend < eventTime:
            free.append([eventTime-prevend, prevend,eventTime])

        frees = sorted(free, key=lambda x: -x[0])[:3]

        def find_good(i):
            leng_i = endTime[i] - startTime[i]
            for leng, s, e in frees:
                if startTime[i] not in [s,e] and endTime[i] not in [s,e] and leng >= leng_i:
                    return 0
            return leng_i
                
        best = 0

        for i in range(N):
            # check using frees if thereis at least one non-adjacent and large enough free spot between the largest 3 
            # to place the i-th meeting. If there is sum the adjacent space + the meeting len
            # otherwise sum only the adjent space as answer
            r = eventTime if i == N-1 else startTime[i+1]
            l = 0 if i == 0 else endTime[i-1]
            best = max(best, r - l - find_good(i))

        return best







if __name__ == "__main__":
    eventTime = 10
    startTime = [1,3, 6]
    endTime = [2,5, 7]
    print(Solution().maxFreeTime(eventTime=eventTime, startTime=startTime, endTime=endTime))