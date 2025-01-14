class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        ## if n is odd is not possible a priori        
        if n & 1:
            return False
        ## slocked will contain the indexes of open parentheses locked
        ## sunlocked will contain all unlocked indexes
        slocked, sunlocked = [], []
        ## left to right
        for i, si in enumerate(s):
            if locked[i] == "0":
                sunlocked.append(i)
            elif si == "(":
                slocked.append(i)
            else: # locked and ")"
                if slocked: # prefer the locked parenthesis
                    slocked.pop()
                elif sunlocked: # then prefer the unlocked one
                    sunlocked.pop()
                else: # if there is nothing to match it cannot be valid
                    return False 
        # right to left
        # basically for each locked "(" we must need to have an unlocked index after it
        while slocked and sunlocked and slocked[-1] < sunlocked[-1]:
            slocked.pop(), sunlocked.pop()
        # if something remain return False
        if slocked:
            return False
        return True


if __name__ == '__main__':
    s = "(()())"
    locked = "010100"
    t = Solution().canBeValid(s, locked)
