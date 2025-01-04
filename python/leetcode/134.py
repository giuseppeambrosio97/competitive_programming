from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total_surplus, current_surplus = 0, 0, 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_surplus += diff
            current_surplus += diff
            
            if current_surplus < 0:
                start = i + 1
                current_surplus = 0
        
        return start if total_surplus >= 0 else -1


if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    t = Solution().canCompleteCircuit(gas, cost)
    print(t)