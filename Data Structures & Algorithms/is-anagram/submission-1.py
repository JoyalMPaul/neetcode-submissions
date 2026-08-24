class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter = ""

        s = list(s)
        t = list(t)
        s.sort()
        t.sort()

        if s != t: 
            return False
        return True