class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        groups = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for letter in s:
                freq[ord(letter) - 97] += 1
            groups[str(freq)].append(s)
        return list(groups.values())
            
            
            