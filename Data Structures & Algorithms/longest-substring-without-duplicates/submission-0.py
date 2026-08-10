class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start,end = 0,0
        max_length = 0
        seen = {}

        while start < len(s):
            while end < len(s) and (s[end] not in seen or seen[s[end]]<start):
                seen[s[end]] = end
                end+=1

            max_length = max(max_length,end-start)
            if end < len(s):
                start = seen[s[end]]+1
                seen[s[end]] = end
                end+=1
            else:
                break

        return max_length