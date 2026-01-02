# Last updated: 1/2/2026, 12:18:14 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        h=0
        length=len(s)-1
        t=length

        while (h<t):
            (s[h],s[t])=(s[t],s[h])
            t=t-1
            h=h+1

        return s