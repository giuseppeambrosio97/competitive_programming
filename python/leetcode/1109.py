from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        differ = [0]*(n+1)
        
        for f, l, s in bookings:
            differ[f-1] += s
            differ[l] -= s
        
        res = []
        csum = 0
        for i in range(n):
            csum += differ[i]
            res.append(csum)

        return res



if __name__ == '__main__':
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    Solution().corpFlightBookings(bookings, n)