from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = set()

        for i in range(len(arr)-1,-1,-1):
            if arr[i]/2 in m or arr[i]*2 in m:
                return True
            m.add(arr[i])
        return False
    
if __name__ == "__main__":
    arr = [7,1,14,11]
    t = Solution().checkIfExist(arr)
    print(t)