from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2*n-1
        res = [0] * size
        used = set()

        def backtrack(i: int): # current index to fill
            if i == len(res):
                return True
            
            for num in range(n, 0, -1):
                ## Validation steps
                # using num will result in an invalid sequence because it is already been used
                if num in used: 
                    continue
                # num is not used and if num > 1 we have to place two location so if i+num >= size or i+num is already
                # occupied then we cannot place two instances of num -> so is invalid and we cannot use num
                if num > 1 and (i+num >= size or res[i+num]):
                    continue
                
                ## Take decision
                used.add(num)            
                res[i] = num
                if num > 1:
                    res[i+num] = num

                ## Recursive Step
                j = i + 1
                while j < size and res[j]:
                    j+=1
                if backtrack(j):
                    return True

                ## Undo decision because if we are here place num in the index i is not good
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i+num] = 0
            return False

        backtrack(0)
        return res

if __name__ == "__main__":
    print(Solution().constructDistancedSequence(n=3))