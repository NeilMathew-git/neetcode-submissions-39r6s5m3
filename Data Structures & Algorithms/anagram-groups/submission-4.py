class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        output = []
        for str in strs:
            sorted_str = sorted(str)
            sorted_str = "".join(sorted_str)

            if sorted_str in anagrams:
                anagrams[sorted_str].append(str)
            else:
                anagrams[sorted_str] = [str]
        for i in anagrams:
            anagram_list = anagrams[i] 
            output.append(anagram_list)
        return output