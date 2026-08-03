class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        if len(s)!=len(t):
            return False
        for idx in range(0,len(s)):
            if s[idx] not in char_count:
                char_count[s[idx]]= 1
            else:
                char_count[s[idx]]+= 1
        for idx in range(0,len(t)):
            if t[idx] not in char_count:
                return False
            else:
                char_count[t[idx]]-=1
        for char in char_count:
            if char_count[char]!=0:
                return False
        return True
        
