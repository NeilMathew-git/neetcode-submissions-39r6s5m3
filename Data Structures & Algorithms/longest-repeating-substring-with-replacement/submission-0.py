class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        counts = defaultdict(int)
        left = 0
        best = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            while sum(counts.values()) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, sum(counts.values()))
        return best

        