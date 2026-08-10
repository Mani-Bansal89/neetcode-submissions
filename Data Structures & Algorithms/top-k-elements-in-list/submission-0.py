class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
    
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        freq_counter = {}
    
        for num in freq:
            if freq[num] in freq_counter:
                freq_counter[freq[num]].append(num)
            else:
                freq_counter[freq[num]] = [num]

        n = len(nums) 
        output = []
        while k>0:
            if n in freq_counter:
                k = k-len(freq_counter[n])
                output+=freq_counter[n]
            n-=1

        return output
        


            