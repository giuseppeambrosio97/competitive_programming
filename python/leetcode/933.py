"""
import bisect

class RecentCounter:

    def __init__(self):
        self.values = []

    def ping(self, t: int) -> int:
        self.values.append(t)
        _lb = t - 3000
        if self.values[0] >= _lb:
            return len(self.values)
        else:
            return len(self.values) - bisect.bisect_left(self.values, _lb)

implementation using a list and binary search.

the ping operation T(n) = O(log n), S(n) = O(n)
considering n the number of requests (# of ping operations)
T(n) = O(logn)
S(n) = O(n)
"""

from collections import deque

class RecentCounter:
    """
    Implementation using a FIFO
    T(n) = O(1)
    S(n) = O(1)
    """

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

if __name__ == '__main__':
    recentCounter = RecentCounter()
    recentCounter.ping(1)
    recentCounter.ping(100)
    recentCounter.ping(3001)
    recentCounter.ping(3002)