import math


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # l=0,r=0 index, cnt black

        # move r until n increment +1
        #   if cnt == k -> return l-r+1-cnt
        #   r++
        #   if b[r] == "B" -> cnt++
        #   if cnt >= k -> l++, 

        l, n = 0, len(blocks)
        cnt_white = 0
        res = math.inf

        for r in range(n):
            if blocks[r] == "B":
                cnt_white+=1
            if r-l+1 == k:
                res = min(res, r-l+1-cnt_white)
                if blocks[l] == "B":
                    cnt_white -= 1
                l+=1
        return res
    
if __name__ == "__main__":
    blocks = "WBWBBBW"
    k = 2
    print(Solution().minimumRecolors(blocks, k))