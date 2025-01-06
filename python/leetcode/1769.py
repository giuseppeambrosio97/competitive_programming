from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """Brute force O(n^2)"""
        # n = len(boxes)
        # res = [0]*n 
        # for i in range(n):
        #     j = (i + 1) % n
        #     v = 0
        #     while j != i:
        #         if boxes[j] == "1":
        #             v += abs(j-i)
        #         j = (j + 1) % n
        #     res[i] = v
        # return res
        """Two pass: first left to right and second right to left. T(n)=(3n), S(n)=O(3n)"""
        # n = len(boxes)
        # lr = [0]*n
        # cnt = 0
        # for i in range(1, n):
        #     if boxes[i-1] == "1":
        #         cnt += 1
        #     lr[i] = lr[i-1] + cnt
        # rl = [0]*n
        # cnt = 0
        # for i in range(n-2,-1,-1):
        #     if boxes[i+1] == "1":
        #         cnt += 1
        #     rl[i] = rl[i+1] + cnt
        # return [rl_+lr_ for lr_,rl_ in zip(lr,rl)]
        """1 loop solution"""
        n = len(boxes)
        res = [0]*n
        balls_to_left = 0
        moves_to_left = 0 ## basically the prefix sum l->r of balls_to_left lr[i]
        balls_to_right = 0
        moves_to_right = 0 ## basically the prefix sum r->l of balls_to_right rl[i]
        for i in range(n):
            # l->r
            res[i] += moves_to_left
            balls_to_left += int(boxes[i])
            moves_to_left += balls_to_left

            # r->l 
            t = n-i-1
            res[t] += moves_to_right
            balls_to_right += int(boxes[t])
            moves_to_right += balls_to_right
        
        return res




if __name__ == '__main__':
    boxes = "0101010"
    t = Solution().minOperations(boxes)
    print(t)