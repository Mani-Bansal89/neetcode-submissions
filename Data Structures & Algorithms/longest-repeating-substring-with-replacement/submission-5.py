class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 1
        for i in range(26):
            start = 0
            seen = []
            for end in range(len(s)):
                char_ord = ord(s[end]) - ord('A')
                if (char_ord != i):
                    seen.append(end)
                while len(seen) > k:
                    start = seen[0] + 1
                    seen.pop(0)
                max_length = max(max_length, end - start + 1)
                
        return max_length
                
                