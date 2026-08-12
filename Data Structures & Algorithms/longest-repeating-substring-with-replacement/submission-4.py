class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 1
        for i in range(26):
            start = 0
            seen = []
            for end in range(start, len(s)):
                char_ord = ord(s[end]) - ord('A')
                if char_ord != i:
                    if len(seen) >= k:
                        max_length = max(max_length, end - start)
                        if k!=0:
                            start = seen[0] + 1
                            seen.pop(0)
                        else:
                            start = end + 1
                    seen.append(end)
            max_length = max(max_length, len(s) - start)
                
        return max_length
                
                