from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        psum = [0] * (n+1)
        vocals = {'a', 'e', 'i', 'o', 'u'}

        for i in range(1, n+1):
            psum[i] = psum[i-1] + (1 if words[i-1][0] in vocals and words[i-1][-1] in vocals else 0)

        res = []
        for l,r in queries:
            res.append(
                psum[r+1]-psum[l]
            )

        return res
