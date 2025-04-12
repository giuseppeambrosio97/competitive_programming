# from math import factorial


# class Solution:
#     def countGoodIntegers(self, n: int, k: int) -> int:
#         dictionary = set()
#         base = 10 ** ((n - 1) // 2)
#         skip = n & 1
#         # Enumerate the number of palindrome numbers of n digits
#         for i in range(base, base * 10):
#             s = str(i)
#             s += s[::-1][skip:]
#             palindromicInteger = int(s)
#             # If the current palindrome number is a k-palindromic integer
#             if palindromicInteger % k == 0:
#                 sorted_s = "".join(sorted(s))
#                 dictionary.add(sorted_s)

#         fac = [factorial(i) for i in range(n + 1)]
#         ans = 0
#         for s in dictionary:
#             cnt = [0] * 10
#             for c in s:
#                 cnt[int(c)] += 1
#             # Calculate permutations and combinations
#             tot = (n - cnt[0]) * fac[n - 1]
#             for x in cnt:
#                 tot //= fac[x]
#             ans += tot

#         return ans


from functools import lru_cache
from typing import List


class Solution:

    def countGoodIntegers(self, n: int, k: int) -> int:
        fact = [1]*11
        done = set()

        for i in range(2,11):
            fact[i] = i*fact[i-1]

        res = [0]

        def is_divisible(number: List[int]) -> bool:
            num = 0
            for d in number:
                num = (num * 10 + d) % k
            return num == 0


        @lru_cache(maxsize=None)
        def perm(freq: List[int], nn: int):
            cnt = fact[nn]
            for i in range(10):
                cnt //= fact[freq[i]]
            return cnt

        def count_arrangments(number: List[int]):
            freq = [0]*10
            for digit in number:
                freq[digit] += 1

            tt = tuple(freq)

            if tt in done:
                return 0

            done.add(tt)

            
            total = perm(tt, n)

            if freq[0] <= 0:
                return total

            freq[0] -= 1

            return total - perm(tuple(freq), n-1) #total - invalid
        
        
        def generate_pali(idx: int, number: List[int]):
            if idx >= (n+1) / 2:
                if is_divisible(number):
                    res[0] += count_arrangments(number)
                return
            start = 1 if idx == 0 else 0
            for i in range(start,10):
                number[idx] = number[n-idx-1] = i
                generate_pali(idx+1,number)

        generate_pali(0,[0]*n)
        return res[0]
