class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        i, n = 0, len(num)

        while i < n and i <= (n // 2) + 1:
            if num[i] != num[n - i - 1]:
                return False
            i += 1
            
        return True
    
if __name__ == '__main__':
    print(Solution().isPalindrome(0))