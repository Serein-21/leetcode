# Last updated: 1/2/2026, 12:18:00 PM
from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def solve(isConnected):
            vis = set()
            n = len(isConnected)
            count = 0
            for i in range(n):
                if i in vis:
                    continue
                count += 1
                vis.add(i)
                q = deque([i])
                while q:
                    el = q.pop()
                    for adj in range(n):
                        if isConnected[el][adj] and adj not in vis:
                            vis.add(adj)
                            q.appendleft(adj)
            return count
        
        # Return the result of calling the solve function
        return solve(isConnected)
