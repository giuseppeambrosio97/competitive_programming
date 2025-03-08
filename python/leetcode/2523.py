import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """T(n)=O(n*sqrt(n))."""

        # def is_prime(a:int):
        #     for i in range(2, math.ceil(math.sqrt(a))+1):
        #         if a % i == 0:
        #             return False
        #     return True
            
        # primes = [a for a in range(left,right+1) if is_prime(a)]

        is_prime = [True]*(right+1)

        for i in range(2, right+1):
            for j in range(i*2, right+1, i):
                is_prime[j] = False

        primes = [i for i in range(left, right+1) if is_prime[i]]

        res = [-1,-1]
        diff = math.inf

        for i in range(len(primes)-1):
            if primes[i+1] - primes[i] < diff:
                diff = primes[i+1] - primes[i]
                res = [primes[i], primes[i+1]]

        return res
