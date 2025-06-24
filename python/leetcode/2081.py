class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int, base: int) -> bool:
            digit = list()
            while x:
                digit.append(x % base)
                x //= base
            return digit == digit[::-1]
        
        def generate_palindrome(i: int, is_even_l: bool):
            combined = i
            x = i // 10 if not is_even_l else i
            while x:
                combined = combined*10 + x%10
                x //= 10
            return combined

        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 indicates enumerating odd-length palindromes
            # op = 1 indicates enumerating even-length palindromes
            for op in [0, 1]:
                # enumerate i'
                for i in range(left, right):
                    if cnt == n:
                        break
                    combined = generate_palindrome(i, op == 1)
                    if isPalindrome(x=combined,base=k):
                        cnt += 1
                        ans += combined
            left = right

        return ans

if __name__ == "__main__":
    k = 2
    n = 5
    print(Solution().kMirror(k,n))