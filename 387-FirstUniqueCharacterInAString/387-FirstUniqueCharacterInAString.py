# Last updated: 1/2/2026, 12:18:10 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = {}

        if len(s) == 1:
            return 0

        for i in s:
            if i in maps:
                maps[i] = maps[i] + 1

            else:

                maps[i] = 1
        
        for n in maps :
            if maps[n]==1:
                return s.index(n)

        
        return -1