import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.PQ = []
        self.t2p = {}
        self.t2u = {}

        for uid, tid, p in tasks:
            self.add(uid,tid,p)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.t2u[taskId] = userId
        self.t2p[taskId] = priority
        heapq.heappush(self.PQ, (-priority,-taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.t2p[taskId] = newPriority
        heapq.heappush(self.PQ, (-newPriority,-taskId))
        

    def rmv(self, taskId: int) -> None:
        self.t2u[taskId] = -1 # softdelete
        self.t2p[taskId] = -1 # softdelete
        

    def execTop(self) -> int:
        while self.PQ:
            np, ntid = heapq.heappop(self.PQ)
            p, tid = -np, -ntid
            
            if self.t2p.get(tid,-2) == p:
                self.t2p.pop(tid)
                return self.t2u.pop(tid)
        return -1
        


if __name__ == "__main__":

    calls = ["TaskManager","add","edit","execTop","rmv","add","execTop"]
    args = [[[[1,101,8],[2,102,20],[3,103,5]]],[4,104,5],[102,9],[],[101],[50,101,8],[]]

    tm = TaskManager(args[0][0])

    for call, arg in zip(calls[1:],args[1:]):
        print(getattr(tm, call)(*arg))