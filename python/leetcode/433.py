from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(a: str, b: str) -> int:
            cnt = 0
            for ai, bi in zip(a, b):
                if ai != bi:
                    cnt += 1
            return cnt

        Q = deque([startGene])
        visited = set([startGene])
        steps = 0

        while Q:
            for _ in range(len(Q)):
                curr = Q.popleft()
                if curr == endGene:
                    return steps
                for gene in bank:
                    if gene not in visited and diff(curr, gene) == 1:
                        visited.add(gene)
                        Q.append(gene)

            steps += 1

        return -1


if __name__ == "__main__":
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation(startGene, endGene, bank))
