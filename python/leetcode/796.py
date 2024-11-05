class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        def match(i):
            """Return True if the string s[i]... is equal to goal (considering s as circular string)"""
            if len(s) != len(goal):
                return False
            n = len(s)
            
            j = 0
            while j < n and s[(i+j)%n] == goal[j]:
                j += 1
            
            return j == n



        for i, ch in enumerate(s):
            if match(i):
                return True
            
        return False