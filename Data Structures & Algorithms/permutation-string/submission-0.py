class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left, right = 0, len(s1)
        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:len(s1)])
        while right < len(s2):
            if s1_counts == s2_counts:
                return True
            else:
                s2_counts[s2[left]] -= 1
                if s2_counts[s2[left]] == 0:
                    del s2_counts[s2[left]]
                s2_counts[s2[right]] += 1
                left += 1
                right += 1
        return s1_counts == s2_counts