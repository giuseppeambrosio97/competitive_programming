from typing import List
import collections as cll

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = cll.deque()
        for curr_a in asteroids:
            while stack and curr_a < 0 < stack[-1]:
                last_a = stack[-1]
                if abs(last_a) == abs(curr_a):
                    stack.pop()
                    break
                elif abs(last_a) > abs(curr_a):
                    break
                else:
                    stack.pop()
            else:
                stack.append(curr_a)

        return list(stack)


if __name__ == '__main__':
    print(Solution().asteroidCollision([10,2,-5]))