from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_stop = max([to for _,_, to in trips])
        a = [0]*(max_stop+1)

        for num_passengers, from_, to_  in trips:
            a[from_] += num_passengers
            a[to_] -= num_passengers

        p = 0
        for i in range(max_stop):
            p += a[i]
            if p > capacity:
                return False
        return True

if __name__ == '__main__':
    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    res = Solution().carPooling(trips, capacity)
    print(res)