class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vocals = {'a', 'e', 'i', 'o', 'u'}

        count = 0
        for i in range(k):
            if s[i] in vocals:
                count += 1

        i = 1
        best = count
        while i + k - 1 < len(s):
            if s[i-1] in vocals:
                count -= 1
            if s[i+k-1] in vocals:
                count += 1
            best = max(best, count)
            i += 1
        return best


if __name__ == '__main__':
    print(Solution().maxVowels("leetcode", 3))