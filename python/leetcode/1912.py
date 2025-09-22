from collections import defaultdict
from typing import List
import heapq

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(list)   # movie -> heap of (price, shop)
        self.rented = []                    # global heap of (price, shop, movie)
        self.sm2p = {}                      # (shop, movie) -> price
        self.active_unrented = set()        # set of (shop, movie) currently available
        self.active_rented = set()          # set of (shop, movie) currently rented

        for s, m, p in entries:
            self.sm2p[(s, m)] = p
            heapq.heappush(self.unrented[m], (p, s))
            self.active_unrented.add((s, m))

    def search(self, movie: int) -> List[int]:
        res = []
        buffer = []
        seen = set()

        while len(res) < 5 and self.unrented[movie]:
            p, s = heapq.heappop(self.unrented[movie])
            if (s, movie) not in self.active_unrented:
                # stale copy, skip
                continue
            if (p,s) in seen:
                continue
            # valid
            res.append(s)
            buffer.append((p, s))
            seen.add((p,s))

        # push back valid ones so heap remains intact
        for item in buffer:
            heapq.heappush(self.unrented[movie], item)

        return res

    def rent(self, shop: int, movie: int) -> None:
        self.active_unrented.discard((shop, movie))
        self.active_rented.add((shop, movie))
        heapq.heappush(self.rented, (self.sm2p[(shop, movie)], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.active_rented.discard((shop, movie))
        self.active_unrented.add((shop, movie))
        heapq.heappush(self.unrented[movie], (self.sm2p[(shop, movie)], shop))

    def report(self) -> List[List[int]]:
        res = []
        buffer = []
        seen = set()

        while len(res) < 5 and self.rented:
            p, s, m = heapq.heappop(self.rented)
            if (s, m) not in self.active_rented:
                # stale copy, skip
                continue
            if (s,m) in seen:
                continue
            # valid
            res.append([s, m])
            buffer.append((p, s, m))
            seen.add((s,m))

        # push back valid ones
        for item in buffer:
            heapq.heappush(self.rented, item)

        return res

        
        


if __name__ == "__main__":
    calls = [
        "MovieRentingSystem",
        "search",
        "rent",
        "rent",
        "report",
        "drop",
        "search",
    ]
    args = [
        [3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]],
        [1],
        [0, 1],
        [1, 2],
        [],
        [1, 2],
        [2],
    ]

    mrs = MovieRentingSystem(*args[0])

    for call, arg in zip(calls[1:], args[1:]):
        print(getattr(mrs, call)(*arg))
