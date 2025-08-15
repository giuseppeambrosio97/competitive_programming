from collections import deque
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        N = 1_000_000
        M = len(blocked)*(len(blocked)-1)//2

        if len(blocked) == 0:
            return True
        
        blocked = set([tuple(b) for b in blocked])

        def neis(x,y):
            res = []
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx, yy = x + dx, y+dy
                if 0 <= xx < N and 0 <= yy < N and (xx,yy) not in blocked:
                    res.append((xx,yy))
            return res
        
        def dfs(s,t):
            visited = set()
            visited.add(tuple(s))
            Q = deque([tuple(s)])
            while Q:
                x,y = Q.popleft()   
                if (x,y) == tuple(t):
                    return True
            
                if len(visited) > M:
                    return True

                for nx,ny in neis(x,y):
                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        Q.append((nx,ny))

            return False
        return dfs(source, target) and dfs(target,source)
    

if __name__ == "__main__":
    blocked = [[537802,17059],[78708,842261],[328635,368483],[979279,797516],[612569,698275],[252668,6127],[257053,758097],[268645,875500],[639173,456448],[903098,1368],[394578,558118],[101294,990763],[651656,466012],[648055,855106],[454065,130529],[75601,74972],[421211,921303],[422588,604894],[835989,193093],[790330,759439],[936054,233555],[93266,613148],[279318,567441],[980048,527253],[43411,172656],[80898,949102],[688078,81351],[834876,77183],[632299,348943],[7701,863301],[339477,46248],[817320,464351],[409911,195474],[633044,507665],[172036,361077],[381949,899844]]
    source = [997128,739012]
    target = [123120,183705]
    print(Solution().isEscapePossible(blocked, source, target))