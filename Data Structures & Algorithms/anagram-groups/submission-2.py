class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            word = strs[i]
            freq_counter = [0]*26
            for j in range(len(word)):
                letter = ord(word[j]) - ord('a')
                freq_counter[letter] += 1
            freq = ','.join(str(freq_counter))

            if freq in anagrams:
                anagrams[freq].append(word)
            else:
                anagrams[freq] = [word]


        output = []
        for key in anagrams:
            output.append(anagrams[key])
        return output


