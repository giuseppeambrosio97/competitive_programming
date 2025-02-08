from collections import defaultdict
import heapq


class NumberContainers:

    def __init__(self):
        self.id_to_number = {}
        self.number_to_pq = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.id_to_number[index] = number
        heapq.heappush(self.number_to_pq[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_to_pq:
            return -1
        while self.number_to_pq[number]:
            lowest_id = self.number_to_pq[number][0]
            if self.id_to_number[lowest_id] == number:
                return lowest_id
            heapq.heappop(self.number_to_pq[number])
        return -1
        