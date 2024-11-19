from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                rq.append(i)
            else:
                dq.append(i)
        

        while rq and dq:
            headr, heads = rq.popleft(), dq.popleft()

            if headr < heads:
                rq.append(headr+n)
            else:
                dq.append(heads+n)
        
        return "Radiant" if len(dq) == 0 else "Dire"


if __name__ == '__main__':
    senate = "RDD"
    s = Solution().predictPartyVictory(senate)
    print(s)