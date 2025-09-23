class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        part1, part2 = version1.split("."), version2.split(".")
        N1, N2 = len(part1), len(part2)
        for i in range(max(N1,N2)):
            p1 = int(part1[i]) if i < N1 else 0
            p2 = int(part2[i]) if i < N2 else 0
            if p1 < p2:
                return -1
            elif p1 > p2:
                return 1
        return 0