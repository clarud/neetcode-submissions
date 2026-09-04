class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter
        groups = defaultdict(list)
        for s in strs:
            key = sorted(s)
            groups[tuple(key)].append(s)
        return list(groups.values())
            
            
            