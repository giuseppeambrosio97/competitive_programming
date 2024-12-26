from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p, t = sorted(players), sorted(trainers)
        np, nt = len(players), len(trainers)
        cnt = 0
        j = 0
        for i in range(nt):
            if j < np and p[j] <= t[i]:
                cnt += 1
                j += 1
            if j >= np:
                return cnt
            
        return cnt
    
if __name__ == "__main__":
    p = [4,7,9]
    t = [8,2,5,8]
    s = Solution().matchPlayersAndTrainers(p,t)
    print(s)