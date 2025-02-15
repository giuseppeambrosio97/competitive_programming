
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition_exists(s: str, target: int, index: int = 0, cursum: int = 0):
            if index == len(s) and cursum == target:
                return True
            
            for j in range(index,len(s)):
                csum = cursum+int(s[index:j+1])
                ## use early pruning if csum > target
                if csum <= target and partition_exists(
                    s=s,
                    target=target,
                    index=j+1,
                    cursum=csum
                ):
                    return True
            
            return False
        
        return sum(i*i for i in range(1, n+1) if partition_exists(str(i*i), i))

    
if __name__ == "__main__":
    n = 37
    print(Solution().punishmentNumber(n))