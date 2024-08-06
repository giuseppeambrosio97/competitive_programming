import collections as cll
from operator import itemgetter
import math 
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = cll.Counter(word)
        frequencies = sorted(frequencies.items(), key=itemgetter(1), reverse=True)
        cnt = 0
        for idx, fr in enumerate(frequencies):
            m = math.floor(idx / 8) + 1
            cnt += fr[1] * m

        return cnt

if __name__ == '__main__':
    print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))