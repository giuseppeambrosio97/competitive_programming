import math

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        max_val = 10**9
        max_power = math.floor(math.log2(max_val))

        # Precompute digit signatures of all powers of 2
        power_signatures = {tuple(sorted(str(1 << i))) for i in range(max_power + 1)}

        # Check if n's digits match any power of 2's digits
        return tuple(sorted(str(n))) in power_signatures

    

if __name__ == "__main__":
    n = 24
    print(Solution().reorderedPowerOf2(n))