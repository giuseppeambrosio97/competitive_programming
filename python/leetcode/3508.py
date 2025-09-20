from collections import defaultdict, deque
from typing import List
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.n = memoryLimit
        self.check_set = set()
        self.queue = deque()
        self.destination2timestamp = defaultdict(deque)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        hash_ = f"{source}-{destination}-{timestamp}"
        if hash_ in self.check_set:
            return False
        self.check_set.add(hash_)
        self.queue.append([source,destination,timestamp])
        self.destination2timestamp[destination].append(timestamp)
        if len(self.queue) > self.n:
            s,d,t = self.queue.popleft()
            self.check_set.discard(f"{s}-{d}-{t}")
            self.destination2timestamp[d].popleft()
            
        return True


    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        s, d, t = self.queue.popleft()
        self.check_set.discard(f"{s}-{d}-{t}")
        self.destination2timestamp[d].popleft()
        return [s,d,t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        l = bisect.bisect_left(self.destination2timestamp[destination], startTime)
        r = bisect.bisect_right(self.destination2timestamp[destination], endTime)
        return r-l


if __name__ == "__main__":

    calls = ["Router","addPacket","addPacket","addPacket","getCount"]
    args = [[2],[3,1,3],[1,2,3],[4,5,3],[1,2,3]]

    rr = Router(*args[0])
    for call, arg in zip(calls[1:],args[1:]):
        print(getattr(rr,call)(*arg))
