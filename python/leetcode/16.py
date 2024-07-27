from typing import List
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time complexity:
        - sorting -> O(log n)
        - loops: O(n^2)
            - O(n) first loop
            - O(n/2) second loop

        Overall time complexity: O(n^2)
        
        Space complexity:
        - O(n)
        """
        nums_sorted = sorted(nums)
        left = 0
        closest = sum(nums[:3])

        for left in range(len(nums_sorted)):
            middle = left + 1
            right = len(nums_sorted) - 1
            while middle < right:
                candidate = nums_sorted[left] + nums_sorted[middle] + nums_sorted[right]

                if abs(closest - target) > abs(candidate - target):
                    closest = candidate
                
                if candidate == target:
                    return target
                elif candidate < target:
                    ## if candidate < target then what we can do to improve the current solution is only move the middle
                    # pointer to the right, becuase moving the right pointer will increase the distance
                    middle += 1
                else:
                    ## if candidate > target then what we can do to improve the current solution is only move the right 
                    # pointer to the left, because moving the middle pointer will increase the distance
                    right -= 1

        return closest

                





if __name__ == "__main__":
    s = Solution()

    res = s.threeSumClosest([-1,2,1,-4], 1)
    
    print(res)
