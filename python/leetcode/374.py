# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0


import random 

picked = random.randint(0,10)


def guess(num: int) -> int:
    if picked < num:
        return -1
    elif picked == num:
        return 0
    else:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        while l < r:
            m = (l + r) // 2
            res = guess(m)

            if res == 1:
                l = m + 1
            elif res == -1:
                r = m - 1
            else:
                return m
            
        return l
            
            
if __name__ == '__main__':
    print(Solution().guessNumber(124))