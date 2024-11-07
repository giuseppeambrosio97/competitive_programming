from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxs = {}

        for i, a in enumerate(nums):
            if a not in idxs:
                idxs[a] = []
            idxs[a].append(i)
            if len(idxs[a]) > 1 and i - idxs[a][-2] <= k:
                return True
        return False

if __name__ == '__main__':

    print(Solution().containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2))