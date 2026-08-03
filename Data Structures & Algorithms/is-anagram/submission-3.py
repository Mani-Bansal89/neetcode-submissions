class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        for char_t in t:
            if char_t in s:
                s = s.replace(char_t, '',1)
        if len(s) == 0:
            return True
        else:
            return False
