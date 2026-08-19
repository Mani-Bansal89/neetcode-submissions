class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify_max(nums)
        self.klargest = []
        while len(nums)>0 and k > 0 :
            heapq.heappush(self.klargest,heapq.heappop_max(nums))
            k -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.klargest,val)
        if len(self.klargest) > self.k:
            heapq.heappop(self.klargest)
        return self.klargest[0]

