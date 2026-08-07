class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        anagrams = {}

        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word not in anagrams:
                anagrams[sort_word] = [word]
            else:
                anagrams[sort_word].append(word)
        
        for key in anagrams:
            output.append(anagrams[key])

        return output