

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        def atoi(ch: str) -> int:
            return ord(ch) - 97
        counter = [0]*26
        for si in s:
            counter[atoi(si)] += 1
        for _ in range(t):
            new_counter = [0]*26
            for ch in range(26):
                if ch not in counter:
                    continue
                if ch == 25:
                    new_counter[0] = (new_counter[0] + counter[25]) % MOD
                    new_counter[1] = (new_counter[1] + counter[25]) % MOD
                else:
                    new_counter[ch+1] = (new_counter[ch+1] + counter[ch]) % MOD
            counter = new_counter[:]
        return sum(counter) % MOD   
     
if __name__ == "__main__":
    s = "azbk"
    t = 1
    print(Solution().lengthAfterTransformations(s,t))