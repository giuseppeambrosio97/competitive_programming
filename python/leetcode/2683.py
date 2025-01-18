from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        OSS1: if a is a valid original array then also the flippled version is a valid array
        """
        """O(n)=T(n), S(n)=O(1)."""
        # return sum(derived) % 2 == 0
        """
        Property of XOR
        a^b=c -> b^c=a and a^c=b
        derived[i] = original[i]^original[i+1] -> original[i+1]=original[i]^derived[i]
        
        so starting from original[0] we can construct the enforced array by the condition.
        the value that original[0] can assume can be only 0 or 1 but for the OSS1 we can assume 0 because if exists for
        0 it exists also for 1
        """
        n = len(derived)
        o = [0]*n
        for i in range(n-1):
            o[i+1] = o[i]^derived[i]

        return o[n-1]^o[0] == derived[n-1]


if __name__ == '__main__':
    derived = [1,1,0] 
    t = Solution().doesValidArrayExist(derived)
    print(t)