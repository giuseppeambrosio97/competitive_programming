import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        usable = [(w,i) for i, w in enumerate(servers)] # (weight server, server id)
        heapq.heapify(usable)

        unusable = [] # (when the server become available, weight, server id)
        res = [-1] * len(tasks) 
        time = 0

        for i, task_time in enumerate(tasks):
            time = max(time, i)

            # check if at the current time we can free server
            while unusable and unusable[0][0] <= time:
                _, w, sid = heapq.heappop(unusable)
                heapq.heappush(usable, (w,sid))

            ## there are no free server
            if not usable:
                time = unusable[0][0]
                while unusable and unusable[0][0] <= time:
                    _, w, sid = heapq.heappop(unusable)
                    heapq.heappush(usable, (w, sid))
            ## there are free server
            w, sid = heapq.heappop(usable)
            heapq.heappush(unusable, (time+task_time, w, sid))
            res[i] = sid
        return res

if __name__ == "__main__":
    servers = [5,1,4,3,2]
    tasks = [2,1,2,4,5,2,1]
    print(Solution().assignTasks(servers, tasks))