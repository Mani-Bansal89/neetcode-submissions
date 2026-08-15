class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longprefix = strs[0]
        longestlen = len(strs[0])

        for i in range(0,len(strs)) :
            longprefix = strs[0][:longestlen]
            while longestlen > 0 and strs[i][:longestlen] != longprefix:
                longestlen -= 1
                longprefix = strs[0][:longestlen]

        return longprefix



            