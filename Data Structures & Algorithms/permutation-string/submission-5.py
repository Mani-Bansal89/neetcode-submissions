class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_seen = {}
        for char in s1:
            s1_seen[char] = 1 + s1_seen.get(char,0)
        s2_seen = {}
        start = 0
        for end in range(len(s2)):
            char = s2[end]
            if char not in s1_seen:
                start = end + 1
                s2_seen = {}
            else:
                s2_seen[char] = 1 + s2_seen.get(char,0)
            while start < end and s2_seen[char] > s1_seen[char]:
                char2 = s2[start]
                s2_seen[char2] -= 1
                start += 1
            if s2_seen == s1_seen:
                return True
        return False
