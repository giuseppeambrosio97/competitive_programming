from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """Brutal force O(n + 100^2)"""
        # position_cnt = Counter(position)
        # min_cost = math.inf
        # for p, _ in position_cnt.items():
        #     v = 0           
        #     for pp, ccnt in position_cnt.items():
        #         if p != pp and abs(p-pp) % 2 != 0:
        #             v += ccnt
        #     min_cost = min(min_cost, v)
        # return min_cost
        """
        OSS1: move chips is free for move odd -> odd and even -> even.
        OSS2: we pay only fro odd -> even and even -> odd
        OSS3: all chips at even (odd) position can be moved at the same position of free
        OSS4: so make sense to first move all even chips at even position and all odd chips at odd position
              and then pay one to move chips to odd or even and then move free at the same position
        for example:
            45 even chips, 50 odd chips
            move 45 even chips to odd and pay 45 and then move for free at the same position of the 50 odd chips
        T(n)=O(n), S(n)=O(1)
        """
        odd_cnt = sum(1 for p in position if p & 1)
        even_cnt = len(position) - odd_cnt
        return min(odd_cnt, even_cnt)

if __name__ == '__main__':
    position = [1,2,2,2,2]
    t = Solution().minCostToMoveChips(position)
    print(t)