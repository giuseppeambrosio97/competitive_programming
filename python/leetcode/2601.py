from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        """
        prev = nums[0]
        for each i, n in nums:
            take the bigger prime number p stricly less than n and such that n - p > rest
            if no such prime number exists return false
            rest  = n - p + 1
        return true
        """
        def is_prime(a: int) -> bool:
            if a == 1:
                return False
            if a == 2:
                return True
            i = 2
            while i <= a // 2:
                if a % i == 0:
                    return False
                i += 1
            return True
        
        def big_prime_less(a: int) -> int:
            for pi in range(a-1, 0, -1):
                if is_prime(pi):
                    return pi
            return -1

        rest = 0
        for ni in nums:            
            pmax = big_prime_less(ni-rest)
            if pmax == -1:
                if ni <= rest:
                    return False
                rest = ni
            else:
                rest = ni - pmax
    
        return True



if __name__ == "__main__":
    nums = [2,3,36,42,51,62,67,72,76,90]
    a = Solution().primeSubOperation(nums)
    print(a)
