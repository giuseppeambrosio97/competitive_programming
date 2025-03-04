
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        
        return True

if __name__ == "__main__":
    n=6574365
    print(Solution().checkPowersOfThree(n))