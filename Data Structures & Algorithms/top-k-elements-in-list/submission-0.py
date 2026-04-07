class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counts = Counter(nums)
        print(counts)
        output = []
        for i in range(k):
            most_freq = max(counts, key = lambda x: counts[x])
            output.append(most_freq)
            counts[most_freq] = -1
        return output
        