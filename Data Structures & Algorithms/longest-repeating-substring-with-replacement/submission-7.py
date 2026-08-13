class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        count = {}
        max_freq = 0
        result = 0

        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            max_freq = max(max_freq, count[s[end]])

            while (end - start + 1) - max_freq > k:
                count[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)
        return result

            